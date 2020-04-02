def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:
    def __init__(self, elem: int):
        self.elem = elem
        self.next = None

    def repok(self):
        return True


class LinkedList:
    def __init__(self, head=None):
        self.head = head

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
        if self.head:
            return self.head.__repr__()
        else:
            return "Empty"
