"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynamically allocated structures with the use of lazy initialization.

"""

import copy
import sys
import os
import signal

import exceptions as excp
import instances as inst
import instance_management as im
import symbolics as sym
import data

from branching_steps import LazyBranchPoint, ConditionalBranchPoint

from smt.smt import SMT
from smt.sort_z3 import SMTInt, SMTBool
from smt.solver_z3 import SMTSolver


# Engine modes of execution
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
        self.build_timeout = cfg_args["build_timeout"]
        self.method_timeout = cfg_args["method_timeout"]

        self.smt = SMT((SMTInt, SMTBool), SMTSolver)
        self._stats = data.ExplorationStats()
        self._branch_points = []
        self._path_condition = []

        self._current_depth = 0
        self._current_bp = 0
        self._current_nodes = 0
        self._ids = 0
        self.mode = CONCRETE_EXECUTION

        for k in self._sut.class_map.keys():
            setattr(k, "_engine", self)

    def explore(self, method_name, input_self, conditions):
        """Main method, explores al feasible possibilities.

        Yields:
            PathExecutionData: The result of the execution of the method under test
        """
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration(conditions)

            args = self._instantiate_args(method_name)

            result = self._execute_method_exploration(method_name, input_self, args)
            yield (result)

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

    def generate_structures(self):
        """ comment here
        """
        structures = []
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration()
            partial_self = inst.symbolic_instantiation(self, self._sut.sclass)

            end_self = self._explore_repok(partial_self)
            if end_self is not None:
                structures.append((end_self, copy.deepcopy(self._path_condition)))

            self._remove_explored_branch()
            if not self._branch_points:
                unexplored_paths = False

        return structures

    def _explore_repok(self, instance):
        try:
            with RepokExplorationMode(self):
                result = instance.repok()
                if sym.is_symbolic_bool(result):
                    result = result.__bool__()
        except excp.MaxDepthException:
            pass
        except excp.TimeOutException:
            pass
        except Exception as e:
            raise e
        else:
            if result:
                return instance
            return None

    def _reset_exploration(self, conditions=[]):
        """Resets the exploration variables to its initial values.
        """
        self._path_condition = copy.deepcopy(conditions)
        self._current_bp = 0
        self._current_nodes = 0
        self._current_depth = 0
        self._ids = 0
        for k in self._sut.class_map.keys():
            k._vector = []

    def _instantiate_args(self, method_name):
        """Instantiates the arguments for the method under test.

        For builtin types, its corresponding symbolic type is instantiated
        For user-defined-types: A new instance with uninitialized fields is created.
        """
        types = self._sut.methods_map[method_name].types_list[1:]
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

    def _execute_method_exploration(self, method_name, input_self, args):
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
        returnv = None
        exception = None
        timeout = False

        end_self = copy.deepcopy(input_self)
        method = getattr(end_self, method_name)

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
        except excp.TimeOutException:
            timeout = True
        except Exception as e:
            exception = e
        finally:
            # if exception:
            #     raise exception

            model = self.smt.get_model(self._path_condition)
            conc_args = inst.concretize(args, model)
            conc_end_self = inst.concretize(end_self, model)
            conc_input_self = inst.concretize(input_self, model)

            self._stats.total_paths += 1
            pathdata = PathExecutionData(self._stats.total_paths)
            pathdata.self_end_state = conc_end_self
            pathdata.input_self = conc_input_self
            pathdata.input_args = conc_args
            pathdata.returnv = inst.concretize(returnv, model)
            pathdata.exception = exception

            if timeout:
                pathdata.status = data.TIMEOUT
            elif exception:
                pathdata.status = data.EXCEPTION
            elif self.execute_repok_concretely(conc_end_self):
                pathdata.status = data.OK
            else:
                pathdata.status = data.FAIL

            return pathdata

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
        if self.mode != REPOK_EXPLORATION:
            return attr

        is_init = im.is_initialized(owner, attr_name)
        attr_type = self._sut.get_attr_type(type(owner), attr_name)
        if im.is_user_defined(attr_type):
            if is_init or not im.is_tracked(owner):
                return attr

            setattr(owner, im.ISINIT_PREFIX + attr_name, True)
            if attr is None:
                new_value = self.get_next_lazy_step(attr_type)
                setattr(owner, pref_name, new_value)
        else:
            assert sym.Symbolic.is_supported_builtin(attr_type)
            assert attr is not None
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
        if self.mode == METHOD_EXPLORATION:
            assert False
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
        if self._current_nodes >= self._max_nodes:
            new_bp.advance_branch()
            return None
        self._current_nodes += 1
        n = inst.symbolize_partially(self, lazy_class)
        lazy_class._vector.append(n)
        return n

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
        assert self.mode != CONCRETE_EXECUTION
        if self._current_bp < len(self._branch_points):
            assert isinstance(
                self._branch_points[self._current_bp], ConditionalBranchPoint
            )
            condition_value = self._branch_points[self._current_bp].get_branch()
        else:
            if self._max_depth < self._current_depth:
                raise excp.MaxDepthException()
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

        assert self.path_condition_sat()
        return condition_value

    def path_condition_sat(self):
        conditions = True
        for c in self._path_condition:
            conditions = self.smt.And(conditions, c)
        return self.smt.check(conditions)

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
        """Returns the collected statistics of all executions.
        """
        return self._stats


def raise_timeout(signum, frame):
    raise excp.TimeOutException()


class Timeout:
    def __init__(self, max_time):
        self.time = max_time

    def __enter__(self):
        signal.signal(signal.SIGALRM, raise_timeout)
        signal.alarm(self.time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


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


class PathExecutionData:
    def __init__(self, exec_number: int):
        self.self_end_state = None
        self.input_self = None
        self.input_args = ()
        self.returnv = None
        self.exception = None
        self.number = exec_number
        self.status = None
