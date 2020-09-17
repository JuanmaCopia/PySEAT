class Node:  # pragma: no cover
    # Instance attributes annotations (will be treated as symbolic)
    elem: int
    next: "Node"

    # Init params should be annotated also
    def __init__(self, elem: int):
        self.elem = elem
        self.next = None

    def __repr__(self):
        return "node(" + str(self.elem) + ")"


class LinkedList:
    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.head = None

    def swap_node(self):
        head = self.head
        if head and head.next is not None:
            if head.elem - head.next.elem > 0:
                t = head.next
                head.next = t.next
                t.next = head
                self.head = t
        return self.head

    def is_ordered(self):
        current = self.head
        while current and current.next:
            if current.elem >= current.next.elem:
                return False
            current = current.next
        return True

    def repok(self):  # pragma: no cover
        # acyclic
        visited = set()
        current = self.head
        while current:
            if current in visited:
                return False
            visited.add(current)
            current = current.next
        return True

    def __repr__(self):  # pragma: no cover
        if not self.head:
            return "EmptyList"

        str_repr = str(self.head.elem)
        current = self.head
        while current:
            current = current.next
            if current:
                str_repr += " -> {}".format(current.elem)
        return str_repr
