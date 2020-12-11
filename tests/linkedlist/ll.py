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

    def prepend(self, elem: int):
        new_node = Node(elem)
        new_node.next = self.head
        self.head = new_node

    def append(self, elem: int):
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, elem: int):
        if self.head:
            if self.head.elem == elem:
                self.head = self.head.next
            else:
                current = self.head
                while current.next and current.next.elem != elem:
                    current = current.next
                if current.next:
                    current.next = current.next.next

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
