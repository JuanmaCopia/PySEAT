
import copy
from collections.abc import Iterable

from branching_steps import LazyStep, ConditionalStep
from exception_mod import MaxDepthException, ClassNotDocumentedError, UnsatBranchError

import proxy as proxy

# TODO: Check what happen when a class is not documented
# TODO: Check what happen when de contract doesnt document the right amount of parameters
# in init methon and also in the function to explore
# TODO: Support preconditions and posconditions
# TODO: Make symbolic all attr of an instance, not only the ones on the contract
# In order to do this the entire class should be documented with all it's attributes
# and its types. It also can document class atributes to support them.
# TODO: Check what happen with objects like list and dict... in instanciation
# method

class SEEngine:

    _branching_points = []
    _path_condition = []
    _current_bp = 0
    _current_depth = 0
    _total_paths = 0
    _pruned = 0
    _pruned_by_error = 0


    _is_method = False
    _function = None    # Function under exloration
    _func_args_types = [] # Initial arguments, they could be symbolic or a instrumented reference object
    _max_depth = 10

    _self_class = None
    _real_to_proxy = {}
    _class_params_map = {}

    @classmethod
    def initialize(cls, function, func_args_types, max_depth, class_params_map, primitives, self_class=None):
        # TODO: Add kwargs
        cls._function = function
        cls._func_args_types = func_args_types
        cls._max_depth = max_depth

        if self_class:
            cls._is_method = True

        cls._class_params_map = class_params_map
        cls._self_class = self_class
        cls._real_to_proxy =  primitives
        

    @classmethod
    def exploration(cls):
        for r in cls.explore():
            yield r

    @classmethod
    def explore(cls): 

        unexplored_paths = True

        while unexplored_paths:
            cls._path_condition = []
            cls._current_bp = 0
            cls._current_depth = 0
            cls._total_paths += 1


            cls.reset_vectors()

            args = [cls.instantiate(a) for a in cls._func_args_types]

            try:
                result = cls.execute_program(args)
            except UnsatBranchError as e:
                raise e
            except MaxDepthException:
                cls._pruned += 1
            except ClassNotDocumentedError as e:
                cls._pruned_by_error += 1
                raise e
            else:
                yield(result)
            
            cls.remove_explored_branching_points()

            if not cls._branching_points:
                unexplored_paths = False
    
    @classmethod
    def reset_vectors(cls):
        for k in cls._class_params_map.keys():
            k._vector = [None]


    @classmethod
    def execute_program(cls, args):
        try:
            if cls._is_method:
                # if its a method i know that args[0] is the self
                the_self = args[0]
                args = args[1:]
                method = getattr(the_self, cls._function.__name__)
                if args:
                    returnv = method(*args)
                else:
                    returnv = method()
                # If the method returns a boolean expression, it
                # isnt evaluated, so neither added to path condition..
                # with the next line we force to evaluate tha missing
                # boolean expression
                if proxy.is_symbolic_bool(returnv):
                    returnv = returnv.__bool__()
                # TODO: make it work for a non method function    
                #else:
                    # function = cls._function
                    # returnv = function(*nargs)
        except AttributeError as e:
            raise e
        else:

            result = {}
            result["self"] = the_self 
            result["returnv"] = returnv
            result["path_codition"] = cls._path_condition
            result["model"] = proxy.smt.get_model(cls._path_condition)
            result["conc_ret"] = cls._concretize(copy.deepcopy(result["returnv"]), result["model"])
            result["conc_self"] = cls._concretize(copy.deepcopy(result["self"]), result["model"])
        return result

    @classmethod
    def _concretize(cls, obj, model):
        #FIXME: Hay que iterar sobre builtins que puedan contener ProxyObjects
        if obj is None:
            return None
        elif proxy.is_symbolic(obj):
            return obj._concretize(model)
        elif isinstance(obj, list):
            return [cls._concretize(x, model) for x in obj]
        elif isinstance(obj, tuple):
            return tuple([cls._concretize(x, model) for x in obj])
        elif proxy.is_user_defined(obj):
            # User defined (abstract) class
            # obj.__dict__ returns all instance-only defined attributes
            if obj.concretized:
                return obj
            obj.concretized = True
            try:
                for name in obj.__dict__:
                    # TODO: Hacerlo genérico, incluyendo atributos de clase
                    attr = getattr(obj, name)
                    if not callable(attr):
                        setattr(obj, name, cls._concretize(attr, model))
            except AttributeError:
                # TODO: Check wtf is this
                if isinstance(obj, Iterable):
                    pass
            return obj
        else:
            # i think this is executed when the object is a builtin or a 
            # callable
            return obj


    @classmethod
    def remove_explored_branching_points(cls):
        # Advance last branch 
        if not cls._branching_points:
            return None
        last_bp = cls._branching_points[-1]
        last_bp.advance_branch()
        # While is not empty and..
        while cls._branching_points and last_bp.all_branches_covered():
            # Delete last branching point
            del cls._branching_points[-1]
            # Advance branch in the new last branching point
            if cls._branching_points:
                last_bp = cls._branching_points[-1]
                last_bp.advance_branch()

    @classmethod
    def get_next_lazy_step(cls, lazy_class, vector):
        # TODO: Think about it: Backup last lazy step with a copy
        # if is last lazy step()       Esto quizas se pueda hacer siempre, total el ultimo es el que va a quedar
        # backup = copy.deepcopy(cls._self_class._vector)

        if cls._max_depth < cls._current_depth:
            raise MaxDepthException
        cls._current_depth += 1

        # if is the branching point already exist
        if cls._current_bp < len(cls._branching_points):

            # Getting the corresponding index
            branch_point = cls._branching_points[cls._current_bp]
            assert(isinstance(branch_point, LazyStep))
            index = branch_point.get_branch()    
            cls._current_bp += 1
            # if is one of the previously created structures
            if index < len(vector):
                return vector[index]
            # Else return a new structure

            # TODO: is it ok to raise an exception? what else is possible?
            try:
                init_types = cls._class_params_map[lazy_class]
            except KeyError:
                raise ClassNotDocumentedError(lazy_class)
            else:
                init_args = [cls.instantiate_only_primitives(a) for a in init_types]
                n = lazy_class(*init_args)
                vector.append(n)

            return n
        # Else create the new branching point
        cls._branching_points.append(LazyStep(len(vector)))
        cls._current_bp += 1
        return None   

    @classmethod
    def evaluate(cls, bool_proxy):
        partial_solve = cls._get_partial_solve(bool_proxy)
        if partial_solve != None:
           return partial_solve

        condition = bool_proxy.formula
        condition_value = cls.get_next_conditional_step()

        if condition_value:
            cls._path_condition.append(condition)
        else:
            cls._path_condition.append(proxy.smt.Not(condition))

        # TODO: Check if next lines are necessary
        if not condition_value:
            bool_proxy.formula = proxy.smt.Not(bool_proxy.formula)
        return condition_value

    @classmethod
    def is_pathcondition_sat(cls):
        conditions = True
        for c in cls._path_condition:
            conditions = proxy.smt.And(conditions, c)
        result  = proxy.smt.check(conditions)
        if result == "sat":
            return True
        else:
            return False

    @classmethod
    def _get_partial_solve(cls, bool_proxy):
        """
        :returns: None if constrains haven't define a concrete value yet,
                  else returns that concrete value (True or False).
        It tries to obtain a bool value if possible. Without branching.
        """
        conditions = True
        for c in cls._path_condition:
            conditions = proxy.smt.And(conditions, c)
        true_cond  = proxy.smt.check(proxy.smt.And(conditions, bool_proxy.formula))
        false_cond = proxy.smt.check(proxy.smt.And(conditions, proxy.smt.Not(bool_proxy.formula)))
        # TODO: Que pasa si es indecidible?
        if true_cond == "sat" and not false_cond == "sat":
            return True
        if false_cond == "sat" and not true_cond == "sat":
            return False    

    @classmethod
    def get_next_conditional_step(cls):
        if cls._max_depth < cls._current_depth:
            raise MaxDepthException
        
        cls._current_depth += 1

        # if is the branching point already exist
        if cls._current_bp < len(cls._branching_points):
            assert(isinstance(cls._branching_points[cls._current_bp], ConditionalStep))
            bool_value = cls._branching_points[cls._current_bp].get_branch()
        else:
            cls._branching_points.append(ConditionalStep())
            bool_value = True

        cls._current_bp += 1
        return bool_value

    @classmethod
    def instantiate(cls, param_type):
        if param_type in cls._real_to_proxy.keys():
            return cls._real_to_proxy[param_type]()
        elif param_type == type(None):
            return None
        elif proxy.is_user_defined(param_type):
            return cls.create_instance(param_type)
        # TODO: Check if this is working
        # with this I intend to catch types not suported, like dictionaries
        return param_type()
    
    @classmethod
    def create_instance(cls, user_def_class):
        class_args = copy.deepcopy(cls._class_params_map[user_def_class])
        for i, ptype in enumerate(class_args):
            # If supported symbolic type_
            if ptype in cls._real_to_proxy.keys():
                class_args[i] = cls._real_to_proxy[ptype]()
            elif proxy.is_user_defined(ptype):
                class_args[i] = None
            else:
                # TODO: Check if this is working
                # with this I intend to catch types not suported, like dictionaries
                class_args[i] = ptype()

        if not class_args:
            new_instance = user_def_class()
        else:
            new_instance = user_def_class(*class_args)
        user_def_class._vector = [None, new_instance]
        return new_instance

    @classmethod
    def instantiate_only_primitives(cls, arg):
        if arg in cls._real_to_proxy.keys():
            return cls._real_to_proxy[arg]()
        elif arg == type(None) or proxy.is_user_defined(arg):
            return None
        # Else
        # TODO: Check if this is working
        # with this I intend to catch types not suported, like dictionaries
        return arg()

    @classmethod
    def statistics(cls):
        data = {}
        data["explored"] = cls._total_paths - cls._pruned
        data["total_paths"] = cls._total_paths
        data["pruned_paths"] = cls._pruned
        return data