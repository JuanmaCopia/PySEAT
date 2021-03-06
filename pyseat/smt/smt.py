from decorator import decorator
from smt.sort_base import SMTSortBase
from smt.solver_base import SMTSolverBase


# Exceptions generated by the Solver. All exeptions generated by the sorts
# or the solver are internally catched and re-raised as SMTExceptions
class SMTException(Exception):
    pass


class SMTCantFoundModel(SMTException):
    def __init__(self, formulas):
        super().__init__("Can't found a model for the formulas\n\t%s" % formulas)


def wrap_exceptions(fun):
    """
    Catch all the internal (in use) solver exceptions and raises SMTExceptions
    """

    def new_fun(fun, self, *args, **kwargs):
        exceptions = self._exeptions
        try:
            return fun(self, *args, **kwargs)
        except exceptions as e:
            raise SMTException(e)
        except Exception as e:
            raise e

    return decorator(new_fun, fun)


class SMT(object):
    def __init__(self, sorts=(), solver=None, **kwargs):
        assert issubclass(solver, SMTSolverBase)
        self._solver = solver()
        self._sorts = sorts
        self._vars = {}
        self._exeptions = solver.exceptions
        for x in sorts:
            assert issubclass(x, SMTSortBase)
            self._vars[x] = 0

    # TODO: Implement this funtions in a more eficient way! It is possible
    @wrap_exceptions
    def check(self, formula):
        self._solver.clear()
        self._solver.add(formula)
        return self._solver.check() == "sat"

    @wrap_exceptions
    def get_model(self, formula):
        self._solver.clear()
        self._solver.add(formula)
        return self._solver.solve()

    @wrap_exceptions
    def simplify(self, formula):
        return self._solver.simplify(formula)

    @wrap_exceptions
    def sort_of(self, value):
        for s in self._sorts:
            if s.belongsToSort(value):
                return s

    @wrap_exceptions
    def is_smt_value(self, value):
        s = self.sort_of(value)
        if s != None:
            return s.isSMTValue(value)
        else:
            False

    @wrap_exceptions
    def concrete_value(self, value):
        """
        If val is an smt_value, represent it as a concrete python object
        """
        s = self.sort_of(value)
        return s.concreteValue(value)

    @wrap_exceptions
    def Const(self, sort, *args, **kwargs):
        var_name = "%s_%s" % (sort.name, self._vars[sort])
        self._vars[sort] += 1
        return sort.Const(var_name, *args, **kwargs)

    @wrap_exceptions
    def Add(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Add(left, right)
        elif ss:
            return ss.Add(left, right)
        else:
            return left + right

    @wrap_exceptions
    def Sub(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Sub(left, right)
        elif ss:
            return ss.Sub(left, right)
        else:
            return left - right

    @wrap_exceptions
    def Mul(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Mul(left, right)
        elif ss:
            return ss.Mul(left, right)
        else:
            return left * right

    @wrap_exceptions
    def Div(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Div(left, right)
        elif ss:
            return ss.Div(left, right)
        else:
            return left / right

    @wrap_exceptions
    def Neg(self, left):
        s = self.sort_of(left)
        if s:
            return s.Neg(left)
        else:
            return -left

    @wrap_exceptions
    def Mod(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Mod(left, right)
        elif ss:
            return ss.Mod(left, right)
        else:
            return left % right

    @wrap_exceptions
    def Not(self, left):
        s = self.sort_of(left)
        if s:
            return s.Not(left)
        else:
            return not left

    @wrap_exceptions
    def Eq(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Eq(left, right)
        elif ss:
            return ss.Eq(left, right)
        else:
            return left == right

    @wrap_exceptions
    def Gt(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Gt(left, right)
        elif ss:
            return ss.Gt(left, right)
        else:
            return left > right

    @wrap_exceptions
    def Ge(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Ge(left, right)
        elif ss:
            return ss.Ge(left, right)
        else:
            return left >= right

    @wrap_exceptions
    def Lt(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Lt(left, right)
        elif ss:
            return ss.Lt(left, right)
        else:
            return left < right

    @wrap_exceptions
    def Le(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Le(left, right)
        elif ss:
            return ss.Le(left, right)
        else:
            return left <= right

    @wrap_exceptions
    def And(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.And(left, right)
        elif ss:
            return ss.And(left, right)
        else:
            return left and right

    @wrap_exceptions
    def Or(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Or(left, right)
        elif ss:
            return ss.Or(left, right)
        else:
            return left or right

    @wrap_exceptions
    def Xor(self, left, right):
        s, ss = self.sort_of(left), self.sort_of(right)
        if s:
            return s.Xor(left, right)
        elif ss:
            return ss.Xor(left, right)
        else:
            return left ^ right

    @wrap_exceptions
    def Select(self, array, index):
        s = self.sort_of(array)
        return s.Select(array, index)

    @wrap_exceptions
    def Store(self, array, index, value):
        s = self.sort_of(array)
        return s.Store(array, index, value)
