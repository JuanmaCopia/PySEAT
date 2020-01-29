
import copy
from collections.abc import Iterable

from branching_steps import LazyStep, ConditionalStep
import proxy as proxy
from enum import Enum

# TODO: Check in lazy initializations that the object has to be
# a tracked one, that is to say or a parameter, o the self, or 
# a previously created one
# TODO: Manage exceptions raised when the types are not specified or 
# incorrectly specified
# TODO: Support preconditions and posconditions
# TODO: Check what happen with objects like list and dict... in instanciation
# method
# TODO: Support other symbolic types like list, tuple, dict, slices

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class MaxDepthException(Error):
    """Exception raised when the maximum exploration depth
    is reached.
    """

    def __init__(self):
        self.message = "Max exploration depth reached"

class ClassNotDocumentedError(Error):
    """Exception raised when an user defined class has
    no docstring on his init method.
    """

    def __init__(self, message):
        self.message = message

class UnsatBranchError(Error):
    """Exception raised when a branch is not satisfacible.
    """

    def __init__(self):
        self.message = "Unsat branch"

class RepOkFailException(Error):
    """Exception raised when the maximum exploration depth
    is reached.

    Attributes:
        message -- explanation of the error
        cls -- Class
    """

    def __init__(self, message, cls):
        self.message = message


