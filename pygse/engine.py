"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynammically allocated structures with the use of lazy initialization.

"""

import copy

from branching_steps import LazyStep, ConditionalStep
from data import Status, PathExecutionData, ExplorationStats, Mode
from exceptions import UnsatBranchError, NoInitializedException
from exceptions import RepOkFailException, MaxRecursionException
from exceptions import MaxDepthException, CantMakeDecisionException
from exceptions import TimeOutException
from helpers import do_add, is_user_defined, keep_first_n_items
from helpers import set_to_initialized, get_initialized_name, add_prefix
from symbolics import Symbolic, SymBool, SymInt, is_symbolic, is_symbolic_bool

from smt.smt import SMT
from smt.sort_z3 import SMTInt, SMTBool, SMTChar, SMTArray
from smt.solver_z3 import SMTSolver


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

        _path_condition (list): Collects all the path constraints of the current
        execution.

        _current_bp (LazyStep, ConditionalStep): Is the current branching point, it could
        be a Lazy Initialization Stem or a Conditional Step.

        _current_depth (int): Depth's of the current execution tree.

        _max_depth (int): Max depth search, any execution that exeeds this value
        is pruned.

        _globalstats (ExplorationStats): Contains the overall statistics of all executed
        program paths.

        _sut (SUT): Data of the program under test, contains the method or function,
        parameter types, etc.

        _real_to_proxy (dict): Maps builtin supported types to Symbolic Ones.
    """

    def __init__(self, sut_data, max_depth):
        """Setups the initial values of the engine.

        Args:
            sut_data: System under test (function, types, classes).
            max_depth: Depth limit of the exploration tree.
        """
        self.smt = SMT((SMTInt, SMTBool, SMTChar, SMTArray), SMTSolver)
        self._sut = sut_data
        self._real_to_proxy = Symbolic.get_symtypes_mapping()
        self._max_depth = max_depth
        self._stats = ExplorationStats()
        self._backups = LazyBackup()
        self.mode = Mode.NOMODE
        self.prev_mode = Mode.NOMODE
        self._current_depth = 0
        self._current_bp = 0
        self._recursion_limit = 0
        self._branching_points = []
        self._path_condition = []
        self._current_self = None

        for k in self._sut.class_map.keys():
            setattr(k, "_engine", self)
            setattr(k, "_vector", [])
            setattr(k, "_id", 0)

    def sym_int(self, value=None):
        return SymInt(self, value)

    def sym_bool(self, formula=None):
        return SymBool(self, formula)

    def new_symbolic(self, typ):
        if isinstance(typ, SymInt):
            return self.sym_int()
        elif isinstance(typ, SymBool):
            return self.sym_bool()
        assert False

    def set_mode(self, mode):
        self.prev_mode = self.mode
        self.mode = mode

    def restore_prev_mode(self):
        self.mode = self.prev_mode

    def explore(self):
        """Main method, implements the generalized symbolic execution.

        Yields:
            PathExecutionData: The result of the execution of the function under test
        """
        self._branching_points = []
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration()

            args = self.instantiate_method_params()
            self._backups.initialize_backup(args)

            result = self._execute_method_exploration(args)
            self.set_mode(Mode.CONCRETE_EXECUTION)
            yield (result)

            self._remove_explored_branches()

            if not self._branching_points:
                unexplored_paths = False

    def instantiate_method_params(self):
        types = self._sut.get_method_types()
        return [self._symbolic_instantiation(typ) for typ in types]

    def _symbolic_instantiation(self, typ):
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
        if typ in self._real_to_proxy.keys():
            return self._real_to_proxy[typ](self)
        elif isinstance(typ, type(None)):
            return None
        elif is_user_defined(typ):
            instance = self._symbolize_partially(typ)
            typ._vector.append(instance)
            return instance
        return typ()

    def _symbolize_partially(self, user_def_class):
        """Creates partially symbolic instance of a class.

        Returns an instance of user_def_class with all it's builtin
        instance attributes symbolized and it's user-defined attributes
        initialized to None.

        Args:
            user_def_class: The class to be partially symbolized.

        Returns:
            A partially symbolic instance of user_def_class.
        """
        init_types = self._get_init_types(user_def_class)[1:]
        init_args = [self._make_symbolic(a) for a in init_types]
        if init_args:
            partial_ins = user_def_class(*init_args)
        else:
            partial_ins = user_def_class()
        # Instrumentation
        # adding initialized fields
        for attr_name in self._sut.get_instance_attr_dict(user_def_class).keys():
            setattr(partial_ins, get_initialized_name(attr_name), False)

        setattr(partial_ins, "_objid", user_def_class._id)
        user_def_class._id += 1
        return partial_ins

    def _get_init_types(self, user_def_class):
        """Returns the types of the parameters of the class.

        Returns a list containing the types of the parameters
        of the init method of user_def_class.

        Args:
            user_def_class: An user-defined class.

        Returns:
            A list of types.
        """
        return self._sut.get_cls_init_types(user_def_class)

    def _make_symbolic(self, typ):
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
        if typ in self._real_to_proxy.keys():
            return self._real_to_proxy[typ](self)
        elif isinstance(typ, type(None)) or is_user_defined(typ):
            return None
        return typ()

    def _reset_exploration(self):
        """Resets the exploration variables to it's initial values.
        """
        self._path_condition = []
        self._current_bp = 0
        self._current_depth = 0
        self._recursion_limit = 20
        self._backups = LazyBackup()
        for k in self._sut.class_map.keys():
            k._vector = []
            k._id = 0

    def _execute_method_exploration(self, args):
        """Executes the method and returns the result.

        Collect and returns all the execution data, like the returned
        value, the final state of the self, the path condition, the
        model, exceptions raised, concrete values of arguments and
        result, and state.

        Args:
            args (List): List of the arguments to call the function
                or method.

        Returns:
            PathExecutionData: The result of the execution of the function
            under test
        """
        self._stats.total_paths += 1

        returnv = None
        exception = None
        status = Status.PRUNED

        self._current_self = args[0]
        args = args[1:]
        method = getattr(self._current_self, self._sut.get_method_name())
        self.set_mode(Mode.METHOD_EXPLORATION)
        try:
            if args:
                returnv = method(*args)
            else:
                returnv = method()
            if is_symbolic_bool(returnv):
                returnv = returnv.__bool__()
        except UnsatBranchError:
            self._stats.pruned_by_error += 1
        except MaxDepthException:
            self._stats.pruned_by_depth += 1
        except RepOkFailException:
            self._stats.pruned_by_repok += 1
        except MaxRecursionException:
            self._stats.pruned_by_rec_limit += 1
        except Exception as e:
            self._stats.pruned_by_exception += 1
            exception = e
        else:
            status = Status.OK
        finally:
            self.set_mode(Mode.CONCRETE_EXECUTION)
            # if exception:
            #     raise exception
            if status == Status.PRUNED:
                exec_num = self._stats.total_paths
                model = self.smt.get_model(self._path_condition)
                pruned_sym = self._backups.get_self()
                pruned = self.concretize(pruned_sym, model)
                run_data = PathExecutionData(exec_num, status, exception, pruned)
                run_data.pathcondition = self._path_condition
                run_data.symbolic_inself = pruned_sym
                return run_data

            stats = self.build_stats(status, args, returnv)
            self._stats.status_count(stats.status)
            return stats

    def build_stats(self, status, args, returnv):
        # Path condition and model
        path = self._path_condition
        model = self.smt.get_model(path)

        # Input Self
        symbolic_inself = self._backups.get_self()
        symbolic_args = self._backups.get_args()

        input_self = self.build(symbolic_inself, model)
        if input_self is None:
            self._stats.pruned_invalid += 1
            return PathExecutionData(self._stats.total_paths, Status.PRUNED)

        input_args = self.build(symbolic_args, model)

        # Execution of method with concrete input
        self_end_state = copy.deepcopy(input_self)
        args = copy.deepcopy(input_args)

        returnv = self.execute_method_concretely(self_end_state, args)

        if self.execute_repok_concretely(self_end_state):
            status = Status.OK
        else:
            status = Status.FAIL

        pathdata = PathExecutionData(self._stats.total_paths, status)
        pathdata.input_args = input_args
        pathdata.pathcondition = path
        pathdata.model = model
        pathdata.self_end_state = self_end_state
        pathdata.input_self = input_self
        pathdata.symbolic_inself = symbolic_inself
        pathdata.returnv = returnv
        return pathdata

    def execute_method_concretely(self, obj, args):
        self.set_mode(Mode.CONCRETE_EXECUTION)
        try:
            method = getattr(obj, self._sut.get_method_name())
            if args:
                returnv = method(*args)
            else:
                returnv = method()
        except AttributeError as e:
            raise e
        except TimeOutException as e:
            raise e
        finally:
            self.restore_prev_mode()
            return returnv

    def execute_repok_concretely(self, obj):
        self.set_mode(Mode.CONCRETE_EXECUTION)
        try:
            result = obj.repok()
        except AttributeError as e:
            raise e
        except TimeOutException as e:
            raise e
        finally:
            self.restore_prev_mode()
            return result

    def _reset_for_repok(self, iself, pc_len):
        self._path_condition = keep_first_n_items(self._path_condition, pc_len)
        self._backups = LazyBackup()
        self._backups.init_self_backup(iself)
        self._current_bp = 0
        self._current_depth = 0
        self._recursion_limit = 200
        for k in self._sut.class_map.keys():
            k._vector = []
        self.fill_class_vectors(iself)

    def build(self, symbolic, model):
        if symbolic is None:
            return None
        elif is_symbolic(symbolic):
            return symbolic.concretize(model)
        elif isinstance(symbolic, list):
            for i, x in enumerate(symbolic):
                symbolic[i] = self.build(x, model)
                if x is not None and symbolic[i] is None:
                    assert False
            return symbolic
        elif is_user_defined(symbolic):
            return self.build_partial_struture(symbolic, model)
        assert False

    def build_partial_struture(self, input_self, model):
        self._recursion_limit = 200
        concretei = self.concretize(input_self, model)
        if self.execute_repok_concretely(concretei):
            return concretei

        backup_bp = copy.deepcopy(self._branching_points)
        self._branching_points = []
        pc_len = len(self._path_condition)

        unexplored_paths = True

        # just for debug purposes
        useless = 0

        while unexplored_paths:
            useless += 1
            iself = copy.deepcopy(input_self)
            self._reset_for_repok(iself, pc_len)

            result = self._execute_repok_exploration(iself)

            if result is not None:
                self._path_condition = keep_first_n_items(self._path_condition, pc_len)
                self._branching_points = backup_bp
                return result

            self._remove_explored_branches()
            if not self._branching_points:
                unexplored_paths = False

        self._path_condition = keep_first_n_items(self._path_condition, pc_len)
        self._branching_points = backup_bp

    @staticmethod
    def fill_class_vectors(structure):
        if not is_user_defined(structure):
            return
        visited = set()
        visited.add(structure)
        worklist = []
        worklist.append(structure)
        while worklist:
            current = worklist.pop(0)
            setattr(current, "_recursion_depth", 0)
            if not hasattr(current, "_objid"):
                setattr(current, "_objid", type(current)._id)
                type(current)._id += 1
            current._vector.append(current)
            for name in current.__dict__:
                attr = None
                if hasattr(current, name):
                    attr = getattr(current, name)
                if is_user_defined(attr) and do_add(visited, attr):
                    worklist.append(attr)

    def _execute_repok_exploration(self, instance):
        self._current_self = instance
        self.set_mode(Mode.REPOK_EXPLORATION)
        try:
            result = instance.repok()
            if is_symbolic_bool(result):
                result = result.__bool__()
        except UnsatBranchError:
            pass
        except MaxDepthException:
            pass
        except RepOkFailException:
            pass
        except TimeOutException as e:
            raise e
        except MaxRecursionException:
            assert False
            raise MaxRecursionException("Max recursion reached on repok")
        except AttributeError as e:
            raise e
        else:
            if result:
                model = self.smt.get_model(self._path_condition)
                new_object = self.concretize(instance, model)
                return new_object
            return None
        finally:
            self.restore_prev_mode()

    def _remove_explored_branches(self):
        """Removes fully explored branhes.

        Advance the last branching point and removes it if it
        has been fully explored. After removing a branching point
        the same is done again until no more branches are removed
        or no more branches left.
        """
        if not self._branching_points:
            return None

        last_bp = self._branching_points[-1]
        last_bp.advance_branch()

        while self._branching_points and last_bp.all_branches_covered():
            del self._branching_points[-1]
            if self._branching_points:
                last_bp = self._branching_points[-1]
                last_bp.advance_branch()

    def check_conservative_repok(self, obj):
        self.set_mode(Mode.CONSERVATIVE_EXECUTION)
        try:
            if hasattr(obj, "repok") and not obj.repok():
                raise RepOkFailException()
            if (
                obj._objid != self._current_self._objid or
                not isinstance(obj, type(self._current_self))
            ):
                if not self._current_self.repok():
                    raise RepOkFailException()
        except NoInitializedException:
            pass
        except CantMakeDecisionException:
            pass
        except RepOkFailException as e:
            raise e
        except AttributeError as e:
            raise e
        finally:
            self.restore_prev_mode()

    def lazy_initialization(self, obj, attr_name):
        assert obj is not None
        pref_name = add_prefix(attr_name)
        isinit_name = get_initialized_name(attr_name)
        assert hasattr(obj, pref_name)

        if hasattr(obj, isinit_name):
            is_init = getattr(obj, isinit_name)
        else:
            setattr(obj, isinit_name, False)
            is_init = False

        attr = getattr(obj, pref_name)

        if self.mode == Mode.CONCRETE_EXECUTION:
            return attr
        if self.mode == Mode.CONSERVATIVE_EXECUTION:
            if not is_init:
                raise NoInitializedException()
            self.check_recursion_limit(attr)
            return attr

        attr_type = self._sut.get_attr_type(type(obj), attr_name)

        if is_user_defined(attr_type):
            if is_init or not self.is_tracked(obj):
                self.check_recursion_limit(attr)
                return attr

            setattr(obj, isinit_name, True)
            if attr is None:
                new_value = self.get_next_lazy_step(attr_type)
                setattr(obj, pref_name, new_value)
                self._backups.make_backup()

                if self.mode == Mode.METHOD_EXPLORATION:
                    setattr(obj, "_recursion_depth", 0)
                    self.check_conservative_repok(obj)

        else:
            assert Symbolic.is_supported_builtin(attr_type)
            assert attr is not None
            if not is_init:
                setattr(obj, isinit_name, True)
                if not is_symbolic(attr):
                    new_sym = self.new_symbolic(attr_type)
                    setattr(obj, pref_name, new_sym)

        return getattr(obj, pref_name)

    def lazy_set_attr(self, obj, attr_name, value):
        assert self.mode != Mode.CONSERVATIVE_EXECUTION
        set_to_initialized(obj, attr_name)
        setattr(obj, add_prefix(attr_name), value)

    def get_next_lazy_step(self, lazy_class):
        """Implements a lazy initialization step.

        If it's a new initialization step creates the branching
        point an return None as first initialization, on the
        other hand if it's an already existent one it gets the
        corresponding initialization that could be:
            - None
            - Any previous created instances of lazy_class.
            - A new lazy_class instance.

        Args:
            lazy_class: Type of the instance to be created.
            vector: A vector containing the previous created
                instances of lazy_class.

        Returns:
            An instance of lazy_class or None.
        """
        if self._max_depth < self._current_depth:
            raise MaxDepthException
        self._current_depth += 1

        if self._current_bp < len(self._branching_points):
            branch_point = self._branching_points[self._current_bp]
            assert isinstance(branch_point, LazyStep)
            index = branch_point.get_branch()
            self._current_bp += 1

            if index == 0:
                n = self._symbolize_partially(lazy_class)
                lazy_class._vector.append(n)
                return n
            elif index == 1:
                return None
            else:
                assert index - 2 >= 0
                assert index - 2 < len(lazy_class._vector)
                return lazy_class._vector[index - 2]

        self._branching_points.append(LazyStep(len(lazy_class._vector) + 1))
        self._current_bp += 1
        n = self._symbolize_partially(lazy_class)
        lazy_class._vector.append(n)
        return n

    def evaluate(self, sym_bool):
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
        assert self.mode != Mode.CONCRETE_EXECUTION
        bool_value = self.conditioned_value(sym_bool)
        if bool_value is not None:
            return bool_value

        if self.mode == Mode.CONSERVATIVE_EXECUTION:
            raise NoInitializedException()

        condition = sym_bool.formula
        condition_value = self._get_next_conditional_step()

        if condition_value:
            self._path_condition.append(condition)
        else:
            self._path_condition.append(self.smt.Not(condition))
        return condition_value

    def conditioned_value(self, sym_bool):
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
        for c in self._path_condition:
            conditions = self.smt.And(conditions, c)
        true_cond = self.smt.check(self.smt.And(conditions, sym_bool.formula))
        false_cond = self.smt.check(
            self.smt.And(conditions, self.smt.Not(sym_bool.formula))
        )
        if true_cond and not false_cond:
            return True
        if false_cond and not true_cond:
            return False
        if not true_cond and not false_cond:
            raise UnsatBranchError()

    def _get_next_conditional_step(self):
        """Retrieves the conditional of the current branching point.

        Looks and returns the value that must take the current branching
        point (conditional branching point).

        Returns:
            True or False Depending on the current branching point value.
        """
        if self._max_depth < self._current_depth:
            raise MaxDepthException
        self._current_depth += 1

        if self._current_bp < len(self._branching_points):
            assert isinstance(self._branching_points[self._current_bp], ConditionalStep)
            bool_value = self._branching_points[self._current_bp].get_branch()
        else:
            self._branching_points.append(ConditionalStep())
            bool_value = True

        self._current_bp += 1
        return bool_value

    def check_recursion_limit(self, obj):
        if obj is not None and is_user_defined(obj):
            # see this
            if not hasattr(obj, "_recursion_depth"):
                setattr(obj, "_recursion_depth", 1)
            else:
                obj._recursion_depth += 1
                if obj._recursion_depth > self._recursion_limit:
                    raise MaxRecursionException(str(obj._recursion_depth))

    @staticmethod
    def is_tracked(obj):
        if not hasattr(obj, "_objid"):
            setattr(obj, "_objid", type(obj)._id)
            type(obj)._id += 1
            return False
        obj = next((x for x in obj._vector if x._objid == obj._objid), None)
        return obj is not None

    def statistics(self):
        """Returns the collected statistics of all executions.
        """
        return self._stats

    def concretize(self, symbolic, model):
        self.set_mode(Mode.CONCRETE_EXECUTION)
        visited = set()
        sym_copy = copy.deepcopy(symbolic)
        if is_user_defined(sym_copy):
            visited.add(sym_copy)
        conc = self._concretize(sym_copy, model, visited)
        self.restore_prev_mode()
        return conc

    def _concretize(self, symbolic, model, visited):
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
        elif is_symbolic(symbolic):
            return symbolic.concretize(model)
        elif isinstance(symbolic, list):
            for i, x in enumerate(symbolic):
                symbolic[i] = self._concretize(x, model, visited)
            return symbolic
        elif is_user_defined(symbolic):
            setattr(symbolic, "_recursion_depth", 0)
            for attr_name, value in symbolic.__dict__.items():
                set_to_initialized(symbolic, attr_name)
                attr = value
                if not callable(attr) and do_add(visited, attr):
                    setattr(symbolic, attr_name, self._concretize(attr, model, visited))
            return symbolic
        return symbolic


