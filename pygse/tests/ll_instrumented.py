def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:

    _vector = []
    _engine = None
    _id = 0

    def __init__(self, elem: int):
        self.elem = elem
        self.next = None
        # Instrumentation instance attributes
        self._next_is_initialized = False
        self._elem_is_initialized = True

        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_elem(self):
        if not self._elem_is_initialized:
            self._elem_is_initialized = True
            self.elem = self._engine.sym_int()
        return self.elem

    def _set_elem(self, value):
        self.elem = value
        self._elem_is_initialized = True

    def _get_next(self):
        if not self._next_is_initialized and self._engine.is_tracked(self):
            self._next_is_initialized = True
            self.next = self._engine.get_next_lazy_step(Node, Node._vector)
            self._engine.save_lazy_step(Node)
            self._engine.ignore_if(not self.conservative_repok(), self)
        else:
            self._engine.check_recursion_limit(self.next)
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def swap_node(self):
        if self._get_next() is not None:
            if self._get_elem() - self._get_next()._get_elem() > 0:
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

    def conservative_repok(self):
        return True

    def repok(self):
        return True

    def to_str(self, visited=False):
        if visited:
            return " **" + self._identifier + "(" + str(self.elem) + ")"
        if self._next_is_initialized:
            if self.next is None:
                return " " + self._identifier + "(" + str(self.elem) + ") -> None"
            else:
                return " " + self._identifier + "(" + str(self.elem) + ") ->"
        else:
            return " " + self._identifier + "(" + str(self.elem) + ") -> CLOUD"

    def __repr__(self):
        str_rep = ""
        visited = set()
        visited.add(self)
        worklist = []
        worklist.append(self)
        while worklist:
            current = worklist.pop(0)
            str_rep += current.to_str()

            if current.next:
                if not do_add(visited, current.next):
                    str_rep += current.next.to_str(True)
                else:
                    worklist.append(current.next)
        return str_rep


class LinkedList:

    _vector = []
    _engine = None
    _id = 0

    def __init__(self, head: "Node" = None):
        self.head = head

        self._head_is_initialized = False

        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_head(self):
        if not self._head_is_initialized and self._engine.is_tracked(self):
            self._head_is_initialized = True
            self.head = self._engine.get_next_lazy_step(Node, Node._vector)
            self._engine.save_lazy_step(Node)
            self._engine.ignore_if(not self.conservative_repok(), self)
        else:
            self._engine.check_recursion_limit(self.head)
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

    def repok(self):
        return self.acyclic()

    def acyclic(self):
        if self.head is None:
            return True
        visited = set()
        visited.add(self.head)
        current = self.head
        while current.next:
            if not do_add(visited, current.next):
                return False
            current = current.next
        return True

    def conservative_repok(self):
        return self.conservative_acyclic()

    def conservative_acyclic(self):
        if not self._head_is_initialized:
            return True
        if self.head is None:
            return True
        visited = set()
        visited.add(self.head)
        current = self.head

        if not current._next_is_initialized:
            return True
        while current.next:
            if not do_add(visited, current.next):
                return False
            current = current.next
            if not current._next_is_initialized:
                return True
        return True

    def instrumented_repok(self):
        return self.instrumented_acyclic()

    def instrumented_acyclic(self):
        if self._get_head() is None:
            return True
        visited = set()
        visited.add(self._get_head())
        current = self._get_head()
        while current._get_next():
            if not do_add(visited, current._get_next()):
                return False
            current = current._get_next()
        return True

    def swap_node(self):
        head = self._get_head()
        if head and head._get_next() is not None:
            if head._get_elem() - head._get_next()._get_elem() > 0:
                t = head._get_next()
                head._set_next(t._get_next())
                t._set_next(head)
                self._set_head(t)
        return self._get_head()

    def __repr__(self):
        if not self.head:
            return "Empty"
        return self.head.__repr__()
