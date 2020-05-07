"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynammically allocated structures with the use of lazy initialization.

"""

import copy
import time
import sys
import os
import signal

import exceptions as excp
import instances as inst
import instance_managment as im
import helpers
import symbolics as sym
import data

from branching_steps import LazyBranchPoint, ConditionalBranchPoint

from smt.smt import SMT
from smt.sort_z3 import SMTInt, SMTBool
from smt.solver_z3 import SMTSolver


# Engine modes of execution
CONSERVATIVE_EXECUTION = 0
METHOD_EXPLORATION = 1
REPOK_EXPLORATION = 2
CONCRETE_EXECUTION = 3

RECURSION_LIMIT = 30


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

    def __init__(self, sut_data, max_depth, max_nodes, max_r_nodes, m_timeout, b_timeout):
        """Setups the initial values of the engine.

        Args:
            sut_data: System under test (function, types, classes).
            max_depth: Depth limit of the exploration tree.
        """
        self.smt = SMT((SMTInt, SMTBool), SMTSolver)
        self._sut = sut_data
        self._max_depth = max_depth
        self._stats = data.ExplorationStats()
        self._backups = None
        self.mode = CONCRETE_EXECUTION
        self._current_depth = 0
        self._current_bp = 0
        self._branch_points = []
        self._path_condition = []
        self.curr_self = None
        self._max_nodes = max_nodes
        self._current_nodes = 0
        self._max_r_nodes = max_r_nodes
        self._current_repok_max = 0
        self.build_timeout = b_timeout
        self.method_timeout = m_timeout
        self._time = 0
        self._rec_times = 0
        self._ids = 0

        for k in self._sut.class_map.keys():
            setattr(k, "_engine", self)

    def explore(self):
        """Main method, implements the generalized symbolic execution.

        Yields:
            data.PathExecutionData: The result of the execution of the function under test
        """
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration()
            args = self.instantiate_input()
            self._backups = LazyBackup(args)

            result = self._execute_method_exploration(args)
            yield (result)

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

    def instantiate_input(self):
        types = self._sut.get_method_param_types()
        return [inst.symbolic_instantiation(self, typ) for typ in types]

    def _reset_exploration(self):
        """Resets the exploration variables to it's initial values.
        """
        self._path_condition = []
        self._current_bp = 0
        self._current_nodes = 0
        self._current_depth = 0
        self._rec_times = 0
        self._ids = 0
        for k in self._sut.class_map.keys():
            k._vector = []

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
            data.PathExecutionData: The result of the execution of the function
            under test
        """
        self._stats.total_paths += 1
        pathdata = data.PathExecutionData(self._stats.total_paths, data.PRUNED)

        returnv = None
        exception = None

        self.curr_self = args[0]
        args = args[1:]
        method = getattr(self.curr_self, self._sut.get_method_name())

        self._time = time.time()
        try:
            with Timeout(self.method_timeout), HiddenPrints():
                with MethodExplorationMode(self):
                    if args:
                        returnv = method(*args)
                    else:
                        returnv = method()
                    if sym.is_symbolic_bool(returnv):
                        returnv = returnv.__bool__()

        except excp.MaxDepthException:
            self._stats.pruned_by_depth += 1
        except excp.RepOkFailException:
            self._stats.pruned_by_repok += 1
        except excp.MaxRecursionException:
            if not self.build_stats(pathdata):
                self._stats.pruned_by_rec_limit += 1
            else:
                self._stats.builded_after_rec_limit += 1
        except excp.TimeOutException:
            if not self.build_stats(pathdata):
                self._stats.pruned_by_timeout += 1
            else:
                self._stats.builded_after_timeout += 1
        except Exception as e:
            exception = e
            if not self.build_stats(pathdata):
                self._stats.pruned_by_exception += 1
            else:
                self._stats.builded_after_exception += 1
        else:
            self.build_stats(pathdata)
            if pathdata.status == data.PRUNED:
                self._stats.pruned_by_not_builded += 1
        finally:
            # if exception:
            #     raise exception
            pathdata.time = time.time() - self._time
            self._stats.status_count(pathdata.status)
            return pathdata

    def build_stats(self, pathdata):
        path = self._path_condition
        model = self.smt.get_model(path)

        symbolic_inself = self._backups.get_self()
        symbolic_args = self._backups.get_args()

        builded = False
        try:
            input_self = self.build(symbolic_inself, model)
            input_args = self.build(symbolic_args, model)
        except excp.BuildTimeOutException:
            self._stats.not_builded_by_timeout += 1
        except excp.CouldNotBuildError:
            pass
        except Exception:
            assert False
        else:
            builded = True
        finally:
            if builded:
                pathdata.input_args = input_args
                pathdata.input_self = input_self
                pathdata.pathcondition = path
                pathdata.model = model

                self_end_state = copy.deepcopy(input_self)
                args = copy.deepcopy(input_args)
                returnv = self.execute_method_concretely(self_end_state, args)

                if isinstance(returnv, Exception):
                    if isinstance(returnv, excp.TimeOutException):
                        pathdata.status = data.TIMEOUT
                    else:
                        pathdata.status = data.EXCEPTION
                        pathdata.exception = returnv
                else:
                    if self.execute_repok_concretely(self_end_state):
                        pathdata.status = data.OK
                    else:
                        pathdata.status = data.FAIL

                    pathdata.self_end_state = self_end_state
                    pathdata.returnv = returnv
                return True
            return False

    def execute_method_concretely(self, obj, args):
        assert self.mode == CONCRETE_EXECUTION
        try:
            method = getattr(obj, self._sut.get_method_name())
            with Timeout(self.method_timeout), HiddenPrints():
                if args:
                    returnv = method(*args)
                else:
                    returnv = method()
        except Exception as e:
            returnv = e
        finally:
            return returnv

    def execute_repok_concretely(self, obj):
        assert self.mode == CONCRETE_EXECUTION
        try:
            with Timeout(self.build_timeout):
                result = obj.repok()
        except AttributeError as e:
            raise e
        except excp.TimeOutException as e:
            raise e
        finally:
            return result

    def _reset_for_repok(self, iself, pc_len):
        self._path_condition = helpers.keep_first_n(self._path_condition, pc_len)
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
            return symbolic
        elif im.is_user_defined(symbolic):
            self._current_repok_max = 0
            concretei = inst.concretize(symbolic, model)
            if self.execute_repok_concretely(concretei):
                self._stats.builded_at[self._current_repok_max] += 1
                return concretei

            build = None
            with Timeout(self.build_timeout):
                while not build and self._current_repok_max <= self._max_r_nodes:
                    with HiddenPrints(), BuildStructure(self):
                        build = self.build_partial_struture(symbolic, model)
                    self._current_repok_max += 1

            if build is None:
                raise excp.CouldNotBuildError()
            self._stats.builded_at[self._current_repok_max - 1] += 1
            return build
        assert False

    def node_limit(self):
        if self.mode == METHOD_EXPLORATION:
            return self._current_nodes >= self._max_nodes
        elif self.mode == REPOK_EXPLORATION:
            return self._current_nodes >= self._current_repok_max
        else:
            assert False

    def build_partial_struture(self, input_self, model):
        pc_len = len(self._path_condition)

        unexplored_paths = True
        while unexplored_paths:
            iself = copy.deepcopy(input_self)
            self._reset_for_repok(iself, pc_len)

            result = self._execute_repok_exploration(iself)
            if result is not None:
                return result

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

    def _execute_repok_exploration(self, instance):
        try:
            with RepokExplorationMode(self):
                result = instance.repok()
                if sym.is_symbolic_bool(result):
                    result = result.__bool__()
        except excp.MaxDepthException:
            pass
        except excp.TimeOutException as e:
            raise e
        except excp.MaxRecursionException:
            raise excp.MaxRecursionException("Max recursion reached on repok")
        except AttributeError as e:
            raise e
        else:
            if result:
                model = self.smt.get_model(self._path_condition)
                new_object = inst.concretize(instance, model)
                return new_object
            return None

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
        try:
            with ConservativeRepokMode(self):
                if hasattr(obj, "repok") and not obj.repok():
                    raise excp.RepOkFailException()
                if obj._objid != self.curr_self._objid:
                    if hasattr(self.curr_self, "repok") and not self.curr_self.repok():
                        raise excp.RepOkFailException()
        except excp.NoInitializedException:
            pass
        except excp.CantMakeDecisionException:
            pass
        except excp.RepOkFailException as e:
            raise e
        except AttributeError as e:
            raise e

    def lazy_initialization(self, obj, attr_name):
        pref_name = im.SYMBOLIC_PREFIX + attr_name
        attr = getattr(obj, pref_name)
        if self.mode == CONCRETE_EXECUTION:
            return attr

        is_init = im.is_initialized(obj, attr_name)
        if self.mode == CONSERVATIVE_EXECUTION:
            if not is_init:
                raise excp.NoInitializedException()
            return attr

        attr_type = self._sut.get_attr_type(type(obj), attr_name)
        if im.is_user_defined(attr_type):
            if is_init or not im.is_tracked(obj):
                self.check_recursion_limit(attr)
                return attr

            setattr(obj, im.ISINIT_PREFIX + attr_name, True)
            if attr is None:
                new_value = self.get_next_lazy_step(attr_type)
                setattr(obj, pref_name, new_value)
                self._rec_times = 0

                if self.mode == METHOD_EXPLORATION:
                    if self._current_bp >= len(self._branch_points):
                        self.check_conservative_repok(obj)
                    self.mimic_change(obj, pref_name, new_value)

        else:
            assert sym.Symbolic.is_supported_builtin(attr_type)
            assert attr is not None
            if not is_init:
                setattr(obj, im.ISINIT_PREFIX + attr_name, True)
                if not sym.is_symbolic(attr):
                    new_sym = sym.symbolic_factory(self, attr_type)
                    setattr(obj, pref_name, new_sym)

        return getattr(obj, pref_name)

    def lazy_set_attr(self, obj, attr_name, value):
        pref_name = im.SYMBOLIC_PREFIX + attr_name
        setattr(obj, im.ISINIT_PREFIX + attr_name, True)
        setattr(obj, pref_name, value)

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

    def evaluate(self, expression):
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
        assert self.mode != CONCRETE_EXECUTION

        if self.mode == CONSERVATIVE_EXECUTION:
            raise excp.NoInitializedException()

        if self._current_bp < len(self._branch_points):
            assert isinstance(self._branch_points[self._current_bp], ConditionalBranchPoint)
            condition_value = self._branch_points[self._current_bp].get_branch()
        else:
            if self._max_depth < self._current_depth:
                raise excp.MaxDepthException
            self._current_depth += 1

            condition_value = self.conditioned_value(expression)
            if condition_value is not None:
                self._branch_points.append(ConditionalBranchPoint(condition_value))
            else:
                self._branch_points.append(ConditionalBranchPoint())
                condition_value = True

        self._current_bp += 1

        if condition_value:
            self._path_condition.append(expression)
        else:
            self._path_condition.append(self.smt.Not(expression))
        return condition_value

    def conditioned_value(self, expression):
        """Checks if a constraint's value is conditioned by the path.

        Checks whether the constraint represented by sym_bool has a
        determined value conditioned by the path_condition.

        Args:
            sym_bool: the symbolic bool that represents a constraint.

        Returns:
            True or False if the value it's conditioned by the path_condition,
            None otherwise.
        """
        conditions = True
        for c in self._path_condition:
            conditions = self.smt.And(conditions, c)
        true_cond = self.smt.check(self.smt.And(conditions, expression))
        false_cond = self.smt.check(
            self.smt.And(conditions, self.smt.Not(expression))
        )
        if true_cond and not false_cond:
            return True
        if false_cond and not true_cond:
            return False
        return None

    def check_recursion_limit(self, obj):
        if self.mode != REPOK_EXPLORATION:
            self._rec_times += 1
            if self._rec_times > RECURSION_LIMIT:
                raise excp.MaxRecursionException(str(self._rec_times))

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
            setattr(obj_backup, attr_name, new_val)
        else:
            setattr(obj_backup, attr_name, copy.deepcopy(new_value))


