def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:
    # Class attribues
    _vector = []
    _engine = None
    _id = 0

    # Instance attributes annotations (will be treated as symbolic)
    elem: int
    next: "Node"

    # Init params should be annotated also
    def __init__(self, elem: int):
        self.s_elem = elem
        self.s_next = None
        # Instrumentation instance attributes
        self._next_is_initialized = False
        self._elem_is_initialized = True

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    @property
    def elem(self):
        return self._engine.lazy_initialization(self, "elem")

    @elem.setter
    def elem(self, value):
        return self._engine.lazy_set_attr(self, "elem", value)

    @property
    def next(self):
        return self._engine.lazy_initialization(self, "next")

    @next.setter
    def next(self, value):
        return self._engine.lazy_set_attr(self, "next", value)

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

    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.s_head = None
        self._head_is_initialized = False

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    @property
    def head(self):
        return self._engine.lazy_initialization(self, "head")

    @head.setter
    def head(self, value):
        return self._engine.lazy_set_attr(self, "head", value)

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

    def swap_node(self):
        head = self.head
        if head and head.next is not None:
            if head.elem - head.next.elem > 0:
                t = head.next
                head.next = t.next
                t.next = head
                self.head = t
        return self.head

    def __repr__(self):
        if not self.head:
            return "Empty"
        return self.head.__repr__()
