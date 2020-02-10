"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynammically allocated structures with the use of lazy initialization.

"""

import copy
from collections.abc import Iterable

from pygse.branching_steps import LazyStep, ConditionalStep
from pygse.stats import Status, ExecutionStats, GlobalStats
from pygse.engine_errors import UnsatBranchError, MissingTypesError, RepOkFailException
from pygse.engine_errors import MaxDepthException
import pygse.proxy as proxy

# TODO: Check in lazy initializations that the object has to be
# a tracked one, that is to say or a parameter, o the self, or
# a previously created one. New objects created in the method
# under test should be treated as initialized in alll its fields
# TODO: Manage exceptions raised when the types are not specified or
# incorrectly specified
# TODO: Support preconditions and posconditions
# TODO: Check what happen with objects like list and dict... in instanciation
# method
# TODO: Support other symbolic types like list, tuple, dict, slices


class SEEngine:
    """Symbolic Execution engine.

    Performs symbolic execution on programs. Handles complex
    dynammically allocated structures with the use of lazy initialization.

    Attributes:
        _branching_points (list): Represents the desitions made at the program
        symbolic execution. The program execution has two possible branching
        scenarios:
            - Lazy Initialization Step: It happens when a user-defined class field
            is accessed, so the engine must initialize it to each posibility creating
            differents executions paths. The possible choices are initializate field to:
                - None
                - Any previous created instances of the user-defined class.
                - A new instance of that class.
            - Conditional Step: It happens the execution reachs a condition over
            symbolic fields, so two there are two possible decisions: make it True
            or make it False, generating different path executions.

        _path_condition (list): Collects all the path constraints of the current execution.

        _current_bp (LazyStep, ConditionalStep): Is the current branching point, it could
        be a Lazy Initialization Stem or a Conditional Step. 

        _current_depth (int): Depth's of the current execution tree.

        _max_depth (int): Max depth search, any execution that exeeds this value is pruned.

        _globalstats (GlobalStats): Contains the overall statistics of all executed
        program paths.

        _sut (SUT): Data of the program under test, contains the method or function,
        parameter types, etc.

        _real_to_proxy (dict): Maps builtin supported types to Symbolic Ones.
    """
    _branching_points = []
    _path_condition = []
    _current_bp = 0
    _current_depth = 0
    _max_depth = 0

    _globalstats = None
    _sut = None
    _real_to_proxy = {}

    _lazy_backups = {}

    @classmethod
    def initialize(cls, sut_data, max_depth):
        """Setups the initial values of the engine.

        Args:
            sut_data: System under test (function, types, classes).
            max_depth: Depth limit of the exploration tree.
        """
        cls._sut = sut_data
        cls._branching_points = []
        cls._path_condition = []
        cls._current_bp = 0
        cls._current_depth = 0
        cls._globalstats = GlobalStats()
        cls._max_depth = max_depth
        cls._real_to_proxy = {x.emulated_class: x for x in proxy.ProxyObject.__subclasses__()}

    @classmethod
    def explore(cls):
        """Main method, implements the generalized symbolic execution.

        Yields:
            ExecutionStats: The result of the execution of the function under test
        """
        unexplored_paths = True
        while unexplored_paths:
            cls._reset_exploration()

            args = [cls._symbolic_instantiation(a) for a in cls._sut.types]

            result = cls._execute_program(args)
            yield (result)

            cls._remove_explored_branches()

            if not cls._branching_points:
                unexplored_paths = False

    @classmethod
    def _reset_exploration(cls):
        """Resets the exploration variables to it's initial values.
        """
        cls._path_condition = []
        cls._current_bp = 0
        cls._current_depth = 0
        for k in cls._sut.class_params_map.keys():
            k._vector = [None]
            cls._lazy_backups[k] = LazyBackup()
        

    @classmethod
    def _execute_program(cls, args):
        """Executes the method and returns the result.

        Collect and returns all the execution data, like the returned
        value, the final state of the self, the path condition, the
        model, exceptions raised, concrete values of arguments and
        result, and state.

        Args:
            args (List): List of the arguments to call the function
                or method.

        Returns:
            ExecutionStats: The result of the execution of the function
            under test
        """
        cls._globalstats.total_paths += 1
        stats = ExecutionStats(cls._globalstats.complete_exec)
        returnv = None
        the_self = None
        try:
            if cls._sut.is_method:
                the_self = args[0]
                args = args[1:]
                method = getattr(the_self, cls._sut.function.__name__)
                if args:
                    returnv = method(*args)
                else:
                    returnv = method()
                if proxy.is_symbolic_bool(returnv):
                    returnv = returnv.__bool__()
            # TODO: make it work for a non method function
        except UnsatBranchError:
            cls._globalstats.pruned_by_error += 1
        except MaxDepthException:
            cls._globalstats.pruned_by_depth += 1
        except RepOkFailException:
            cls._globalstats.pruned_by_repok += 1
        except Exception as e:
            if not cls._expected(e):
                stats.status = Status.FAIL
            else:
                stats.status = Status.OK
            stats.exception = e
        else:
            stats.status = Status.OK
        finally:
            if stats.status == Status.PRUNED:
                return stats
            cls._globalstats.complete_exec += 1
            stats.pathcondition = cls._path_condition
            stats.model = proxy.smt.get_model(cls._path_condition)
            
            ##
            the_self = cls._lazy_backups[cls._sut.sclass].get_entity()
            cls.retrieve_inputs(args)
            ##
            stats.self_structure = the_self
            stats.concrete_self = cls._concretize(copy.deepcopy(the_self), stats.model)
            if args:
                stats.concrete_args = cls._concretize(copy.deepcopy(args), stats.model)

            if stats.exception:
                cls._globalstats.status_count(stats.status)
                return stats

            if not cls._check_repok(returnv):
                stats.status = Status.FAIL
                stats.errors.append("Return value RepOk fail")
            if not cls._check_repok(the_self):
                stats.status = Status.FAIL
                stats.errors.append("Self RepOk fail")
            stats.returnv = returnv
            stats.concrete_return = cls._concretize(
                copy.deepcopy(stats.returnv), stats.model
            )
            cls._globalstats.status_count(stats.status)
            return stats

    @classmethod
    def retrieve_inputs(cls, args_list):
        for i, arg in enumerate(args_list):
            if proxy.is_user_defined(arg):
                args_list[i] = cls._lazy_backups[type(arg)].get_entity()

    @classmethod
    def _expected(cls, exception):
        """Checks whether an exception is expected or not.

        Args:
            exception (Exception): A raised exception during
                the execution of a function.

        Returns:
            True if expected, False otherwise.
        """
        return isinstance(exception, ValueError)

    @classmethod
    def _check_repok(cls, instance):
        """Checks whether an instance pass it's class invariant o not.

        Args:
            instance: instance of a user_defined_class

        Returns:
            True if instance is valid (pass it's repok), False otherwise.
        """
        if proxy.is_user_defined(type(instance)):
            return instance.rep_ok()
        return True

    @classmethod
    def _concretize(cls, symbolic, model):
        """Creates the concrete object.

        Creates the concrete object from a symbolic (builtin symbolic)
        or a partially symbolic (user-defined) one and the model 
        describing it's restrictions.

        Args:
            symbolic: a symbolic builtin or a partially symbolic
                user-defined class.
            model: Model describing the constraints that the object
                must acomplish.

        Returns:
            The concrete object represented by symbolic and the model.
        """
        # FIXME: Hay que iterar sobre builtins que puedan contener ProxyObjects
        if symbolic is None:
            return None
        elif proxy.is_symbolic(symbolic):
            return symbolic.concretize(model)
        elif isinstance(symbolic, list):
            return [cls._concretize(x, model) for x in symbolic]
        elif isinstance(symbolic, tuple):
            return tuple([cls._concretize(x, model) for x in symbolic])
        elif proxy.is_user_defined(symbolic):
            # symbolic.__dict__ returns all instance-only defined attributes
            if symbolic.concretized:
                return symbolic
            symbolic.concretized = True
            try:
                for name in symbolic.__dict__:
                    # TODO: Hacerlo genérico, incluyendo atributos de clase
                    attr = getattr(symbolic, name)
                    if not callable(attr):
                        setattr(symbolic, name, cls._concretize(attr, model))
            except AttributeError:
                # TODO: Check wtf is this
                if isinstance(symbolic, Iterable):
                    pass
            return symbolic
        else:
            # i think this is executed when the symbolicect is a builtin or a
            # callable
            return symbolic

    @classmethod
    def _remove_explored_branches(cls):
        """Removes fully explored branhes.

        Advance the last branching point and removes it if it
        has been fully explored. After removing a branching point
        the same is done again until no more branches are removed
        or no more branches left.
        """
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
        """Implements a lazy initialization step.

        If it's a new initialization step creates the branching
        point an return None as first initialization, on the
        other hand if it's an already existent one it gets the
        corresponding initialization that could be:
            - None
            - Any previous created instances of lazy_class.
            - A new lazy_class instance.

        Args:
            lazy_class: The instance type to be initialized.
            vector: A vector containing the previous created 
                instances of lazy_class.

        Returns:
            An instance of lazy_class or None.
        """
        if cls._max_depth < cls._current_depth:
            raise MaxDepthException
        cls._current_depth += 1

        if cls._current_bp < len(cls._branching_points):
            branch_point = cls._branching_points[cls._current_bp]
            assert isinstance(branch_point, LazyStep)
            index = branch_point.get_branch()
            cls._current_bp += 1

            if index < len(vector):
                return vector[index]

            n = cls._symbolize_partially(lazy_class)
            vector.append(n)
            return n

        cls._branching_points.append(LazyStep(len(vector)))
        cls._current_bp += 1
        return None

    @classmethod
    def _symbolic_instantiation(cls, typ):
        """Creates a symbolic or a partially symbolic instance.

        If it's a supported builtin type it returns the appropiate
        symbolic instance.
        If it's an user-defined class returns a partially symbolic
        instance of that class

        Args:
            typ: The type to be instantiated. Could be builtin or
            user defined.

        Returns:
            A symbolic or partially symbolic instance.
        """
        if typ in cls._real_to_proxy.keys():
            return cls._real_to_proxy[typ]()
        elif isinstance(typ, type(None)):
            return None
        elif proxy.is_user_defined(typ):
            instance = cls._symbolize_partially(typ)
            typ._vector.append(instance)
            cls._lazy_backups[typ].add_entity(typ._vector)
            return instance
        return typ()

    @classmethod
    def _symbolize_partially(cls, user_def_class):
        """Creates partially symbolic instance of a class.

        Returns an instance of user_def_class with all it's builtin
        instance attributes symbolized and it's user-defined attributes
        initialized to None.

        Args:
            user_def_class: The class to be partially symbolized.

        Returns:
            A partially symbolic instance of user_def_class.
        """
        init_types = cls._get_init_types(user_def_class)
        init_args = [cls._make_symbolic(a) for a in init_types]
        if init_args:
            return user_def_class(*init_args)
        return user_def_class()

    @classmethod
    def _get_init_types(cls, user_def_class):
        """Returns the types of the parameters of the class.

        Returns a list containing the types of the parameters
        of the init method of user_def_class.

        Args:
            user_def_class: An user-defined class.

        Returns:
            A list of types.
        """
        init_types = copy.deepcopy(cls._sut.class_params_map[user_def_class])
        number_params = user_def_class.__init__.__code__.co_argcount
        if number_params - 1 != len(init_types):
            raise MissingTypesError(
                "Incomplete type annotations in: " + str(user_def_class)
            )
        return init_types

    @classmethod
    def _make_symbolic(cls, typ):
        """Creates a symbolic instance.

        If it's a supported builtin type it returns the appropiate
        symbolic instance.
        If it's an user-defined class returns None

        Args:
            typ: The type to be instantiated. Could be builtin or
            user defined.

        Returns:
            A symbolic instance of a builtin type or None.
        """
        if typ in cls._real_to_proxy.keys():
            return cls._real_to_proxy[typ]()
        elif isinstance(typ, type(None)) or proxy.is_user_defined(typ):
            return None
        return typ()

    @classmethod
    def evaluate(cls, sym_bool):
        """Evaluates a condition represented by a symbolic bool.

        If the value of the symbol represented constraint is conditioned
        to True or False by the path conditions, that value is returned
        and no branching point is created. Otherwise (both values are
        feasible) return the corresponding bool evaluation of the current
        branching point.

        Args:
            sym_bool: the symbolic bool that represents a constraint.

        Returns:
            True or False, depending on the evaluation.
        """
        bool_value = cls.conditioned_value(sym_bool)
        if bool_value is not None:
            return bool_value

        condition = sym_bool.formula
        condition_value = cls._get_next_conditional_step()

        if condition_value:
            cls._path_condition.append(condition)
        else:
            cls._path_condition.append(proxy.smt.Not(condition))

        # TODO: Check if next lines are necessary
        if not condition_value:
            sym_bool.formula = proxy.smt.Not(sym_bool.formula)
        return condition_value

    @classmethod
    def conditioned_value(cls, sym_bool):
        """Checks if a constraint's value is conditioned by the path.

        Checks whether the constraint represented by sym_bool has a
        determined value conditioned by the path_condition.

        Args:
            sym_bool: the symbolic bool that represents a constraint.

        Returns:
            True or False if the value it's conditioned by the path_condition,
            None otherwise.

        Raises:
            UnstatBranchError: Unsat constraint Error.
        """
        conditions = True
        for c in cls._path_condition:
            conditions = proxy.smt.And(conditions, c)
        true_cond = proxy.smt.check(proxy.smt.And(conditions, sym_bool.formula))
        false_cond = proxy.smt.check(
            proxy.smt.And(conditions, proxy.smt.Not(sym_bool.formula))
        )
        if true_cond and not false_cond:
            return True
        if false_cond and not true_cond:
            return False
        if not true_cond and not false_cond:
            raise UnsatBranchError()

    @classmethod
    def _get_next_conditional_step(cls):
        """Retrieves the conditional of the current branching point.

        Looks and returns the value that must take the current branching
        point (conditional branching point).

        Returns:
            True or False Depending on the current branching point value.
        """
        if cls._max_depth < cls._current_depth:
            raise MaxDepthException
        cls._current_depth += 1

        if cls._current_bp < len(cls._branching_points):
            assert isinstance(cls._branching_points[cls._current_bp], ConditionalStep)
            bool_value = cls._branching_points[cls._current_bp].get_branch()
        else:
            cls._branching_points.append(ConditionalStep())
            bool_value = True

        cls._current_bp += 1
        return bool_value

    @classmethod
    def ignore_if(cls, value, instance):
        """Ignores this execution path if value is true.

        Value deepends on instance repok, if repok is violated,
        value will be True and an exception is raised.

        Raises:
            RepOkFailException: RepOk of instances failed.
        """
        if value:
            raise RepOkFailException()

    @classmethod
    def statistics(cls):
        """Returns the collected statistics of all executions.
        """
        return cls._globalstats

    @classmethod
    def save_lazy_step(cls, sclass, vector):
        cls._lazy_backups[sclass].new_backup(vector)

class LazyBackup:
    def __init__(self, vector=[None], amount_entities=0):
        self.vector = copy.deepcopy(vector)
        self.amount_entities = amount_entities
        self.next_entity = 1
    
    def add_entity(self, vector):
        self.vector = copy.deepcopy(vector)
        self.amount_entities += 1

    def new_backup(self, vector):
        self.vector = copy.deepcopy(vector)

    def get_entity(self):
        entity = self.vector[self.next_entity]
        self.next_entity += 1
        return entity

