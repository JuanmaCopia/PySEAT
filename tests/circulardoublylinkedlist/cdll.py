class Node:
    # Instance attributes annotations (will be treated as symbolic)
    key: int
    next: "Node"
    prev: "Node"

    # Init params should be annotated also
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.prev = None


class CDLinkedList:
    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.head = None

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
        length = len(s)  # pragma: no mutate
        s.add(x)  # pragma: no mutate
        return len(s) != length  # pragma: no mutate

    def repok(self):  # pragma: no cover
        if self.head is None:  # pragma: no mutate
            return True  # pragma: no mutate
        if not self.head.prev or not self.head.next:  # pragma: no mutate
            return False  # pragma: no mutate
        if (  # pragma: no mutate
            self.head.next is self.head  # pragma: no mutate
            and self.head.prev is self.head  # pragma: no mutate
        ):  # pragma: no mutate
            return True  # pragma: no mutate
        if (  # pragma: no mutate
            self.head.next is self.head  # pragma: no mutate
            and self.head.prev is not self.head  # pragma: no mutate
        ):  # pragma: no mutate
            return False  # pragma: no mutate
        if (  # pragma: no mutate
            self.head.prev is self.head  # pragma: no mutate
            and self.head.next is not self.head  # pragma: no mutate
        ):  # pragma: no mutate
            return False  # pragma: no mutate

        visited = set()  # pragma: no mutate
        current = self.head  # pragma: no mutate
        next_node = current.next  # pragma: no mutate
        visited.add(current)  # pragma: no mutate

        while next_node is not self.head:  # pragma: no mutate
            if next_node.next is None or next_node.prev is None:  # pragma: no mutate
                return False  # pragma: no mutate
            if next_node.next is next_node:  # pragma: no mutate
                return False  # pragma: no mutate
            if (  # pragma: no mutate
                next_node.prev is not current  # pragma: no mutate
                or current.next is not next_node  # pragma: no mutate
            ):  # pragma: no mutate
                return False  # pragma: no mutate
            current = next_node  # pragma: no mutate
            if not CDLinkedList.do_add(visited, next_node):  # pragma: no mutate
                return False  # pragma: no mutate
            next_node = current.next  # pragma: no mutate
            if next_node is self.head:  # pragma: no mutate
                if current is not self.head.prev:  # pragma: no mutate
                    return False  # pragma: no mutate
        return True  # pragma: no mutate
