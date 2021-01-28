"""Symbolic execution Engine

Implements a Generalized Symbolic execution engine that handles complex
dynamically allocated structures with the use of lazy initialization.

"""

import copy
import sys
import os
import signal
import functools

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
NO_MODE = 0
GENERATION_MODE = 1


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

        _sut (SUT): Data of the program under test, contains the method or function,
        parameter types, etc.

    """

    def __init__(self, sut_data, cfg_args: dict):
        self._sut = sut_data
        self._max_depth = cfg_args["max_depth"]
        self._max_nodes = cfg_args["max_nodes"]
        self.timeout = cfg_args["timeout"]

        self.initializations_map = {}
        self.classes_ids = {}

        self.smt = SMT((SMTInt, SMTBool), SMTSolver)
        self._branch_points = []
        self._path_condition = []

        self._current_depth = 0
        self._current_bp = 0
        self._current_nodes = 0
        self._ids = 0
        self.mode = NO_MODE

        for k in self._sut.class_map.keys():
            setattr(k, "_engine", self)
            self.classes_ids[k] = 0

    def explore(self, method_name, input_self, constraints):
        """Main method, explores al feasible possibilities.

        Yields:
            PathExecutionData: The result of the execution of the method under test
        """
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration(constraints)

            result = self._explore_method_path(method_name, input_self)
            if result is not None:
                yield (result)

            unexplored_paths = self._set_next_path()

    def generate_structures(self):
        """comment here"""
        structures = []
        unexplored_paths = True

        while unexplored_paths:
            self._reset_exploration()

            end_self = self._explore_repok_path()
            if end_self is not None:
                structures.append((end_self, self._path_condition))

            unexplored_paths = self._set_next_path()

        return structures

    def _explore_repok_path(self):
        result = None
        try:
            with RepokExplorationMode(self):
                instance = inst.symbolic_instantiation(self, self._sut.sclass)
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

    def _reset_exploration(self, constraints=[]):
        """Resets the exploration variables to its initial values."""
        self._path_condition = copy.deepcopy(constraints)
        self._current_bp = 0
        self._current_nodes = 0
        self._current_depth = 0
        for k in self._sut.class_map.keys():
            k._vector = []
            self.classes_ids[k] = 0

    def _instantiate_args(self, method_name):
        """Instantiates the arguments for the method under test.

        For builtin types, its corresponding symbolic type is instantiated
        For user-defined-types: A new instance with uninitialized fields is created.
        """
        types = self._sut.methods_map[method_name].types_list[1:]
        return [inst.symbolic_instantiation(self, typ) for typ in types]

    def _set_next_path(self):
        """Removes the last explored branch.

        Advance the last branching point and removes it if it
        has been fully explored.
        """
        if not self._branch_points:
            # All paths in symbolic execution tree were explored.
            return False

        last_bp = self._branch_points[-1]
        last_bp.advance_branch()

        if last_bp.all_branches_covered():
            del self._branch_points[-1]
            return self._set_next_path()

        return True

    def _explore_method_path(self, method_name, input_self):
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
        returnv = exception = args = None
        timeout = False
        pruned = False

        end_self = copy.deepcopy(input_self)
        method = getattr(end_self, method_name)

        try:
            with Timeout(self.timeout), HiddenPrints():
                args = self._instantiate_args(method_name)
                if args:
                    returnv = method(*args)
                else:
                    returnv = method()
                if sym.is_symbolic_bool(returnv):
                    returnv = returnv.__bool__()

        except excp.MaxDepthException:
            pruned = True
        except excp.TimeOutException:
            timeout = True
        except Exception as e:
            exception = e
        finally:
            # if exception:
            #     raise exception
            if pruned:
                return None

            model = self.smt.get_model(self._path_condition)
            conc_args = inst.concretize(args, model)
            conc_end_self = inst.concretize(end_self, model)
            conc_input_self = inst.concretize(input_self, model)

            pathdata = PathExecutionData()
            pathdata.self_end_state = conc_end_self
            pathdata.input_self = conc_input_self
            pathdata.input_args = conc_args
            pathdata.returnv = inst.concretize(returnv, model)
            pathdata.exception = exception

            if timeout:
                iself = copy.deepcopy(conc_input_self)
                args = copy.deepcopy(conc_args)
                ret = self.execute_method_concretely(iself, args, method_name)
                if isinstance(ret, excp.TimeOutException):
                    pathdata.status = data.TIMEOUT
                else:
                    return None
            elif exception:
                pathdata.status = data.EXCEPTION
            elif self.execute_repok_concretely(conc_end_self):
                pathdata.status = data.OK
            else:
                pathdata.status = data.FAIL

            return pathdata

    def execute_repok_concretely(self, obj):
        try:
            with Timeout(self.timeout):
                result = obj.repok()
        except AttributeError as e:
            raise e
        except excp.TimeOutException as e:
            raise e
        finally:
            return result

    def execute_method_concretely(self, iself, args, method_name):
        try:
            method = getattr(iself, method_name)
            with Timeout(self.timeout), HiddenPrints():
                if args:
                    returnv = method(*args)
                else:
                    returnv = method()
        except Exception as e:
            returnv = e
        finally:
            return returnv

    def _get_attr(self, owner, attr_name):
        """Performs the initialization of the attribute.

        It is called whenever the target method performs a get over a field
        of a partially symbolic structure. It returns or sets and returns the
        new value depending on the case.

        Args:
            owner: The object that contains the attribute to be initialized.
            attr_name (str): The name of the attribute.

        Returns:
            The requested attribute of the object
        """
        pref_name = im.SYMBOLIC_PREFIX + attr_name
        if self.mode != GENERATION_MODE or im.is_initialized(owner, attr_name) or not im.is_tracked(owner):
            return getattr(owner, pref_name)

        setattr(owner, im.ISINIT_PREFIX + attr_name, True)
        attr_type = self._sut.get_attr_type(type(owner), attr_name)

        if im.is_user_defined(attr_type):
            new_value = self._lazy_initialization(attr_type)
            setattr(owner, pref_name, new_value)
        else:
            new_value = sym.symbolic_factory(self, attr_type)
            setattr(owner, pref_name, new_value)

        return new_value


    def _lazy_initialization(self, lazy_class):
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
        if self._current_nodes >= self._max_nodes:
            new_bp.advance_branch()
            return None
        self._current_nodes += 1
        n = inst.symbolize_partially(self, lazy_class)
        lazy_class._vector.append(n)
        return n

    def _set_attr(self, owner, attr_name, value):
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
        if self._current_bp < len(self._branch_points):
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
        # functios.reduce is a fold left function
        conditions = functools.reduce(self.smt.And, self._path_condition, True)
        true_cond = self.smt.check(self.smt.And(conditions, expression))
        false_cond = self.smt.check(self.smt.And(conditions, self.smt.Not(expression)))

        if true_cond and not false_cond:
            return True
        if false_cond and not true_cond:
            return False
        return None


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
        self.engine.mode = GENERATION_MODE

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.mode = NO_MODE


class PathExecutionData:
    def __init__(self, exec_number: int = 0):
        self.self_end_state = None
        self.input_self = None
        self.input_args = ()
        self.returnv = None
        self.exception = None
        self.number = exec_number
        self.status = None
