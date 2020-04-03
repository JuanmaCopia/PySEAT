"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynammically allocated structures with the use of lazy initialization.

"""

import copy

from pygse.branching_steps import LazyStep, ConditionalStep
from pygse.stats import Status, ExecutionStats, GlobalStats
from pygse.engine_errors import UnsatBranchError, MissingTypesError
from pygse.engine_errors import RepOkFailException, MaxRecursionException
from pygse.engine_errors import MaxDepthException, RepokNotFoundError
from pygse.helpers import do_add, is_user_defined
from pygse.helpers import set_to_initialized
import pygse.proxy as proxy


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
    _recursion_limit = 0

    _globalstats = None
    _sut = None
    _real_to_proxy = {}

    _lazy_backups = {}

    _current_self = None

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
        cls._current_self = None

    @classmethod
    def explore(cls):
        """Main method, implements the generalized symbolic execution.

        Yields:
            ExecutionStats: The result of the execution of the function under test
        """
        cls._branching_points = []
        unexplored_paths = True

        while unexplored_paths:
            cls._reset_exploration()

            args = [cls._symbolic_instantiation(typ) for name, typ in cls._sut.params.items()]

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
        cls._recursion_limit = 10
        for k in cls._sut.class_params_map.keys():
            k._vector = []
            k._id = 0
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

        returnv = None
        exception = None
        status = Status.PRUNED

        cls._current_self = args[0]
        args = args[1:]
        method = getattr(cls._current_self, cls._sut.function.__name__)

        try:
            if args:
                returnv = method(*args)
            else:
                returnv = method()
            if proxy.is_symbolic_bool(returnv):
                returnv = returnv.__bool__()
        except UnsatBranchError:
            cls._globalstats.pruned_by_error += 1
        except MaxDepthException:
            cls._globalstats.pruned_by_depth += 1
        except RepOkFailException:
            cls._globalstats.pruned_by_repok += 1
        except MaxRecursionException:
            cls._globalstats.pruned_by_rec_limit += 1
        except RecursionError as e:
            status = Status.PRUNED
            exception = e
        except Exception as e:
            status = Status.PRUNED
            exception = e
        else:
            status = Status.OK
        finally:
            if status == Status.PRUNED:
                exec_num = cls._globalstats.total_paths
                return ExecutionStats(exec_num, status, exception)

            stats = cls.build_stats(status, args, returnv)
            cls._globalstats.status_count(stats.status)
            return stats

    @classmethod
    def build_stats(cls, status, args, returnv):
        # Path condition and model
        path = cls._path_condition
        model = proxy.smt.get_model(path)

        # Input Self
        input_self = cls._lazy_backups[cls._sut.sclass].get_entity()
        builded_in_self = cls.build_partial_struture(input_self, model)

        if builded_in_self is None:
            cls._globalstats.pruned_invalid += 1
            return ExecutionStats(cls._globalstats.total_paths, Status.PRUNED)

        # input arguments
        cls.retrieve_inputs(args)
        args = cls.concretize(args, model)

        # Execution of method with concrete input
        end_self = copy.deepcopy(builded_in_self)
        input_args = copy.deepcopy(args)
        method = getattr(end_self, cls._sut.function.__name__)
        if args:
            returnv = method(*input_args)
        else:
            returnv = method()

        if end_self.repok():
            status = Status.OK
        else:
            status = Status.FAIL

        stats = ExecutionStats(cls._globalstats.total_paths, status)
        stats.concrete_args = args
        stats.pathcondition = path
        stats.model = model
        stats.concrete_end_self = end_self
        stats.builded_in_self = builded_in_self
        stats.input_self = input_self
        stats.returnv = returnv
        stats.concrete_return = cls.concretize(returnv, model)
        return stats

    @classmethod
    def _reset_for_repok(cls, iself, pc_len):
        cls._path_condition = cls.keep_first_n_items(cls._path_condition, pc_len)
        cls._current_bp = 0
        cls._current_depth = 0
        cls._recursion_limit = 200
        for k in cls._sut.class_params_map.keys():
            k._vector = []
            cls._lazy_backups[k] = LazyBackup()
        cls.fill_class_vectors(iself)

    @classmethod
    def build_partial_struture(cls, input_self, model):
        concretei = cls.concretize(input_self, model)
        if concretei.repok():
            return concretei

        backup_bp = copy.deepcopy(cls._branching_points)
        cls._branching_points = []
        pc_len = len(cls._path_condition)

        unexplored_paths = True

        # just for debug purposes
        useless = 0

        while unexplored_paths:
            useless += 1
            iself = copy.deepcopy(input_self)
            cls._reset_for_repok(iself, pc_len)
            result = cls._execute_repok(iself)

            if result is not None and result.repok():
                cls._path_condition = cls.keep_first_n_items(cls._path_condition, pc_len)
                cls._branching_points = backup_bp
                return result

            cls._remove_explored_branches()
            if not cls._branching_points:
                unexplored_paths = False

        cls._path_condition = cls.keep_first_n_items(cls._path_condition, pc_len)
        cls._branching_points = backup_bp

    @classmethod
    def fill_class_vectors(cls, structure):
        if not is_user_defined(structure):
            return
        visited = set()
        visited.add(structure)
        worklist = []
        worklist.append(structure)
        while worklist:
            current = worklist.pop(0)
            setattr(current, "_recursion_depth", 0)
            current._vector.append(current)
            for name in current.__dict__:
                attr = None
                if hasattr(current, name):
                    attr = getattr(current, name)
                if is_user_defined(attr) and do_add(visited, attr):
                    worklist.append(attr)

    @staticmethod
    def keep_first_n_items(l, n):
        new_list = []
        i = 0
        while i < n:
            new_list.insert(i, l[i])
            i += 1
        return new_list

    @classmethod
    def _execute_repok(cls, instance):
        try:
            result = instance.instrumented_repok()
        except UnsatBranchError:
            pass
        except MaxDepthException:
            pass
        except RepOkFailException:
            pass
        except MaxRecursionException:
            raise MaxRecursionException("Max recursion reached on repok")
        except AttributeError as e:
            raise e
        else:
            if result:
                model = proxy.smt.get_model(cls._path_condition)
                new_object = cls.concretize(instance, model)
                assert new_object.repok()
                return new_object
            return None

    @classmethod
    def retrieve_inputs(cls, args_list):
        for i, arg in enumerate(args_list):
            if proxy.is_user_defined(arg):
                args_list[i] = cls._lazy_backups[type(arg)].get_entity()

    @classmethod
    def _check_repok(cls, instance):
        """Checks whether an instance pass it's class invariant o not.

        Args:
            instance: instance of a user_defined_class

        Returns:
            True if instance is valid (pass it's repok), False otherwise.
        """
        if proxy.is_user_defined(type(instance)):
            return instance.conservative_repok()
        return True

    @classmethod
    def concretize(cls, symbolic, model):
        visited = set()
        sym_copy = copy.deepcopy(symbolic)
        if is_user_defined(sym_copy):
            visited.add(sym_copy)
        return cls._concretize(sym_copy, model, visited)

    @classmethod
    def _concretize(cls, symbolic, model, visited):
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
        if symbolic is None:
            return None
        elif proxy.is_symbolic(symbolic):
            return symbolic.concretize(model)
        elif isinstance(symbolic, list):
            for i, x in enumerate(symbolic):
                symbolic[i] = cls._concretize(x, model, visited)
            return symbolic
        elif proxy.is_user_defined(symbolic):
            setattr(symbolic, "_recursion_depth", 0)
            for attr_name, value in symbolic.__dict__.items():
                set_to_initialized(symbolic, attr_name)
                attr = value
                if not callable(attr) and do_add(visited, attr):
                    setattr(symbolic, attr_name, cls._concretize(attr, model, visited))
            return symbolic
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

            if index == 0:
                n = cls._symbolize_partially(lazy_class)
                vector.append(n)
                return n
            elif index == 1:
                return None
            else:
                assert index - 2 >= 0
                assert index - 2 < len(vector)
                return vector[index - 2]

        cls._branching_points.append(LazyStep(len(vector) + 1))
        cls._current_bp += 1
        n = cls._symbolize_partially(lazy_class)
        vector.append(n)
        return n


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
            partial_ins = user_def_class(*init_args)
        else:
            partial_ins = user_def_class()
        return partial_ins

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
        init_types = list(cls._sut.class_params_map[user_def_class].values())
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
        repok_passed = cls._current_self.conservative_repok()
        if not repok_passed:
            raise RepOkFailException()
        return None

    @classmethod
    def check_recursion_limit(cls, obj):
        if obj is not None:
            obj._recursion_depth += 1
            if obj._recursion_depth > cls._recursion_limit:
                raise MaxRecursionException()


    @staticmethod
    def is_tracked(obj):
        return obj._identifier in [x._identifier for x in obj._vector if x is not None]

    @classmethod
    def statistics(cls):
        """Returns the collected statistics of all executions.
        """
        return cls._globalstats

    @classmethod
    def save_lazy_step(cls, sclass):
        cls._lazy_backups[sclass].new_backup(sclass._vector, cls._path_condition)
        if (sclass != cls._sut.sclass):
            cls._lazy_backups[cls._sut.sclass].new_backup(cls._sut.sclass._vector, cls._path_condition)


class LazyBackup:
    def __init__(self, vector=[], amount_entities=0):
        self.vector = copy.deepcopy(vector)
        self.path_condition = []
        self.amount_entities = amount_entities
        self.next_entity = 0

    def add_entity(self, vector):
        self.vector = copy.deepcopy(vector)
        self.amount_entities += 1

    def new_backup(self, vector, pc):
        self.vector = copy.deepcopy(vector)
        self.path_condition = copy.deepcopy(pc)

    def get_entity(self):
        entity = self.vector[self.next_entity]
        self.next_entity += 1
        return entity

    def get_vector(self):
        return self.vector
