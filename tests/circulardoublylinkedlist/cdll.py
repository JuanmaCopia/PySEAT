class Node:  # pragma: no cover
    # Instance attributes annotations (will be treated as symbolic)
    key: int
    next: "Node"
    prev: "Node"

    # Init params should be annotated also
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        ps = None

        if self.prev:
            ps = " <- "
        else:
            ps = "None <- "

        ns = None
        if self.next:
            ns = " -> "
        else:
            ns = " -> None"

        return ps + self.key.__repr__() + ns


class CDLinkedList:
    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.head = None

    def __repr__(self):  # pragma: no cover
        if not self.head:
            return "<Empty list>"
        str_rep = ""
        visited = set()
        visited.add(self.head)
        worklist = []
        worklist.append(self.head)
        while worklist:
            current = worklist.pop(0)
            str_rep += current.__repr__()
            if current.next:
                if not self.do_add(visited, current.next):
                    str_rep += "**"
                else:
                    worklist.append(current.next)
        return str_rep

    # Insert node at the end of the circular doubly linked list
    def append(self, key: int):
        new_node = Node(key)

        # If there are no elements in the circular doubly linked list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head

        # If there are more elements in the circular doubly linked list
        else:
            last_node = self.head.prev

            last_node.next = new_node
            new_node.next = self.head

            new_node.prev = last_node
            self.head.prev = new_node

    # Insert node at the beginning of the circular doubly linked list
    def prepend(self, key: int):
        new_node = Node(key)

        # If there are no elements in the circular doubly linked list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head

        else:

            # If not an empty circular doubly linked list - the next and previous
            # pointers for the head, new node and last node need to be updated

            last_node = self.head.prev

            # New node pointers updated
            new_node.next = self.head
            new_node.prev = last_node

            # head , last node pointers updated
            self.head.prev = new_node
            last_node.next = new_node

            # Update new head
            self.head = new_node

    # Insert after a specific node in the circular doubly linked list
    def insert_after(self, afterkey: int, key: int):
        current_node = self.head
        while current_node:

            if current_node.next == self.head and current_node.key == afterkey:
                # New node is to be appended to the list
                self.append(key)
                return

            # New node to be added in between nodes
            elif current_node.key == afterkey:
                new_node = Node(key)
                next_node = current_node.next

                # Update next pointers
                current_node.next = new_node
                new_node.next = next_node

                # Update prev pointers
                new_node.prev = current_node
                next_node.prev = new_node

                return
            else:
                if current_node.next == self.head:
                    break
            current_node = current_node.next

    # Insert before a specific node in the circular doubly linked list
    def insert_before(self, beforekey: int, key: int):
        current_node = self.head
        while current_node:

            if current_node == self.head and current_node.key == beforekey:
                # New node is to be prepended to the list
                self.prepend(key)
                return
            # New node to be added in between nodes
            elif current_node.key == beforekey:
                new_node = Node(key)
                prev_node = current_node.prev

                # Update next pointers
                prev_node.next = new_node
                new_node.next = current_node

                # Update prev pointers
                new_node.prev = prev_node
                current_node.prev = new_node
                return
            else:
                if current_node.next == self.head:
                    break
            current_node = current_node.next

    def delete(self, deletekey: int):
        current_node = self.head
        while current_node:

            # The node to be deleted is the head node
            if current_node.key == deletekey and current_node == self.head:

                # Case 1 - The head is the only element in circular doubly
                # linked list
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                    return

                # Case 2 - There are more elements in the circular doubly
                # linked list
                else:

                    last_node = self.head.prev
                    next_node = self.head.next

                    last_node.next = next_node
                    next_node.prev = last_node

                    self.head = next_node
                    current_node = None

                    return

            # Case 3 & 4 - Node to be deleted in between nodes or last node
            elif current_node.key == deletekey:
                prev_node = current_node.prev
                next_node = current_node.next

                prev_node.next = next_node
                next_node.prev = prev_node

                current_node = None
                return

            else:
                if current_node.next == self.head:
                    break

            current_node = current_node.next

    @staticmethod
    def do_add(s, x):  # pragma: no cover
        length = len(s)
        s.add(x)
        return len(s) != length

    def repok(self):  # pragma: no cover
        if self.head is None:
            return True
        if not self.head.prev or not self.head.next:
            return False
        if self.head.next is self.head and self.head.prev is self.head:
            return True
        if self.head.next is self.head and self.head.prev is not self.head:
            return False
        if self.head.prev is self.head and self.head.next is not self.head:
            return False

        visited = set()
        current = self.head
        next_node = current.next
        visited.add(current)

        while next_node is not self.head:
            if next_node.next is None or next_node.prev is None:
                return False
            if next_node.next is next_node:
                return False
            if next_node.prev is not current or current.next is not next_node:
                return False
            current = next_node
            if not CDLinkedList.do_add(visited, next_node):
                return False
            next_node = current.next
            if next_node is self.head:
                if current is not self.head.prev:
                    return False
        return True
