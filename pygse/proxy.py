# coding:utf-8
from pygse.proxy_decorators import forward_to_rfun, check_comparable_types
from pygse.proxy_decorators import check_equality, check_self_and_other_have_same_type
# Import objets for the SMT Solver
from pygse.smt.smt import SMT
from pygse.smt.sort_z3 import SMTInt, SMTBool, SMTChar, SMTArray
from pygse.smt.solver_z3 import SMTSolver

import pygse.symbolic_execution_engine as see

# Gideline para crear/modificar proxys:
#   *) Si queremos saber si una variable tiene algo preguntar si es != None.
#      Comparaciones con valores o usar como booleanos a variables puede
#      producir branching no deseado.
#   *) La implementación de __str__ y __repr__ de los Proxy no debe generar
#      branching. Facilita el debugeo y evita caminos generalmente innecesarios.
#   *) No utilizar la función `len` ya que python hace checkeo de tipos.
#   *) Los métodos _concretize deben devolver un objeto concreto "equivalente".
#   *) Cada proxy object DEBE tener un atributo de clase `emulated_class` que
#      tenga como valor la clase que el proxy object emula. ej.
#      ProxyInt.emulated_class = int, ProxyList.emulated_class = list

smt = SMT((SMTInt, SMTBool, SMTChar, SMTArray), SMTSolver)


class ConcolicExecutionError(Exception):
    pass


class MaxDepthError(ConcolicExecutionError):
    def __init__(self):
        super(MaxDepthError, self).__init__("Max depth reached")


def is_symbolic(obj):
    return isinstance(obj, ProxyObject)


def is_symbolic_bool(obj):
    return isinstance(obj, BoolProxy)


def is_user_defined(obj):
    return hasattr(obj, "_is_user_defined")


class ProxyObject(object):
    """
    Base class of a ProxyObject that can become any type by inheriting it.
    """


class IntProxy(ProxyObject):
    """
    Int Proxy object for variables that behave like ints.
    """
    emulated_class = int

    def __init__(self, real=None):
        """
        :real: Either symbolic numeric variable in smt solver or real int value.
        """
        if isinstance(real, IntProxy):
            self.real = real.real  # Idempotent creation
        elif real != None:
            self.real = real
        else:
            self.real = smt.Const(SMTInt)

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
        return IntProxy(smt.Add(self.real, other.real))

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
        other = other.real if isinstance(other, IntProxy) else other
        return BoolProxy(smt.Eq(self.real, other))

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
                return IntProxy(smt.Div(self.real, other.real))
        else:
            raise ZeroDivisionError("IntProxy division or modulo by zero")

    @check_comparable_types
    def __ge__(self, other):
        """
        :types: other: int
        x.__ge__(y) <==> x>=y
        """
        other = other.real if isinstance(other, IntProxy) else other
        return BoolProxy(smt.Ge(self.real, other))

    @check_comparable_types
    def __gt__(self, other):
        """
        :types: other: int
        x.__gt__(y) <==> x>y
        """
        other = other.real if isinstance(other, IntProxy) else other
        return BoolProxy(smt.Gt(self.real, other))

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
        other = other.real if isinstance(other, IntProxy) else other
        return BoolProxy(smt.Le(self.real, other))

    @check_comparable_types
    def __lt__(self, other):
        """
        :types: other: int
        x.__lt__(y) <==> x<y
        """
        other = other.real if isinstance(other, IntProxy) else other
        return BoolProxy(smt.Lt(self.real, other))

    @forward_to_rfun()
    def __mod__(self, other):
        """
        :types: other: int
        x.__mod__(y) <==> x%y
        """
        if other != 0:
            return IntProxy(smt.Mod(self.real, other.real))
        else:
            raise ZeroDivisionError("IntProxy division or modulo by zero")

    @forward_to_rfun()
    def __mul__(self, other):
        """
        :types: other: int
        x.__mul__(y) <==> x*y
        """
        return IntProxy(smt.Mul(self.real, other.real))

    def __ne__(self, other):
        """
        :types: other: int
        x.__ne__(y) <==> x!=y
        """
        other = other.real if isinstance(other, IntProxy) else other
        return BoolProxy(smt.Not(smt.Eq(self.real, other)))

    def __neg__(self):
        """
        x.__neg__() <==> -x
        """
        return IntProxy(smt.Neg(self.real))

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
            s = smt.simplify(self.real)
            if SMTInt.isSMTValue(s):
                s = SMTInt.concreteValue(s)
        return "IntProxy(%s)" % s

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
                return IntProxy(smt.Div(other.real, self.real))
        else:
            raise ZeroDivisionError("IntProxy division or modulo by zero")

    @check_self_and_other_have_same_type
    def __rmod__(self, other):
        """
        :types: other: int
        x.__rmod__(y) <==> y%x
        """
        if self != 0:
            return IntProxy(smt.Mod(other.real, self.real))
        else:
            raise ZeroDivisionError("IntProxy division or modulo by zero")

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
        return IntProxy(smt.Sub(other.real, self.real))

    @forward_to_rfun()
    def __sub__(self, other):
        """
        :types: other: int
        x.__sub__(y) <==> x-y
        """
        return IntProxy(smt.Sub(self.real, other.real))

    @forward_to_rfun()
    def __truediv__(self, other):
        """
        :types: other: int
        x.__truediv__(y) <==> x/y
        """
        raise NotImplementedError("FloatProxy not implemented.")

    def _concretize(self, model):
        if isinstance(self.real, int):
            result = self.real
        else:
            result = SMTInt.concreteValue(model.evaluate(self.real))
        return result


class BoolProxy(ProxyObject):
    """
    Bool Proxy object for variables that behave like bools.
    """
    emulated_class = bool

    def __init__(self, formula=None):
        if formula is None:
            formula = smt.Const(SMTBool)
        self.formula = formula

    def __not__(self):
        return BoolProxy(smt.Not(self.formula))

    def __bool__(self):
        if isinstance(self.formula, bool):
            return self.formula
        # If self.formula isn't a builtin bool we have to solve it
        return see.SEEngine.evaluate(self)

    def __nonzero__(self):
        return self.__bool__()

    def _get_partial_solve(self):
        """
        :returns: None if constrains haven't define a concrete value yet,
                  else returns that concrete value (True or False).
        It tries to obtain a bool value if possible. Without branching.
        """
        return see.SEEngine._get_partial_solve(self)

    def __repr__(self):
        ps = self._get_partial_solve()
        return "BoolProxy(%s)" % (ps if ps is not None else str(self.formula))

    def __deepcopy__(self, memo):
        return self

    def _concretize(self, model):
        if isinstance(self.formula, bool):
            result = self.formula
        else:
            result = SMTBool.concreteValue((model.evaluate(self.formula)))
        return result
