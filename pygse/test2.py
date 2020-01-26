from symbolic_execution_engine import SEEngine

class X:

    _vector = [None]
    _is_user_defined = True
    _n = 0

    def __init__(self, data: int, nxt: "X"):
        self.data = data
        self.next = nxt
        self._next_is_initialized = False
        self.marked = False
        self.concretized = False

    def __repr__(self):
        r = "X" + str(X._n) + "=" + self.data.__repr__() + "->X"
        return r

    def rep_ok(self):
        return True
class A:

    _vector = [None]
    _is_user_defined = True
    _n = 0

    def __init__(self, data: int, x: "X", nxt: "A"):
        self.data = data
        self.next = nxt
        self.marked = False
        self._next_is_initialized = False
        self._x_is_initialized = False
        self.marked2 = False
        self.concretized = False

    def _get_next(self):
        if not self._next_is_initialized:
            self._next_is_initialized = True
            self.next = SEEngine.get_next_lazy_step(A, A._vector)
            # Verify.ignore_if(not self.precondition())
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def to_str(self):
        self.marked = True
        if not self._next_is_initialized:
            return self.data.__repr__() + "-> CLOUD"
        if self.next is None:
            return self.data.__repr__() + "-> None"
        else:
            if self.next.marked:
                return self.data.__repr__() + "->" + self.next.data.__repr__() + "*"
            return self.data.__repr__() + "->" + self.next.to_str()

    def __repr__(self):
        result = self.to_str()
        aux = self
        while aux is not None and aux.marked:
            aux.marked = False
            aux = aux.next
        return result

    def rep_ok(self):
        return True

class B:

    _vector = [None]
    _is_user_defined = True
    _n = 0

    def __init__(self, data: int, a: "A", nxt: "B"):
        self.data = data
        self.a = a
        self.next = nxt
        self._next_is_initialized = False
        self._a_is_initialized = False
        self.marked = False
        self.marked2 = False
        self.concretized = False

    def _get_next(self):
        if not self._next_is_initialized:
            self._next_is_initialized = True
            self.next = SEEngine.get_next_lazy_step(B, B._vector)
            # Verify.ignore_if(not self.precondition())
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def to_str(self):
        self.marked = True
        if not self._next_is_initialized:
            return self.data.__repr__() + "-> CLOUD"
        if self.next is None:
            return self.data.__repr__() + "-> None"
        else:
            if self.next.marked:
                return self.data.__repr__() + "->" + self.next.data.__repr__() + "*"
            return self.data.__repr__() + "->" + self.next.to_str()

    def __repr__(self):
        result = self.to_str()
        aux = self
        while aux is not None and aux.marked:
            aux.marked = False
            aux = aux.next
        return result

    def rep_ok(self):
        return True

class C:

    _vector = [None]
    _is_user_defined = True
    _n = 0

    def __init__(self, a: "A", b: "B", nxt: "C"):
        self.a = a
        self.b = b
        self.next = nxt
        self._a_is_initialized = False
        self._b_is_initialized = False
        self._next_is_initialized = False
        self.marked = False
        self.concretized = False

    def _get_next(self):
        if not self._next_is_initialized:
            self._next_is_initialized = True
            self.next = SEEngine.get_next_lazy_step(C, C._vector)
            # Verify.ignore_if(not self.precondition())
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def _get_a(self):
        if not self._a_is_initialized:
            self._a_is_initialized = True
            self.a = SEEngine.get_next_lazy_step(A, A._vector)
            # Verify.ignore_if(not self.precondition())
        return self.a

    def _set_a(self, value):
        self.a = value
        self._a_is_initialized = True

    def _get_b(self):
        if not self._b_is_initialized:
            self._b_is_initialized = True
            self.b = SEEngine.get_next_lazy_step(B, B._vector)
            # Verify.ignore_if(not self.precondition())
        return self.b

    def _set_b(self, value):
        self.b = value
        self._b_is_initialized = True

    def __repr__(self):
        r = "A:  " + self.a.__repr__() + "\n" + "         B:  " + self.b.__repr__()
        return r

    def rep_ok(self):
        return True

    def test_method(self):
        suma_A = 0
        current = self._get_a()
        while current and not current.marked2:
            current.marked2 = True
            suma_A += current.data
            current = current._get_next()

        suma_B = 0
        current = self._get_b()
        while current and not current.marked2:
            current.marked2 = True
            suma_B += current.data
            current = current._get_next()
        return suma_A > suma_B

