from sym_decorators import forward_to_rfun, check_comparable_types
from sym_decorators import check_equality, check_self_and_other_have_same_type

from smt.sort_z3 import SMTInt, SMTBool
import copy


def is_symbolic(obj):
    return isinstance(obj, Symbolic)


def is_symbolic_bool(obj):
    return isinstance(obj, SymBool)


class Symbolic:

    _real_to_sym = {}

    @classmethod
    def get_supported_builtins(cls):
        if not cls._real_to_sym:
            cls._real_to_sym = {x.emulated_class: x for x in Symbolic.__subclasses__()}
        return cls._real_to_sym.keys()

    @classmethod
    def is_supported_builtin(cls, obj):
        supported_types = cls.get_supported_builtins()
        return obj in supported_types or type(obj) in supported_types

    @classmethod
    def get_symtypes_mapping(cls):
        if not cls._real_to_sym:
            cls._real_to_sym = {x.emulated_class: x for x in Symbolic.__subclasses__()}
        return copy.deepcopy(cls._real_to_sym)


class SymInt(Symbolic):

    emulated_class = int

    def __init__(self, engine, real=None):
        """
        :real: Either symbolic numeric variable in smt solver or real int value.
        """
        self.engine = engine
        self.smt = engine.smt
        if isinstance(real, SymInt):
            self.real = real.real  # Idempotent creation
        elif real is not None:
            self.real = real
        else:
            self.real = self.smt.Const(SMTInt)

    def __abs__(self):
        """
        x.__abs__() <==> abs(x)
        """
        return self if self > 0 else -self

    @forward_to_rfun()
    def __add__(self, other):
        """
        :types: other: int
        x.__add__(y) <==> x+y
        """
        return SymInt(self.engine, self.smt.Add(self.real, other.real))

    def __bool__(self):
        """
        x.__bool__() <==> x != 0
        """
        return bool(self != 0)

    def __deepcopy__(self, memo):
        """
        x.__deepcopy__() <==> copy.deepcopy(x)
        """
        return self

    @check_equality
    def __eq__(self, other):
        """
        :types: other: int
        x.__eq__(y) <==> x==y
        """
        other = other.real if isinstance(other, SymInt) else other
        return SymBool(self.engine, self.smt.Eq(self.real, other))

    @forward_to_rfun()
    def __floordiv__(self, other):
        """
        :types: other: int
        x.__floordiv__(y) <==> x//y
        """
        if other != 0:
            # Fix z3 bugs
            # 1) -1 == -1//2 != 1//-2  == 0
            # 2)  1 ==  1//2 != -1//-2 == 0
            if other < 0:
                return -self // -other
            else:
                return SymInt(self.engine, self.smt.Div(self.real, other.real))
        else:
            raise ZeroDivisionError("SymInt division or modulo by zero")

    @check_comparable_types
    def __ge__(self, other):
        """
        :types: other: int
        x.__ge__(y) <==> x>=y
        """
        other = other.real if isinstance(other, SymInt) else other
        return SymBool(self.engine, self.smt.Ge(self.real, other))

    @check_comparable_types
    def __gt__(self, other):
        """
        :types: other: int
        x.__gt__(y) <==> x>y
        """
        other = other.real if isinstance(other, SymInt) else other
        return SymBool(self.engine, self.smt.Gt(self.real, other))

    def __hash__(self):
        """
        x.__hash__() <==> hash(x)
        """
        return super().__hash__()

    @check_comparable_types
    def __le__(self, other):
        """
        :types: other: int
        x.__le__(y) <==> x<=y
        """
        other = other.real if isinstance(other, SymInt) else other
        return SymBool(self.engine, self.smt.Le(self.real, other))

    @check_comparable_types
    def __lt__(self, other):
        """
        :types: other: int
        x.__lt__(y) <==> x<y
        """
        other = other.real if isinstance(other, SymInt) else other
        return SymBool(self.engine, self.smt.Lt(self.real, other))

    @forward_to_rfun()
    def __mod__(self, other):
        """
        :types: other: int
        x.__mod__(y) <==> x%y
        """
        if other != 0:
            return SymInt(self.engine, self.smt.Mod(self.real, other.real))
        else:
            raise ZeroDivisionError("SymInt division or modulo by zero")

    @forward_to_rfun()
    def __mul__(self, other):
        """
        :types: other: int
        x.__mul__(y) <==> x*y
        """
        return SymInt(self.engine, self.smt.Mul(self.real, other.real))

    def __ne__(self, other):
        """
        :types: other: int
        x.__ne__(y) <==> x!=y
        """
        other = other.real if isinstance(other, SymInt) else other
        formula = self.smt.Not(self.smt.Eq(self.real, other))
        return SymBool(self.engine, formula)

    def __neg__(self):
        """
        x.__neg__() <==> -x
        """
        return SymInt(self.engine, self.smt.Neg(self.real))

    @check_self_and_other_have_same_type
    def __radd__(self, other):
        """
        :types: other: int
        x.__radd__(y) <==> y+x
        """
        return self.__add__(other)

    def __repr__(self):
        """
        x.__repr__() <==> repr(x)
        """
        if not isinstance(self.real, int):
            s = self.smt.simplify(self.real)
            if SMTInt.isSMTValue(s):
                s = SMTInt.concreteValue(s)
        return "%s" % s

    @check_self_and_other_have_same_type
    def __rfloordiv__(self, other):
        """
        :types: other: int
        x.__rfloordiv__(y) <==> y//x
        """
        if self != 0:
            # Fix z3 bugs
            # 1) -1 == -1//2 != 1//-2  == 0
            # 2)  1 ==  1//2 != -1//-2 == 0
            if self < 0:
                return -other // -self
            else:
                return SymInt(self.engine, self.smt.Div(other.real, self.real))
        else:
            raise ZeroDivisionError("SymInt division or modulo by zero")

    @check_self_and_other_have_same_type
    def __rmod__(self, other):
        """
        :types: other: int
        x.__rmod__(y) <==> y%x
        """
        if self != 0:
            return SymInt(self.engine, self.smt.Mod(other.real, self.real))
        else:
            raise ZeroDivisionError("SymInt division or modulo by zero")

    @check_self_and_other_have_same_type
    def __rmul__(self, other):
        """
        :types: other: int
        x.__rmul__(y) <==> y*x
        """
        return self.__mul__(other)

    @check_self_and_other_have_same_type
    def __rsub__(self, other):
        """
        :types: other: int
        x.__rsub__(y) <==> y-x
        """
        return SymInt(self.engine, self.smt.Sub(other.real, self.real))

    @forward_to_rfun()
    def __sub__(self, other):
        """
        :types: other: int
        x.__sub__(y) <==> x-y
        """
        return SymInt(self.engine, self.smt.Sub(self.real, other.real))

    @forward_to_rfun()
    def __truediv__(self, other):
        """
        :types: other: int
        x.__truediv__(y) <==> x/y
        """
        raise NotImplementedError("FloatProxy not implemented.")

    def concretize(self, model):
        if isinstance(self.real, int):
            result = self.real
        else:
            result = SMTInt.concreteValue(model.evaluate(self.real))
        return result


class SymBool(Symbolic):

    emulated_class = bool

    def __init__(self, engine, formula=None):
        self.engine = engine
        self.smt = engine.smt
        if formula is None:
            formula = self.smt.Const(SMTBool)
        self.formula = formula

    def __not__(self):
        return SymBool(self.engine, self.smt.Not(self.formula))

    def __bool__(self):
        if isinstance(self.formula, bool):
            return self.formula
        return self.engine.evaluate(self)

    def __nonzero__(self):
        return self.__bool__()

    def conditioned_value(self):
        """
        :returns: None if constrains haven't define a concrete value yet,
                  else returns that concrete value (True or False).
        It tries to obtain a bool value if possible. Without branching.
        """
        return self.engine.conditioned_value(self)

    def __repr__(self):
        ps = self.conditioned_value()
        return "%s" % (ps if ps is not None else str(self.formula))

    def __deepcopy__(self, memo):
        return self

    def concretize(self, model):
        if isinstance(self.formula, bool):
            result = self.formula
        else:
            result = SMTBool.concreteValue((model.evaluate(self.formula)))
        return result
