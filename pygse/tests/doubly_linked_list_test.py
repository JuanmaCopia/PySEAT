import pygse.symbolic_execution_engine as see
import pygse.proxy as proxy
import sys


class Node:

    _vector = []
    _is_user_defined = True
    _id = 0

    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

        self._data_is_initialized = True
        self._next_is_initialized = False
        self._prev_is_initialized = False

        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_data(self):
        if not self._data_is_initialized:
            self._key_is_initialized = True
            self.data = proxy.IntProxy()
        return self.data

    def _set_data(self, value):
        self.data = value
        self._data_is_initialized = True

    def _get_next(self):
        see.SEEngine.check_recursion_limit(self)
        if not self._next_is_initialized and see.SEEngine.is_tracked(self):
            self._next_is_initialized = True
            self.next = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def _get_prev(self):
        see.SEEngine.check_recursion_limit(self)
        if not self._prev_is_initialized and see.SEEngine.is_tracked(self):
            self._prev_is_initialized = True
            self.prev = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.prev

    def _set_prev(self, value):
        self.prev = value
        self._prev_is_initialized = True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        # return " " + self._identifier + "(" + str(self.key) + ")"
        ps = None
        if self._prev_is_initialized:
            if self.prev:
                ps = self.prev._identifier[-1]
            else:
                ps = "None"
        else:
            ps = "CLOUD"

        ns = None
        if self._next_is_initialized:
            if self.next:
                ns = self.next._identifier[-1]
            else:
                ns = "None"
        else:
            ns = "CLOUD"

        return "(" + ps + " <- " + self._identifier + ": " + self.data.__repr__() + " -> " + ns + ") "

    def repok(self):
        return True

    def conservative_repok(self):
        return True

    def instrumented_repok(self):
        return True