def raise_timeout(signum, frame):
    raise excp.TimeOutException()


def raise_build_timeout(signum, frame):
    raise excp.BuildTimeOutException()


class Timeout:
    def __init__(self, time):
        self.time = time

    def __enter__(self):
        signal.signal(signal.SIGALRM, raise_timeout)
        signal.alarm(self.time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


class BuildStructure:
    def __init__(self, engine):
        self.pc_len = 0
        self.orig_bp = []
        self.engine = engine

    def __enter__(self):
        self.pc_len = len(self.engine._path_condition)
        self.orig_bp = copy.deepcopy(self.engine._branch_points)
        self.engine._branch_points = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine._branch_points = self.orig_bp
        self.engine._path_condition = helpers.keep_first_n(self.engine._path_condition, self.pc_len)


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class RepokExplorationMode:
    def __init__(self, engine):
        self.engine = engine

    def __enter__(self):
        self.engine.mode = REPOK_EXPLORATION

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.mode = CONCRETE_EXECUTION


class MethodExplorationMode:
    def __init__(self, engine):
        self.engine = engine

    def __enter__(self):
        self.engine.mode = METHOD_EXPLORATION

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.mode = CONCRETE_EXECUTION


class ConservativeRepokMode:
    def __init__(self, engine):
        self.engine = engine

    def __enter__(self):
        self.engine.mode = CONSERVATIVE_EXECUTION

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.mode = METHOD_EXPLORATION


class LazyBackup:
    def __init__(self, datalist):
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