class LazyBackup:
    def __init__(self):
        self.self_id = ""
        self.args_bkp = []
        self.self_bkp = None

    def init_self_backup(self, instance):
        self.self_id = instance._objid
        self.self_bkp = copy.deepcopy(instance)

    def _add_argument(self, instance):
        bkp = copy.deepcopy(instance)
        if is_user_defined(instance):
            self.args_bkp.append((instance._objid, bkp))
        else:
            self.args_bkp.append(("", bkp))

    def init_args_backup(self, args_list):
        for arg in args_list:
            self._add_argument(arg)

    def initialize_backup(self, datalist):
        self.init_self_backup(datalist[0])
        self.init_args_backup(datalist[1:])

    def get_self(self):
        return copy.deepcopy(self.self_bkp)

    def get_args(self):
        return [x[1] for x in self.args_bkp]

    def make_backup(self):
        self.make_self_backup()
        self.make_args_backup()

    def make_args_backup(self):
        for (argid, bkp) in self.args_bkp:
            if is_user_defined(bkp):
                arg_bkp = next((x for x in bkp._vector if x._objid == argid), None)
                if arg_bkp is not None:
                    bkp = copy.deepcopy(arg_bkp)
                else:
                    assert False

    def make_self_backup(self):
        vector = self.self_bkp._vector
        self_bkp = next((x for x in vector if x._objid == self.self_id), None)
        if self_bkp is not None:
            self.self_bkp = copy.deepcopy(self_bkp)
        else:
            assert False
