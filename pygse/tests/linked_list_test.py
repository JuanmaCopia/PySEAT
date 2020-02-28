import pygse.symbolic_execution_engine as see


class Node:

    _vector = [None]
    _is_user_defined = True
    _id = 0

    def __init__(self, elem: int):
        self.elem = elem
        self.next = None
        self._next_is_initialized = False
        self._marked = False
        self._concretized = False
        self._identifier = ""
        self._generated = False

    def _get_next(self):
        if not self._next_is_initialized and self in Node._vector:
            self._next_is_initialized = True
            self.next = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.rep_ok(), self)
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def to_str(self):
        self._marked = True
        if not self._next_is_initialized:
            return self._identifier + ":" + self.elem.__repr__() + " ->CLOUD"
        if self.next is None:
            return self._identifier + ":" + self.elem.__repr__() + " ->None"
        else:
            if self.next._marked:
                return (
                    self._identifier
                    + ":"
                    + self.elem.__repr__()
                    + " -> "
                    + self.next._identifier
                    + "("
                    + self.next.elem.__repr__()
                    + ")"
                    + "*"
                )
            return (
                self._identifier
                + ":"
                + self.elem.__repr__()
                + " -> "
                + self.next.to_str()
            )

    def __repr__(self):
        self.unmark_all()
        result = self.to_str()
        self.unmark_all()
        return result

    def unmark_all(self):
        aux = self
        while aux is not None and aux._marked:
            aux._marked = False
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
            if current._marked:
                return False
            current._marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
        return True

    def is_circular(self):
        self.unmark_all()
        current = self
        while current and not current._marked:
            current._marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
            if current is None:
                return False
        return True


class LinkedList:

    _vector = [None]
    _is_user_defined = True
    _id = 0

    def __init__(self, head: "Node" = None):
        self.head = head
        if head:
            self._head_is_initialized = True
        else:
            self._head_is_initialized = False
        self._concretized = False
        self._identifier = ""
        self._generated = False

    def _get_head(self):
        if not self._head_is_initialized and self in LinkedList._vector:
            self._head_is_initialized = True
            self.head = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.rep_ok(), self)
        return self.head

    def _set_head(self, value):
        self.head = value
        self._head_is_initialized = True

    def insert(self, elem: int):
        new_node = Node(elem)
        new_node._set_next(self.head)
        self._set_head(new_node)

    def size(self):
        current = self._get_head()
        count = 0
        while current:
            count += 1
            current = current._get_next()
        return count

    def search(self, elem: int):
        current = self._get_head()
        found = False
        while current and found is False:
            if current.get_elem() == elem:
                found = True
            else:
                current = current._get_next()
        if current is None:
            raise ValueError("elem not in list")
        return current

    def delete(self, elem: int):
        current = self._get_head()
        previous = None
        found = False
        while current and found is False:
            if current.get_elem() == elem:
                found = True
            else:
                previous = current
                current = current._get_next()
        if current is None:
            raise ValueError("elem not in list")
        if previous is None:
            self._set_head(current._get_next())
        else:
            previous._set_next(current._get_next())
        return self

    def unmark_all(self):
        aux = self.head
        while aux is not None and aux._marked:
            aux._marked = False
            aux = aux.next

    def rep_ok(self):
        return True

    def acyclic(self):
        self.unmark_all()
        current = self.head
        while current:
            if current._marked:
                return False
            current._marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
        return True

    def is_circular(self):
        self.unmark_all()
        current = self.head
        while current and not current._marked:
            current._marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
            if current is None:
                return False
        return True

    def swap_node(self):
        head = self._get_head()
        if head and head._get_next() is not None:
            if head.elem - head._get_next().elem > 0:
                t = head._get_next()
                head._set_next(t._get_next())
                t._set_next(head)
                return t
        return head

    def __repr__(self):
        if self.head:
            return self.head.__repr__()
        else:
            return "Empty"
