
from symbolic_execution_engine import SEEngine

class Node:

    _vector = [None]
    _is_user_defined = True

    def __init__(self, elem):
        """
        :type: elem: int
        """
        self.elem = elem
        self.next = None
        self._next_is_initialized = False
        self.marked = False
        self.concretized = False

    def _get_next(self):
        if not self._next_is_initialized:
            self._next_is_initialized = True
            self.next = SEEngine.get_next_lazy_step(Node, Node._vector)
            #Verify.ignore_if(not self.precondition())
        return self.next
    
    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def to_str(self):
        self.marked = True
        if not self._next_is_initialized:
            return self.elem.__repr__() + "-> CLOUD"
        if self.next is None:
            return self.elem.__repr__() + "-> None"
        else:
            if self.next.marked:
                return self.elem.__repr__() + "->" + self.next.elem.__repr__() + "*"
            return self.elem.__repr__() + "->" + self.next.to_str()

    def __repr__(self):
        result = self.to_str()
        aux = self
        while aux is not None and aux.marked:
            aux.marked = False
            aux = aux.next
        return result

    def swap_node(self):
        if self._get_next() is not None:
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