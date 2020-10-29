"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynamically allocated structures with the use of lazy initialization.

"""

import copy
import time
import sys
import os
import signal

import exceptions as excp
import instances as inst
import instance_management as im
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


class SEEngine:
    """Symbolic Execution engine.

    Performs symbolic execution on programs. Handles complex
    dynamically allocated structures with the use of lazy initialization.

    Attributes:
        _branching_points (list): Represents the decisions made at the program
        symbolic execution. The program execution has two possible branching
        scenarios:
            - Lazy Initialization Step: It happens when a user-defined class field
            is accessed, so the engine must initialize it to each possibility creating
            different executions paths.
            The possible choices when initializing a filed are:
                - None
                - Any previous created instances of the user-defined class.
                - A new instance of that class.
            - Conditional Step: It happens the execution reaches a condition over
            symbolic fields, so two there are two possible decisions: make it True
            or make it False, generating different path executions.

        _path_condition (list): Collects all the path constraints of the current
        execution.

        _current_bp (int): Is the current branching point, it could
        be a Lazy Initialization Stem or a Conditional Step.

        _curr_depth (int): Depth's of the current execution tree.

        _max_depth (int): Max depth search, any execution that exceeds this value
        is pruned.

        _stats (ExplorationStats): Contains the overall statistics of all executed
        program paths.

        _sut (SUT): Data of the program under test, contains the method or function,
        parameter types, etc.

    """

    def __init__(self, sut_data, cfg_args: dict):
        self._sut = sut_data
        self._max_depth = cfg_args["max_depth"]
        self._max_nodes = cfg_args["max_nodes"]
        self._max_r_nodes = cfg_args["max_repok_nodes"]
        self.build_timeout = cfg_args["build_timeout"]
        self.method_timeout = cfg_args["method_timeout"]
        self.max_get = cfg_args["max_get"]

        self.smt = SMT((SMTInt, SMTBool), SMTSolver)
        self._stats = data.ExplorationStats()
        self._branch_points = []
        self._path_condition = []
        self._backups = None
        self.curr_self = None
        self._current_depth = 0
        self._current_bp = 0
        self._current_nodes = 0
        self._current_repok_max = 0
        self.time = 0
        self.get_count = 0
        self._ids = 0
        self.mode = CONCRETE_EXECUTION

        for k in self._sut.class_map.keys():
            setattr(k, "_engine", self)

    def explore(self):
        """Main method, explores al feasible possibilities.

        Yields:
            PathExecutionData: The result of the execution of the method under test
        """
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration()
            args = self._instantiate_input()
            self._backups = LazyBackup(args)

            result = self._execute_method_exploration(args)
            yield (result)

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

    def _reset_exploration(self):
        """Resets the exploration variables to its initial values."""
        self._path_condition = []
        self._current_bp = 0
        self._current_nodes = 0
        self._current_depth = 0
        self.get_count = 0
        self._ids = 0
        for k in self._sut.class_map.keys():
            k._vector = []

    def _instantiate_input(self):
        """Instantiates the arguments for the method under test.

        For builtin types, its corresponding symbolic type is instantiated
        For user-defined-types: A new instance with uninitialized fields is created.
        """
        types = self._sut.get_method_param_types()
        return [inst.symbolic_instantiation(self, typ) for typ in types]

    def _remove_explored_branch(self):
        """Removes the last explored branch.

        Advance the last branching point and removes it if it
        has been fully explored.
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

    def _execute_method_exploration(self, args):
        """Performs the method exploration.

        Executes method and returns all the execution data, like the returned
        value, the final state of the self, the path condition, the
        model, exceptions raised, concrete values of arguments,
        result, and state.

        Args:
            args (List): Symbolic and partially symbolic arguments.

        Returns:
            PathExecutionData: The result of the exploration (input builded, arguments,
            path_condition, etc).
        """
        self._stats.total_paths += 1
        pathdata = data.PathExecutionData(self._stats.total_paths, data.PRUNED)

        returnv = None
        exception = None

        self.curr_self = args[0]
        args = args[1:]
        method = getattr(self.curr_self, self._sut.get_method_name())

        self.time = time.time()
        try:
            with Timeout(self.method_timeout), HiddenPrints():
                with MethodExplorationMode(self):
                    if not self.curr_self.repok():
                        return pathdata
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
            pass
        except excp.TimeOutException:
            if not self._build_stats(pathdata):
                self._stats.pruned_by_timeout += 1
            else:
                if pathdata.status != data.TIMEOUT:
                    pathdata.status = data.PRUNED
                else:
                    self._stats.builded_after_timeout += 1
        except Exception as e:
            exception = e
            if not self._build_stats(pathdata):
                self._stats.pruned_by_exception += 1
            else:
                if pathdata.status != data.EXCEPTION:
                    pathdata.status = data.PRUNED
                else:
                    self._stats.builded_after_exception += 1
        else:
            self._build_stats(pathdata)
            if pathdata.status == data.PRUNED:
                self._stats.pruned_by_not_builded += 1
        finally:
            # if exception:
            #     raise exception
            pathdata.time = time.time() - self.time
            return pathdata

    def _build_stats(self, pathdata):
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
        except Exception as e:
            raise e
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
                return concretei

            build = None
            with Timeout(self.build_timeout):
                while not build and self._current_repok_max <= self._max_r_nodes:
                    with HiddenPrints(), BuildStructure(self):
                        build = self.build_partial_structure(symbolic, model)
                    self._current_repok_max += 1

            if build is None:
                raise excp.CouldNotBuildError()
            return build

    def build_partial_structure(self, input_self, model):
        pc_len = len(self._path_condition)

        unexplored_paths = True
        while unexplored_paths:
            iself = copy.deepcopy(input_self)
            self._reset_for_build(iself, pc_len)

            result = self._execute_repok_exploration(iself)
            if result is not None:
                return result

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

    def _reset_for_build(self, iself, pc_len):
        self._path_condition = helpers.keep_first_n(self._path_condition, pc_len)
        self._current_bp = 0
        self._current_depth = 0
        self._current_nodes = 0
        for k in self._sut.class_map.keys():
            k._vector = []
        inst.fill_class_vectors(iself)

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

    def execute_method_concretely(self, obj, args):
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
        try:
            with Timeout(self.build_timeout):
                result = obj.repok()
        except AttributeError as e:
            raise e
        except excp.TimeOutException as e:
            raise e
        finally:
            return result

    def lazy_initialization(self, owner, attr_name):
        """Performs the lazy initialization of the attribute.

        It hooks every get over a symbolic or partially symbolic attribute
        of the class, depending of the current engine mode it will behave
        differently.

        Args:
            owner: The object that contains the attribute to be initialized.
            attr_name (str): The name of the attribute.

        Returns:
            The requested attribute of the object
        """
        pref_name = im.SYMBOLIC_PREFIX + attr_name
        attr = getattr(owner, pref_name)
        if self.mode == CONCRETE_EXECUTION:
            return attr

        is_init = im.is_initialized(owner, attr_name)
        if self.mode == CONSERVATIVE_EXECUTION:
            if not is_init:
                raise excp.NoInitializedException()
            return attr

        attr_type = self._sut.get_attr_type(type(owner), attr_name)
        if im.is_user_defined(attr_type):
            if is_init or not im.is_tracked(owner):
                self.check_get_limit(attr)
                return attr

            setattr(owner, im.ISINIT_PREFIX + attr_name, True)
            if attr is None:
                new_value = self.get_next_lazy_step(attr_type)
                setattr(owner, pref_name, new_value)
                self.get_count = 0

                if self.mode == METHOD_EXPLORATION:
                    if self._current_bp >= len(self._branch_points):
                        self.check_conservative_repok(owner)
                    self.mimic_change(owner, pref_name, new_value)

        else:
            if not is_init:
                setattr(owner, im.ISINIT_PREFIX + attr_name, True)
                if not sym.is_symbolic(attr):
                    new_sym = sym.symbolic_factory(self, attr_type)
                    setattr(owner, pref_name, new_sym)

        return getattr(owner, pref_name)

    def get_next_lazy_step(self, lazy_class):
        """Returns the corresponding initialization for the current branch point.

        If it's a new initialization step creates the branching point and
        return a new instance as first initialization, on the other hand
        if it's an already existent one it gets the corresponding initialization
        that could be:
            - A new lazy_class instance
            - None
            - Any previous created instances of lazy_class.

        Args:
            lazy_class: Type of the instance to be created.

        Returns:
            An instance of lazy_class or None.
        """
        if self._current_bp < len(self._branch_points):
            branch_point = self._branch_points[self._current_bp]
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

    def node_limit(self):
        if self.mode == METHOD_EXPLORATION:
            return self._current_nodes >= self._max_nodes
        return self._current_nodes >= self._current_repok_max

    def check_get_limit(self, obj):
        if self.mode != REPOK_EXPLORATION:
            self.get_count += 1
            if self.get_count > self.max_get:
                raise excp.MaxRecursionException(str(self.get_count))

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

    def mimic_change(self, obj, attr_name, new_value):
        obj_backup = self._backups.get_backup_of(obj)

        if self._branch_points[self._current_bp - 1].get_branch() > 1:
            new_val = self._backups.get_backup_of(new_value)
            setattr(obj_backup, attr_name, new_val)
        else:
            setattr(obj_backup, attr_name, copy.deepcopy(new_value))

    def lazy_set_attr(self, owner, attr_name, value):
        """Sets the attribute and mark it as initialized.

        It hooks every set over a symbolic or partially symbolic attribute
        of the class. It sets the attribute and turn its initialized field
        to True.

        Args:
            owner: The object that contains the attribute to be setted.
            attr_name (str): The name of the attribute.
            value: The new value of the attribute.
        """
        pref_name = im.SYMBOLIC_PREFIX + attr_name
        setattr(owner, im.ISINIT_PREFIX + attr_name, True)
        setattr(owner, pref_name, value)

    def evaluate(self, expression):
        """Evaluates an expression.

        If there is an existing branching point, it add the corresponding
        expression to the path condition and returns its value.
        Else there isn't an existing branch point for the corresponding point
        of the method execution, if the boolean value of the expression is
        conditioned to True or False by the path conditions, that value is
        returned and no branching point is created. Otherwise (both values are
        feasible) the branch point is created and true is returned as first value.

        Args:
            expression: A path constraint.

        Returns:
            True or False, depending on the evaluation.
        """
        if self.mode == CONSERVATIVE_EXECUTION:
            raise excp.NoInitializedException()

        if self._current_bp < len(self._branch_points):
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

        Checks whether the constraint represented by the expression has a
        determined value conditioned by the path_condition.

        Args:
            expression: A path constraint.

        Returns:
            True or False if the value it's conditioned by the path_condition,
            None otherwise.
        """
        conditions = True
        for c in self._path_condition:
            conditions = self.smt.And(conditions, c)
        true_cond = self.smt.check(self.smt.And(conditions, expression))
        false_cond = self.smt.check(self.smt.And(conditions, self.smt.Not(expression)))
        if true_cond and not false_cond:
            return True
        if false_cond and not true_cond:
            return False
        return None

    def statistics(self):
        """Returns the collected statistics of all executions."""
        return self._stats


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
        orig_pathc = helpers.keep_first_n(self.engine._path_condition, self.pc_len)
        self.engine._path_condition = orig_pathc


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
