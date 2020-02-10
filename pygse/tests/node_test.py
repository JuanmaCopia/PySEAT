import pygse.symbolic_execution_engine as see


class Node:

    _vector = [None]
    _is_user_defined = True

    def __init__(self, elem: int):
        self.elem = elem
        self.next = None
        self._next_is_initialized = False
        self.marked = False
        self.concretized = False

    def _get_next(self):
        if not self._next_is_initialized and self in Node._vector:
            self._next_is_initialized = True
            self.next = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node, Node._vector)
            see.SEEngine.ignore_if(not self.rep_ok(), self)
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def to_str(self):
        self.marked = True
        if not self._next_is_initialized:
            return self.elem.__repr__() + "->CLOUD"
        if self.next is None:
            return self.elem.__repr__() + "->None"
        else:
            if self.next.marked:
                return self.elem.__repr__() + "->" + self.next.elem.__repr__() + "*"
            return self.elem.__repr__() + "->" + self.next.to_str()

    def __repr__(self):
        self.unmark_all()
        result = self.to_str()
        self.unmark_all()
        return result

    def unmark_all(self):
        aux = self
        while aux is not None and aux.marked:
            aux.marked = False
            aux = aux.next

    def swap_node(self):
        if self._get_next() is not None:
            if self.elem - self._get_next().elem > 0:
                t = self._get_next()
                self._set_next(t._get_next())
                t._set_next(self)
                return t
        return self

    def swap_node_with_garbage(self):
        if self._get_next() is not None:
            # Garbage
            x = Node(4)
            z = x._get_next()
            if z:
                z.unmark_all()
            # End garbage
            if self.elem - self._get_next().elem > 0:
                t = self._get_next()
                self._set_next(t._get_next())
                t._set_next(self)
                return t
        return self

    def is_sorted(self):
        current = self
        if current:
            nxt = current._get_next()
            while nxt:
                if nxt.elem <= current.elem:
                    return False
                current = nxt
                nxt = nxt._get_next()
            return True

    def rep_ok(self):
        return True

    def acyclic(self):
        self.unmark_all()
        current = self
        while current:
            if current.marked:
                return False
            current.marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
        return True

    def is_circular(self):
        self.unmark_all()
        current = self
        while current and not current.marked:
            current.marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
            if current is None:
                return False
        return True


def swapNodeFunc(head):
    """
    :type: head: Node
    """
    if head._get_next() != None:
        if head.elem - head.next.elem() > 0:
            t = head._get_next()
            head._set_next(t._get_next())
            t._set_next(head)
            return t
    return head
