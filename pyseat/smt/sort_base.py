"""
All this base clases encapsulate and standarize the smt operations and
formulas with sorts.
"""

class SMTSortBase(object):
    @classmethod
    def Const(cls, name, *args, ctx=None, **kwargs): raise NotImplementedError
    @classmethod
    def Eq(cls, left, right): raise NotImplementedError
    @classmethod
    def belongsToSort(cls, value):
        """
        Returns true iff `value` belongs to this sort.
        """
        raise NotImplementedError
    @classmethod
    def isSMTValue(cls, value):
        """
        Returns true iff `value` represents a concrete constant of this sort.
        """
        raise NotImplementedError
    @classmethod
    def concreteValue(cls, value):
        """
        If isSMTValue(value), we can ask for a concrete representation of
        `value`.
        """
        raise NotImplementedError


class SMTIntBase(SMTSortBase):
    """
    Abstract class to implement expressions of int type
    """
    name = "int"
    # Operations
    @classmethod
    def Add(cls, left, right): raise NotImplementedError
    @classmethod
    def Sub(cls, left, right): raise NotImplementedError
    @classmethod
    def Mul(cls, left, right): raise NotImplementedError
    @classmethod
    def Div(cls, left, right): raise NotImplementedError
    @classmethod
    def Neg(cls, left): raise NotImplementedError
    @classmethod
    def Mod(cls, left, right): raise NotImplementedError
    # Relations
    @classmethod
    def Gt(cls, left, right): raise NotImplementedError
    @classmethod
    def Ge(cls, left, right): raise NotImplementedError
    @classmethod
    def Le(cls, left, right): raise NotImplementedError
    @classmethod
    def Lt(cls, left, right): raise NotImplementedError


class SMTBoolBase(SMTSortBase):
    """
    Abstract class to implement expressions of bool type
    """
    name = "bool"
    @classmethod
    def And(cls, left, right): raise NotImplementedError
    @classmethod
    def Or(cls, left, right): raise NotImplementedError
    @classmethod
    def Xor(cls, left, right): raise NotImplementedError
    @classmethod
    def Not(cls): raise NotImplementedError


class SMTCharBase(SMTSortBase):
    """
    Abstract class to implement the char sort
    """
    name = "char"
    @classmethod
    def Gt(cls, left, right): raise NotImplementedError
    @classmethod
    def Ge(cls, left, right): raise NotImplementedError
    @classmethod
    def Le(cls, left, right): raise NotImplementedError
    @classmethod
    def Lt(cls, left, right): raise NotImplementedError

class SMTArrayBase(SMTSortBase):
    """
    Abstract class to implement the array sort
    """
    name = "array"
    @classmethod
    def Store(cls, index, value): raise NotImplementedError
    @classmethod
    def Select(cls, index): raise NotImplementedError