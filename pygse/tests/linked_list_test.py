import pygse.symbolic_execution_engine as see


class Node:

    _vector = [None]
    _is_user_defined = True

    def __init__(self, elem: int = None, next: "Node" = None):
        self.elem = elem
        self.next = next
        self._next_is_initialized = False
        self.marked = False
        self.concretized = False

    def get_elem(self):
        return self.elem

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

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
        self.marked = True
        if not self._next_is_initialized:
            return self.elem.__repr__() + "->CLOUD"
        if self.next is None:
            return self.elem.__repr__() + "->None"
        else:
            if self.next.marked:
                return self.elem.__repr__() + "->" + self.next.elem.__repr__() + "*"
            return self.elem.__repr__() + "->" + self.next.to_str()

    def unmark_all(self):
        aux = self
        while aux is not None and aux.marked:
            aux.marked = False
            aux = aux.next

    def __repr__(self):
        self.unmark_all()
        result = self.to_str()
        self.unmark_all()
        return result

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

    def rep_ok(self):
        return self.acyclic()


class LinkedList:

    _vector = [None]
    _is_user_defined = True

    def __init__(self, head: "Node" = None):
        self.head = head
        self._head_is_initialized = False
        self.concretized = False

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
        while aux is not None and aux.marked:
            aux.marked = False
            aux = aux.next

    def rep_ok(self):
        return self.acyclic()

    def acyclic(self):
        self.unmark_all()
        current = self.head
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
        current = self.head
        while current and not current.marked:
            current.marked = True
            # This make the repok conservative
            if not current._next_is_initialized:
                return True
            current = current.next
            if current is None:
                return False
        return True

    def __repr__(self):
        if self.head:
            return self.head.__repr__()
        else:
            return "Empty"
