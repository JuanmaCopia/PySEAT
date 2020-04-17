def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:
    # Class attribues
    _engine = None

    # Instance attributes annotations (will be treated as symbolic)
    elem: int
    next: "Node"

    # Init params should be annotated also
    def __init__(self, elem: int):
        self.s_elem = elem
        self.s_next = None

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
            return " **node" + str(self._objid) + "(" + str(self.elem) + ")"

        if self.next is None:
            if hasattr(self, "_next_is_initialized"):
                if getattr(self, "_next_is_initialized"):
                    return (
                        " node" + str(self._objid) + "(" + str(self.elem) + ") -> None"
                    )
                else:
                    return (
                        " node" + str(self._objid) + "(" + str(self.elem) + ") -> CLOUD"
                    )
            return " node" + str(self._objid) + "(" + str(self.elem) + ") -> None"
        return " node" + str(self._objid) + "(" + str(self.elem) + ") ->"

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

    _engine = None

    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.s_head = None

    @property
    def head(self):
        return self._engine.lazy_initialization(self, "head")

    @head.setter
    def head(self, value):
        return self._engine.lazy_set_attr(self, "head", value)

    def repok(self):
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
            return "EmptyList"
        return self.head.__repr__()
