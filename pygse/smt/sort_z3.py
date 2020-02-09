import pygse.smt.sort_base as sort_base
import z3


class SMTInt(sort_base.SMTIntBase):
    sort = z3.IntSort()

    @classmethod
    def Const(cls, name):
        return z3.Int(name)

    @classmethod
    def Add(cls, left, right):
        return left + right

    @classmethod
    def Sub(cls, left, right):
        return left - right

    @classmethod
    def Mul(cls, left, right):
        return left * right

    @classmethod
    def Div(cls, left, right):
        return left / right

    @classmethod
    def Neg(cls, left):
        return -left

    @classmethod
    def Mod(cls, left, right):
        return left % right

    @classmethod
    def Eq(cls, left, right):
        return left == right

    @classmethod
    def Gt(cls, left, right):
        return left > right

    @classmethod
    def Ge(cls, left, right):
        return left >= right

    @classmethod
    def Le(cls, left, right):
        return left <= right

    @classmethod
    def Lt(cls, left, right):
        return left < right

    @classmethod
    def belongsToSort(cls, value):
        return z3.is_int(value)

    @classmethod
    def isSMTValue(cls, value):
        return z3.is_int_value(value)

    @classmethod
    def concreteValue(cls, value):
        return value.as_long()


class SMTBool(sort_base.SMTBoolBase):
    sort = z3.BoolSort()

    @classmethod
    def Const(cls, name):
        return z3.Bool(name)

    @classmethod
    def And(cls, left, right):
        return z3.And(left, right)

    @classmethod
    def Or(cls, left, right):
        return z3.Or(left, right)

    @classmethod
    def Xor(cls, left, right):
        return z3.Xor(left, right)

    @classmethod
    def Not(cls, left):
        return z3.Not(left)

    @classmethod
    def belongsToSort(cls, value):
        return z3.is_bool(value)

    @classmethod
    def isSMTValue(cls, value):
        return z3.is_bool(value)

    @classmethod
    def concreteValue(cls, value):
        return z3.is_true(value)


class SMTChar(sort_base.SMTCharBase):
    sort = z3.BitVecSort(16)

    @classmethod
    def Const(cls, name):
        return z3.Const(name, z3.BitVecSort(16))

    @classmethod
    def Eq(cls, left, right):
        return left == right

    @classmethod
    def Gt(cls, left, right):
        return z3.UGT(left, right)

    @classmethod
    def Ge(cls, left, right):
        return z3.UGE(left, right)

    @classmethod
    def Le(cls, left, right):
        return z3.ULE(left, right)

    @classmethod
    def Lt(cls, left, right):
        return z3.ULT(left, right)

    @classmethod
    def belongsToSort(cls, value):
        return z3.is_bv(value)

    @classmethod
    def isSMTValue(cls, value):
        return z3.is_bv_value(value)

    @classmethod
    def concreteValue(cls, value):
        return value.as_long()


class SMTArray(sort_base.SMTArrayBase):
    sort = z3.ArraySort

    @classmethod
    def Const(cls, name, from_sort, to_sort):
        assert issubclass(from_sort, sort_base.SMTSortBase) and issubclass(
            to_sort, sort_base.SMTSortBase
        )
        return z3.Const(name, z3.ArraySort(from_sort.sort, to_sort.sort))

    @classmethod
    def Eq(cls, left, right):
        return left == right

    @classmethod
    def Store(cls, array, index, value):
        return z3.Store(array, index, value)

    @classmethod
    def Select(cls, array, index):
        return z3.Select(array, index)

    @classmethod
    def belongsToSort(cls, value):
        return z3.is_array(value)

