"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynammically allocated structures with the use of lazy initialization.

"""

import copy
import time

import exceptions as excp
import instances as inst
import instance_managment as im
import helpers
import symbolics as sym

from branching_steps import LazyBranchPoint, ConditionalBranchPoint
from data import Status, PathExecutionData, ExplorationStats, Mode
from smt.smt import SMT
from smt.sort_z3 import SMTInt, SMTBool
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

        _current_bp (int): Is the current branching point, it could
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

    def __init__(self, sut_data, max_depth, max_nodes, max_r_nodes, timeout=20.0):
        """Setups the initial values of the engine.

        Args:
            sut_data: System under test (function, types, classes).
            max_depth: Depth limit of the exploration tree.
        """
        self.smt = SMT((SMTInt, SMTBool), SMTSolver)
        self._sut = sut_data
        self._max_depth = max_depth
        self._stats = ExplorationStats()
        self._backups = LazyBackup()
        self.mode = Mode.NOMODE
        self.prev_mode = Mode.NOMODE
        self._current_depth = 0
        self._current_bp = 0
        self._recursion_limit = 0
        self._branch_points = []
        self._path_condition = []
        self._current_self = None
        self._max_nodes = max_nodes
        self._current_nodes = 0
        self._max_r_nodes = max_r_nodes
        self._current_repok_max = 0
        self._max_time = timeout
        self._timeout = 0
        self._time = 0

        for k in self._sut.class_map.keys():
            setattr(k, "_engine", self)
            setattr(k, "_vector", [])
            setattr(k, "_id", 0)

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
        assert not self._branch_points
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration()

            args = self.instantiate_input()

            result = self._execute_method_exploration(args)

            self.set_mode(Mode.CONCRETE_EXECUTION)
            yield (result)

            self._remove_explored_branch()

            if not self._branch_points:
                unexplored_paths = False

    def instantiate_input(self):
        types = self._sut.get_method_param_types()
        args = [inst.symbolic_instantiation(self, typ) for typ in types]
        self._backups.initialize_backup(args)
        return args

    def _reset_exploration(self):
        """Resets the exploration variables to it's initial values.
        """
        self._path_condition = []
        self._current_bp = 0
        self._current_nodes = 0
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
        print("\n\nExecuting method:")

        returnv = None
        exception = None
        status = Status.PRUNED

        self._current_self = args[0]
        args = args[1:]
        method = getattr(self._current_self, self._sut.get_method_name())
        self.set_mode(Mode.METHOD_EXPLORATION)
        self._timeout = time.time() + self._max_time
        self._time = time.time()
        try:
            if args:
                returnv = method(*args)
            else:
                returnv = method()
            if sym.is_symbolic_bool(returnv):
                returnv = returnv.__bool__()
        except excp.UnsatBranchError:
            self._stats.pruned_by_error += 1
        except excp.MaxDepthException:
            self._stats.pruned_by_depth += 1
        except excp.RepOkFailException:
            self._stats.pruned_by_repok += 1
        except excp.MaxRecursionException:
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
                pathdata = PathExecutionData(exec_num, status, exception)
                pathdata.time = time.time() - self._time
                return pathdata
                # model = self.smt.get_model(self._path_condition)
                # pruned_sym = self._backups.get_self()
                # pruned = concretize(pruned_sym, model)

                # run_data.pathcondition = self._path_condition
                # run_data.symbolic_inself = pruned_sym
                # return run_data

            pathdata = self.build_stats(status, args, returnv)
            self._stats.status_count(pathdata.status)
            pathdata.time = time.time() - self._time
            return pathdata

    def build_stats(self, status, args, returnv):
        # Path condition and model
        path = self._path_condition
        model = self.smt.get_model(path)

        # Input Self
        symbolic_inself = self._backups.get_self()
        symbolic_args = self._backups.get_args()

        input_self = self.build(symbolic_inself, model)
        self._stats.builded_count(input_self, self._current_repok_max)

        if input_self is None:
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
        except excp.TimeOutException as e:
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
        except excp.TimeOutException as e:
            raise e
        finally:
            self.restore_prev_mode()
            return result

    def _reset_for_repok(self, iself, pc_len):
        self._path_condition = helpers.keep_first_n(self._path_condition, pc_len)
        self._backups = LazyBackup()
        self._current_bp = 0
        self._current_depth = 0
        self._current_nodes = 0
        for k in self._sut.class_map.keys():
            k._vector = []
        inst.fill_class_vectors(iself)

    def build(self, symbolic, model):
        if symbolic is None:
            return None
        elif sym.is_symbolic(symbolic):
            return symbolic.concretize(model)
        elif isinstance(symbolic, list):
            for i, x in enumerate(symbolic):
                symbolic[i] = self.build(x, model)
                if x is not None and symbolic[i] is None:
                    assert False
            return symbolic
        elif im.is_user_defined(symbolic):
            self._recursion_limit = 200
            concretei = inst.concretize(symbolic, model)
            if self.execute_repok_concretely(concretei):
                return concretei

            self._current_repok_max = 0
            build = None
            while not build and self._current_repok_max <= self._max_r_nodes:
                print("Building for ", self._current_repok_max)
                build = self.build_partial_struture(symbolic, model)
                self._current_repok_max += 1
            return build
        assert False

    def node_limit(self):
        if self.mode == Mode.METHOD_EXPLORATION:
            if self._current_nodes >= self._max_nodes:
                return True
        elif self.mode == Mode.REPOK_EXPLORATION:
            if self._current_nodes >= self._current_repok_max:
                return True
        else:
            assert False

    def build_partial_struture(self, input_self, model):
        backup_bp = copy.deepcopy(self._branch_points)
        self._branch_points = []
        pc_len = len(self._path_condition)

        unexplored_paths = True

        while unexplored_paths:
            iself = copy.deepcopy(input_self)
            self._reset_for_repok(iself, pc_len)

            result = self._execute_repok_exploration(iself)

            if result is not None:
                self._path_condition = helpers.keep_first_n(self._path_condition, pc_len)
                self._branch_points = backup_bp
                return result

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

        self._path_condition = helpers.keep_first_n(self._path_condition, pc_len)
        self._branch_points = backup_bp

    def _execute_repok_exploration(self, instance):
        self._current_self = instance
        self.set_mode(Mode.REPOK_EXPLORATION)
        try:
            result = instance.repok()
            if sym.is_symbolic_bool(result):
                result = result.__bool__()
        except excp.UnsatBranchError:
            pass
        except excp.MaxDepthException:
            pass
        except excp.TimeOutException as e:
            raise e
        except excp.MaxRecursionException:
            assert False
            raise excp.MaxRecursionException("Max recursion reached on repok")
        except AttributeError as e:
            print("attr error")
            raise e
        else:
            if result:
                model = self.smt.get_model(self._path_condition)
                new_object = inst.concretize(instance, model)
                return new_object
            return None
        finally:
            self.restore_prev_mode()

    def _remove_explored_branch(self):
        """Removes fully explored branhes.

        Advance the last branching point and removes it if it
        has been fully explored. After removing a branching point
        the same is done again until no more branches are removed
        or no more branches left.
        """
        if not self._branch_points:
            return None

        last_bp = self._branch_points[-1]
        last_bp.advance_branch()

        while self._branch_points and last_bp.all_branches_covered():
            del self._branch_points[-1]
            if self._branch_points:
                last_bp = self._branch_points[-1]
                last_bp.advance_branch()

    def check_conservative_repok(self, obj):
        self.set_mode(Mode.CONSERVATIVE_EXECUTION)
        try:
            if hasattr(obj, "repok") and not obj.repok():
                raise excp.RepOkFailException()
            if not im.is_same(obj, self._current_self):
                if not self._current_self.repok():
                    raise excp.RepOkFailException()
        except excp.NoInitializedException:
            pass
        except excp.CantMakeDecisionException:
            pass
        except excp.RepOkFailException as e:
            raise e
        except AttributeError as e:
            raise e
        finally:
            self.restore_prev_mode()

    def check_timeout(self):
        if time.time() > self._timeout:
            raise excp.TimeOutException()

    def lazy_initialization(self, obj, attr_name):
        attr = im.get_attr(obj, attr_name)
        is_init = im.is_initialized(obj, attr_name)

        if self.mode == Mode.CONCRETE_EXECUTION:
            return attr
        if self.mode == Mode.CONSERVATIVE_EXECUTION:
            if not is_init:
                raise excp.NoInitializedException()
            return attr

        # Mode is METHOD_EXPLORATION OR REPOK_EXPLORATION
        attr_type = self._sut.get_attr_type(type(obj), attr_name)

        if im.is_user_defined(attr_type):
            if is_init or not im.is_tracked(obj):
                self.check_recursion_limit(attr)
                return attr

            im.set_to_initialized(obj, attr_name)
            if attr is None:
                new_value = self.get_next_lazy_step(attr_type)
                im.set_attr(obj, attr_name, new_value)
                setattr(obj, "_recursion_depth", 0)

                if self.mode == Mode.METHOD_EXPLORATION:
                    if self._current_bp - 1 < len(self._branch_points):
                        self.check_conservative_repok(obj)
                    self.mimic_change(obj, attr_name, new_value)

        else:
            assert sym.Symbolic.is_supported_builtin(attr_type)
            assert attr is not None
            if not is_init:
                im.set_to_initialized(obj, attr_name)
                if not sym.is_symbolic(attr):
                    new_sym = sym.symbolic_factory(self, attr_type)
                    im.set_attr(obj, attr_name, new_sym)

        return im.get_attr(obj, attr_name)

    def lazy_set_attr(self, obj, attr_name, value):
        assert self.mode != Mode.CONSERVATIVE_EXECUTION
        im.set_to_initialized(obj, attr_name)
        im.set_attr(obj, attr_name, value)

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
        assert self.mode != Mode.CONSERVATIVE_EXECUTION
        assert self.mode != Mode.CONCRETE_EXECUTION

        if self._current_bp < len(self._branch_points):
            branch_point = self._branch_points[self._current_bp]
            assert isinstance(branch_point, LazyBranchPoint)
            index = branch_point.get_branch()
            self._current_bp += 1

            if index == 0:
                self._current_nodes += 1
                n = inst.symbolize_partially(self, lazy_class)
                lazy_class._vector.append(n)
                return n
            elif index == 1:
                return None
            else:
                assert index - 2 >= 0
                assert index - 2 < len(lazy_class._vector)
                return lazy_class._vector[index - 2]

        new_bp = LazyBranchPoint(len(lazy_class._vector) + 1)
        self._branch_points.append(new_bp)
        self._current_bp += 1
        if self.node_limit():
            new_bp.advance_branch()
            return None
        self._current_nodes += 1
        n = inst.symbolize_partially(self, lazy_class)
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
            raise excp.NoInitializedException()

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
            raise excp.UnsatBranchError()

    def _get_next_conditional_step(self):
        """Retrieves the conditional of the current branching point.

        Looks and returns the value that must take the current branching
        point (conditional branching point).

        Returns:
            True or False Depending on the current branching point value.
        """
        if self._max_depth < self._current_depth:
            raise excp.MaxDepthException
        self._current_depth += 1

        if self._current_bp < len(self._branch_points):
            bool_value = self._branch_points[self._current_bp].get_branch()
        else:
            self._branch_points.append(ConditionalBranchPoint())
            bool_value = True

        self._current_bp += 1
        return bool_value

    def check_recursion_limit(self, obj):
        if hasattr(obj, "_recursion_depth"):
            obj._recursion_depth += 1
            if obj._recursion_depth > self._recursion_limit:
                raise excp.MaxRecursionException(str(obj._recursion_depth))

    def statistics(self):
        """Returns the collected statistics of all executions.
        """
        return self._stats

    def mimic_change(self, obj, attr_name, new_value):
        obj_backup = self._backups.get_backup_of(obj)
        if obj_backup is None:
            assert False

        if self._branch_points[self._current_bp - 1].get_branch() > 1:
            new_val = self._backups.get_backup_of(new_value)
            if new_val is None:
                assert False
            im.set_attr(obj_backup, attr_name, new_val)
        else:
            im.set_attr(obj_backup, attr_name, copy.deepcopy(new_value))


class LazyBackup:
    def __init__(self):
        self.args_bkp = []
        self.self_bkp = None

    def init_self_backup(self, self_obj):
        self.self_bkp = copy.deepcopy(self_obj)

    def initialize_backup(self, datalist):
        self.self_bkp = copy.deepcopy(datalist[0])
        self.args_bkp = copy.deepcopy(datalist[1:])

    def get_self(self):
        return copy.deepcopy(self.self_bkp)

    def get_args(self):
        return copy.deepcopy(self.args_bkp)

    def get_backup_of(self, obj):
        obj_backup = inst.search_obj(obj, self.self_bkp)
        if obj_backup is None:
            for arg in self.args_bkp:
                if im.is_user_defined(arg):
                    obj_backup = inst.search_obj(obj, arg)
                    if obj_backup is not None:
                        break
        return obj_backup
