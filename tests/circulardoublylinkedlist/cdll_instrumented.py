

class Node:

    _vector = []
    _engine = None
    _id = 0

    # Instance attributes annotations (will be treated as symbolic)
    key: int
    next: "Node"
    prev: "Node"

    # Init params should be annotated also
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.prev = None

        self._key_is_initialized = True
        self._next_is_initialized = False
        self._prev_is_initialized = False

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_key(self):
        return self._engine.lazy_initialization(self, "key")

    def _set_key(self, value):
        return self._engine.lazy_set_attr(self, "key", value)

    def _get_next(self):
        return self._engine.lazy_initialization(self, "next")

    def _set_next(self, value):
        return self._engine.lazy_set_attr(self, "next", value)

    def _get_prev(self):
        return self._engine.lazy_initialization(self, "prev")

    def _set_prev(self, value):
        return self._engine.lazy_set_attr(self, "prev", value)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        # return " " + self._identifier + "(" + str(self.key) + ")"
        ps = None
        if self._prev_is_initialized:
            if self.prev:
                ps = self.prev._identifier
            else:
                ps = "None"
        else:
            ps = "CLOUD"

        ns = None
        if self._next_is_initialized:
            if self.next:
                ns = self.next._identifier
            else:
                ns = "None"
        else:
            ns = "CLOUD"

        return "(" + ps + " <- " + self._identifier + ": " + self.key.__repr__() + " -> " + ns + ") "

    def repok(self):
        return True

    def instrumented_repok(self):
        return True


class CDLinkedList:

    _vector = []
    _engine = None
    _id = 0

    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.head = None

        self._head_is_initialized = False

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_head(self):
        return self._engine.lazy_initialization(self, "head")

    def _set_head(self, value):
        return self._engine.lazy_set_attr(self, "head", value)

    def __repr__(self):
        if not self.head:
            return "Empty"
        if self.head.next is self.head and self.head.prev is self.head:
            return self.head.__repr__()
        str_rep = ""
        visited = set()
        visited.add(self.head)
        worklist = []
        worklist.append(self.head)
        while worklist:
            current = worklist.pop(0)
            str_rep += current.__repr__()
            if current.next:
                if not CDLinkedList.do_add(visited, current.next):
                    str_rep += "**" + current.next._identifier
                else:
                    worklist.append(current.next)
            else:
                if current._next_is_initialized:
                    str_rep += " None"
                else:
                    str_rep += " CLOUD"
        return str_rep

    # Insert node at the end of the circular doubly linked list
    def append(self, key: int):
        new_node = Node(key)

        # If there are no elements in the circular doubly linked list
        if self._get_head() is None:
            self._set_head(new_node)
            new_node._set_next(self._get_head())
            new_node._set_prev(self._get_head())

        # If there are more elements in the circular doubly linked list
        else:
            last_node = self._get_head()._get_prev()

            last_node._set_next(new_node)
            new_node._set_next(self._get_head())

            new_node._set_prev(last_node)
            self._get_head()._set_prev(new_node)

    # Insert node at the beginning of the circular doubly linked list
    def prepend(self, key):
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
    def insert_after_node(self, afterkey: int, key: int):
        current_node = self._get_head()
        while current_node:

            if current_node._get_next() == self._get_head() and current_node._get_key() == afterkey:
                # New node is to be appended to the list
                self.append(key)
                return

            # New node to be added in between nodes
            elif current_node._get_key() == afterkey:
                new_node = Node(key)
                next_node = current_node._get_next()

                # Update next pointers
                current_node._set_next(new_node)
                new_node._set_next(next_node)

                # Update prev pointers
                new_node._set_prev(current_node)

                # added
                # if next_node:
                #########
                next_node._set_prev(new_node)

                return
            else:
                if current_node._get_next() == self._get_head():
                    break
            current_node = current_node._get_next()

    # Insert before a specific node in the circular doubly linked list
    def insert_before_node(self, beforekey, key):
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

    def delete(self, deletekey):
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
    def do_add(s, x):
        length = len(s)
        s.add(x)
        return len(s) != length

    def repok(self):
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

    def instrumented_repok(self):
        if self._get_head() is None:
            return True
        if not self._get_head()._get_prev() or not self._get_head()._get_next():
            return False
        if self._get_head()._get_next() is self._get_head() and self._get_head()._get_prev() is self._get_head():
            return True

        if self._get_head()._get_next() is self._get_head() and self._get_head()._get_prev() is not self._get_head():
            return False
        if self._get_head()._get_prev() is self._get_head() and self._get_head()._get_next() is not self._get_head():
            return False

        visited = set()
        current = self._get_head()
        next_node = current._get_next()
        visited.add(current)

        while next_node is not self._get_head():
            if next_node._get_next() is None or next_node._get_prev() is None:
                return False
            if next_node._get_next() is next_node:
                return False
            if next_node._get_prev() is not current or current._get_next() is not next_node:
                return False
            current = next_node
            if not CDLinkedList.do_add(visited, next_node):
                return False
            next_node = current._get_next()
            if next_node is self._get_head():
                if current is not self._get_head()._get_prev():
                    return False
        return True
