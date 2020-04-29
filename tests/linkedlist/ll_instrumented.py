def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:
    # Instance attributes annotations (will be treated as symbolic)
    elem: int
    next: "Node"

    # Init params should be annotated also
    def __init__(self, elem: int):
        self.elem = elem
        self.next = None

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
    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.head = None

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
            return "EmptyList"
        return self.head.__repr__()