class DoublyLinkedList:

    _vector = []
    _is_user_defined = True
    _id = 0

    def __init__(self, head: "Node" = None, tail: "Node" = None):
        self.head = head
        self.tail = tail

        self._head_is_initialized = False
        self._tail_is_initialized = False

        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_head(self):
        see.SEEngine.check_recursion_limit(self)
        if not self._head_is_initialized and see.SEEngine.is_tracked(self):
            self._head_is_initialized = True
            self.head = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.head

    def _set_head(self, value):
        self.head = value
        self._head_is_initialized = True

    def _get_tail(self):
        see.SEEngine.check_recursion_limit(self)
        if not self._tail_is_initialized and see.SEEngine.is_tracked(self):
            self._tail_is_initialized = True
            self.tail = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.tail

    def _set_tail(self, value):
        self.tail = value
        self._tail_is_initialized = True

    # Insert 'value' at the front of the list
    def insert_at_front(self, value: int):
        node = Node(value)
        if self.instrumented_is_empty():
            self._set_head(node)
            self._set_tail(node)
        else:
            node._set_next(self._get_head())
            self._get_head()._set_prev(node)
            self._set_head(node)

    #  insert value at the back of the linked list
    def insert_at_back(self, value: int):
        node = Node(value)
        if self.instrumented_is_empty():
            self._set_head(node)
            self._set_tail(node)
        else:
            self._get_tail()._set_next(node)
            node._set_prev(self._get_tail())
            self._set_tail(node)

    # inserts value after key
    def insert_after(self, key: int, value: int):
        node = Node(value)

        # find the position of key
        curr = self._get_head()
        while curr is not None and curr._get_data() != key:
            curr = curr._get_next()

        if curr is None:
            return

        if curr._get_next() is None:
            curr._set_next(node)
            node._set_prev(curr)
            self._set_tail(node)
        else:
            next_node = curr._get_next()
            curr._set_next(node)
            node._set_prev(curr)
            node._set_next(next_node)
            next_node._set_prev(node)

    # returns the data at first node
    def top_front(self):
        if self.is_empty():
            print("List is empty")
            return

        return self.head.data

    # returns the data at last node
    def top_back(self):
        if self.is_empty():
            print("List is empty")
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        return curr.data

    # removes the item at front of the linked list and return
    def pop_front(self):
        if self.is_empty():
            print("List is empty")
            return

        next_node = self.head.next
        if next_node is not None:
            next_node.prev = None
        item = self.head.data
        self.head = next_node
        return item

    # remove the item at the end of the list and return
    def pop_back(self):
        if self.is_empty():
            print("List is empty")
            return

        item = self.tail.data
        prev = self.tail.prev

        if prev is not None:
            prev.next = None

        self.tail.prev = None
        self.tail = prev

        return item

    # removes an item with value 'key'
    def remove(self, key):
        if self.is_empty():
            print("List is empty")
            return

        # find the position of the key
        curr = self.head

        while curr is not None and curr.data != key:
            curr = curr.next

        if curr is None:
            print("key not found")
            return

        # if curr is head, delete the head
        if curr.prev is None:
            self.pop_front()
        elif curr.next is None:  # if curr is last item
            self.pop_back()
        else:  # anywhere between first and last node
            next_node = curr.next
            prev_node = curr.prev

            prev_node.next = next_node
            next_node.prev = prev_node

            curr.next = None
            curr.prev = None
            curr = None

    # check if the key is in the list
    def find(self, key):
        if self.is_empty():
            print("List is empty")
            return False

        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next

        if curr is None:
            return False

        return True

    # check if the list is empty
    def instrumented_is_empty(self):
        return self._get_head() is None

    def is_empty(self):
        return self.head is None

    def print_reverse(self):
        if self.is_empty():
            print("Nothing to display")
        else:
            curr = self.tail
            while curr is not None:
                sys.stdout.write(str(curr.data) + " ")
                curr = curr.prev
            print("")

    # print all the items
    def printlist(self):
        if self.is_empty():
            print("Nothing to display")
        else:
            curr = self.head
            while curr is not None:
                sys.stdout.write(str(curr.data) + " ")
                curr = curr.next
            print("")

    @staticmethod
    def do_add(s, x):
        length = len(s)
        s.add(x)
        return len(s) != length

    def __repr__(self):
        if not self.head:
            return "Empty"
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
                    str_rep += "**" + current.next._identifier
                else:
                    worklist.append(current.next)
            else:
                if current._next_is_initialized:
                    str_rep += " None"
                else:
                    str_rep += " CLOUD"
        return str_rep

    def repok(self):
        if self.head is None and self.tail is None:
            return True
        if self.head is None or self.tail is None:
            return False
        if self.head.prev is not None or self.tail.next is not None:
            return False

        visited = set()
        visited.add(self.head)

        current = self.head
        next_node = current.next

        while next_node:
            if next_node.prev is not current:
                return False
            if not self.do_add(visited, next_node):
                return False
            current = next_node
            next_node = next_node.next

        if self.do_add(visited, self.tail):
            return False
        return True

    def conservative_repok(self):

        if not self._head_is_initialized or not self._tail_is_initialized:
            return True
        if not self.head._prev_is_initialized or not self.tail._next_is_initialized:
            return True

        if self.head is None and self.tail is None:
            return True
        if self.head is None or self.tail is None:
            return False
        if self.head.prev is not None or self.tail.next is not None:
            return False

        visited = set()
        visited.add(self.head)

        current = self.head
        next_node = current.next

        while next_node:

            if not next_node._prev_is_initialized:
                return True

            if next_node.prev is not current:
                return False
            if not self.do_add(visited, next_node):
                return False
            current = next_node

            if not next_node._next_is_initialized:
                return True

            next_node = next_node.next

        if self.do_add(visited, self.tail):
            return False
        return True

    def instrumented_repok(self):
        if self._get_head() is None and self._get_tail() is None:
            return True
        if self._get_head() is None or self._get_tail() is None:
            return False
        if self._get_head()._get_prev() is not None or self._get_tail()._get_next() is not None:
            return False

        visited = set()
        visited.add(self._get_head())

        current = self._get_head()
        next_node = current._get_next()

        while next_node:
            if next_node._get_prev() is not current:
                return False
            if not self.do_add(visited, next_node):
                return False
            current = next_node
            next_node = next_node._get_next()

        if self.do_add(visited, self._get_tail()):
            return False
        return True