class ReturnValueRepOkFail(Error):
    """Exception raised when the maximum exploration depth
    is reached.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "The returned value does not pass the repok()"


class Status(Enum):
    OK = 0
    PRUNED = 1
    FAIL = 2

class ExecutionStats:
    def __init__(self, exec_number: int):
        self.number = exec_number
        self.status = Status.PRUNED
        self.self_structure = None
        self.concrete_self = None
        self.args = []
        self.concrete_args = []
        self.exception = None
        self.returnv = None
        self.concrete_return = None
        self.end_self_state = None
        self.model = None
        self.pathcondition = []
        self.errors = []

class SEEngine:

    _branching_points: list
    _path_condition: list
    _current_bp: int
    _current_depth: int
    _total_paths: int
    _pruned_by_depth: int
    _pruned_by_error: int
    _pruned_by_repok: int

    _is_method: bool
    _function = None    # Function under exloration
    _func_args_types = [] # Initial arguments, they could be symbolic or a instrumented reference object
    _max_depth: int

    _self_class: type
    _real_to_proxy: dict
    _class_to_params: dict

    _successes: int
    _failures: int
    _complete_exec: int

    @classmethod
    def initialize(cls, target_data: dict):
        cls._self_class = target_data["class"]
        cls._function = target_data["function"]
        cls._args_types = target_data["args_types"]
        cls._return_type = target_data["return_type"]
        cls._repok = target_data["repok"]
        cls._class_to_params = target_data["class_to_params"]
        cls._real_to_proxy = target_data["real_to_proxy"]
        cls._max_depth = target_data["max_depth"]
        if cls._self_class:
            cls._is_method = True
        cls._branching_points = []
        cls._path_condition = []
        cls._current_bp = 0
        cls._current_depth = 0
        cls._total_paths = 0
        cls._pruned_by_depth = 0
        cls._pruned_by_error = 0
        cls._pruned_by_repok = 0
        cls._successes = 0
        cls._failures = 0
        cls._complete_exec = 1

    @classmethod
    def explore(cls): 
        unexplored_paths = True
        while unexplored_paths:
            cls.reset_exploration()
            
            args = [cls.instantiate(a) for a in cls._args_types]

            result = cls.execute_program(args)
            yield(result)

            cls.remove_explored_branching_points()

            if not cls._branching_points:
                unexplored_paths = False
    
    @classmethod
    def reset_exploration(cls):
        cls._path_condition = []
        cls._current_bp = 0
        cls._current_depth = 0
        for k in cls._class_to_params.keys():
            k._vector = [None]

    @classmethod
    def execute_program(cls, args):
        cls._total_paths += 1    
        stats = ExecutionStats(cls._complete_exec)
        try:
            if cls._is_method:
                the_self = args[0]
                args = args[1:]
                method = getattr(the_self, cls._function.__name__)
                if args:
                    returnv = method(*args)
                else:
                    returnv = method()
                if proxy.is_symbolic_bool(returnv):
                    returnv = returnv.__bool__()
            # TODO: make it work for a non method function
        except UnsatBranchError:
            cls._pruned_by_error += 1
        except MaxDepthException:
            cls._pruned_by_depth += 1
        except RepOkFailException:
            cls._pruned_by_repok += 1
        except Exception as e:
            if not cls.expected(e):
                stats.status = Status.FAIL
            else:
                stats.status = Status.OK
            stats.exception = e
        else:
            stats.status = Status.OK

        finally:
            if stats.status == Status.PRUNED:
                return stats
            cls._complete_exec += 1
            stats.pathcondition = cls._path_condition
            stats.model = proxy.smt.get_model(cls._path_condition)
            stats.self_structure = the_self
            stats.concrete_self = cls._concretize(copy.deepcopy(the_self), stats.model)
            if args:
                stats.concrete_args = cls._concretize(copy.deepcopy(args), stats.model)

            if stats.exception:
                cls.status_count(stats.status)
                return stats

            if not cls.check_repok(returnv):
                stats.status = Status.FAIL
                stats.errors.append("Return value RepOk fail")
            if not cls.check_repok(the_self):
                stats.status = Status.FAIL
                stats.errors.append("Self RepOk fail")
            stats.returnv = returnv
            stats.concrete_return = cls._concretize(copy.deepcopy(stats.returnv), stats.model)
            cls.status_count(stats.status)
            return stats

    @classmethod
    def status_count(cls, status):
        if status == Status.OK:
            cls._successes += 1
        else:
            cls._failures += 1

    @classmethod
    def expected(cls, exception):
        return isinstance(exception, ValueError)

    @classmethod
    def check_repok(cls, obj):
        if proxy.is_user_defined(type(obj)):
            return obj.rep_ok()
        return True 


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
        if not cls._branching_points:
            return None

        last_bp = cls._branching_points[-1]
        last_bp.advance_branch()

        while cls._branching_points and last_bp.all_branches_covered():
            del cls._branching_points[-1]
            if cls._branching_points:
                last_bp = cls._branching_points[-1]
                last_bp.advance_branch()

    @classmethod
    def get_next_lazy_step(cls, lazy_class, vector):
        if cls._max_depth < cls._current_depth:
            raise MaxDepthException
        cls._current_depth += 1

        if cls._current_bp < len(cls._branching_points):
            branch_point = cls._branching_points[cls._current_bp]
            assert(isinstance(branch_point, LazyStep))
            index = branch_point.get_branch()    
            cls._current_bp += 1

            if index < len(vector):
                return vector[index]

            n = cls.create_new_object(lazy_class)    
            vector.append(n)
            return n

        cls._branching_points.append(LazyStep(len(vector)))
        cls._current_bp += 1
        return None   


    @classmethod
    def create_new_object(cls, lazy_class):
        init_types = cls.get_init_types(lazy_class)
        init_args = [cls.instantiate_only_primitives(a) for a in init_types]
        return lazy_class(*init_args)


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
        if true_cond == "sat" and not false_cond == "sat":
            return True
        if false_cond == "sat" and not true_cond == "sat":
            return False 
        if true_cond != "sat" and false_cond != "sat":
            raise UnsatBranchError()

    @classmethod
    def get_next_conditional_step(cls):
        if cls._max_depth < cls._current_depth:
            raise MaxDepthException  
        cls._current_depth += 1

        if cls._current_bp < len(cls._branching_points):
            assert(isinstance(cls._branching_points[cls._current_bp], ConditionalStep))
            bool_value = cls._branching_points[cls._current_bp].get_branch()
        else:
            cls._branching_points.append(ConditionalStep())
            bool_value = True

        cls._current_bp += 1
        return bool_value

    @classmethod
    def ignore_if(cls, value, instance):
        if value:
            raise RepOkFailException(type(instance), "Repok Failed")
            

    @classmethod
    def instantiate(cls, param_type):
        if param_type in cls._real_to_proxy.keys():
            return cls._real_to_proxy[param_type]()
        elif param_type == type(None):
            return None
        elif proxy.is_user_defined(param_type):
            return cls.create_instance(param_type)
        return param_type()
    
    @classmethod
    def get_init_types(cls, user_def_class):
        class_args = copy.deepcopy(cls._class_to_params[user_def_class])
        number_params = user_def_class.__init__.__code__.co_argcount
        if (number_params - 1 != len(class_args)):
            raise ClassNotDocumentedError("Docstring not found in: " + str(user_def_class))
        return class_args

    @classmethod
    def create_instance(cls, user_def_class):
        class_args = cls.get_init_types(user_def_class)

        for i, ptype in enumerate(class_args):
            # If supported symbolic type_
            if ptype in cls._real_to_proxy.keys():
                class_args[i] = cls._real_to_proxy[ptype]()
            elif proxy.is_user_defined(ptype):
                class_args[i] = None
            else:
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
        return arg()

    @classmethod
    def statistics(cls):
        data = {}
        data["explored"] = cls._total_paths - cls._pruned_by_depth - cls._pruned_by_repok - cls._pruned_by_error
        data["total_paths"] = cls._total_paths
        data["pruned_by_repok"] = cls._pruned_by_repok
        data["pruned_by_depth"] = cls._pruned_by_depth
        data["pruned_by_error"] = cls._pruned_by_error
        data["successes"] = cls._successes
        data["failures"] = cls._failures
        return data