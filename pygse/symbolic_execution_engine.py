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

    _branching_points = []
    _path_condition = []
    _current_bp = 0
    _current_depth = 0
    _max_depth = 0

    _globalstats = None
    _sut = None
    _real_to_proxy = {}

    @classmethod
    def initialize(cls, sut_data, max_depth):
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
        unexplored_paths = True
        while unexplored_paths:
            cls.reset_exploration()

            args = [cls.instantiate(a) for a in cls._sut.types]

            result = cls.execute_program(args)
            yield (result)

            cls.remove_explored_branching_points()

            if not cls._branching_points:
                unexplored_paths = False

    @classmethod
    def reset_exploration(cls):
        cls._path_condition = []
        cls._current_bp = 0
        cls._current_depth = 0
        for k in cls._sut.class_params_map.keys():
            k._vector = [None]

    @classmethod
    def execute_program(cls, args):
        cls._globalstats.total_paths += 1
        stats = ExecutionStats(cls._globalstats.complete_exec)
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
            cls._globalstats.complete_exec += 1
            stats.pathcondition = cls._path_condition
            stats.model = proxy.smt.get_model(cls._path_condition)
            stats.self_structure = the_self
            stats.concrete_self = cls._concretize(copy.deepcopy(the_self), stats.model)
            if args:
                stats.concrete_args = cls._concretize(copy.deepcopy(args), stats.model)

            if stats.exception:
                cls._globalstats.status_count(stats.status)
                return stats

            if not cls.check_repok(returnv):
                stats.status = Status.FAIL
                stats.errors.append("Return value RepOk fail")
            if not cls.check_repok(the_self):
                stats.status = Status.FAIL
                stats.errors.append("Self RepOk fail")
            stats.returnv = returnv
            stats.concrete_return = cls._concretize(
                copy.deepcopy(stats.returnv), stats.model
            )
            cls._globalstats.status_count(stats.status)
            return stats

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
        # FIXME: Hay que iterar sobre builtins que puedan contener ProxyObjects
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
            assert isinstance(branch_point, LazyStep)
            index = branch_point.get_branch()
            cls._current_bp += 1

            if index < len(vector):
                return vector[index]

            n = cls.create_instance(lazy_class)
            vector.append(n)
            return n

        cls._branching_points.append(LazyStep(len(vector)))
        cls._current_bp += 1
        return None

    @classmethod
    def instantiate(cls, typ):
        if typ in cls._real_to_proxy.keys():
            return cls._real_to_proxy[typ]()
        elif isinstance(typ, type(None)):
            return None
        elif proxy.is_user_defined(typ):
            instance = cls.create_instance(typ)
            typ._vector = [None, instance]
            return instance
        return typ()

    @classmethod
    def create_instance(cls, user_def_class):
        init_types = cls.get_init_types(user_def_class)
        init_args = [cls.make_symbolic(a) for a in init_types]
        if init_args:
            return user_def_class(*init_args)
        return user_def_class()

    @classmethod
    def get_init_types(cls, user_def_class):
        init_types = copy.deepcopy(cls._sut.class_params_map[user_def_class])
        number_params = user_def_class.__init__.__code__.co_argcount
        if number_params - 1 != len(init_types):
            raise MissingTypesError(
                "Incomplete type annotations in: " + str(user_def_class)
            )
        return init_types

    @classmethod
    def make_symbolic(cls, typ):
        if typ in cls._real_to_proxy.keys():
            return cls._real_to_proxy[typ]()
        elif isinstance(typ, type(None)) or proxy.is_user_defined(typ):
            return None
        return typ()

    @classmethod
    def evaluate(cls, bool_proxy):
        partial_solve = cls._get_partial_solve(bool_proxy)
        if partial_solve is not None:
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
        true_cond = proxy.smt.check(proxy.smt.And(conditions, bool_proxy.formula))
        false_cond = proxy.smt.check(
            proxy.smt.And(conditions, proxy.smt.Not(bool_proxy.formula))
        )
        if true_cond and not false_cond:
            return True
        if false_cond and not true_cond:
            return False
        if not true_cond and not false_cond:
            raise UnsatBranchError()

    @classmethod
    def get_next_conditional_step(cls):
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
        if value:
            raise RepOkFailException()

    @classmethod
    def statistics(cls):
        return cls._globalstats
