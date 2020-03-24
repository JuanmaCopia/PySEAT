import sys
import pygse.symbolic_execution_engine as see
import pygse.proxy as proxy


class Node:

    _vector = [None]
    _is_user_defined = True
    _id = 0

    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

        self._data_is_initialized = data
        self._next_is_initialized = False
        self._prev_is_initialized = False

        self._concretized = False
        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1

    def _get_data(self):
        if not self._data_is_initialized:
            self.data = proxy.IntProxy()
        return self.data

    def _set_data(self, value):
        self.data = value
        self._data_is_initialized = True

    def _get_next(self):
        if not self._next_is_initialized and self in self._vector:
            self._next_is_initialized = True
            self.next = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.next

    def _set_next(self, value):
        self.next = value
        self._next_is_initialized = True

    def _get_prev(self):
        if not self._prev_is_initialized and self in self._vector:
            self._prev_is_initialized = True
            self.prev = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.prev

    def _set_prev(self, value):
        self.prev = value
        self._prev_is_initialized = True

    def conservative_repok(self):
        return True

    def repok(self):
        return True

    def __repr__(self):
        return self.data.__repr__()


class DoublyLinkedList:

    _vector = [None]
    _is_user_defined = True
    _id = 0

    def __init__(self, head: "Node" = None, tail: "Node" = None):
        self.head = head
        self.tail = tail

        self._head_is_initialized = False
        self._tail_is_initialized = False

        self._concretized = False
        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1

    def _get_head(self):
        if not self._head_is_initialized and self in self._vector:
            self._head_is_initialized = True
            self.head = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.head

    def _set_head(self, value):
        self.head = value
        self._head_is_initialized = True

    def _get_tail(self):
        if not self._tail_is_initialized and self in self._vector:
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

    def to_str(self):
        if self.is_empty():
            return "Empty"
        str_rep = ""
        visited = set()
        visited.add(self.head)
        worklist = []
        worklist.append(self.head)
        while worklist:
            current = worklist.pop(0)
            str_rep += current.data.__repr__() + " "
            if current.next:
                if not DoublyLinkedList.do_add(visited, current.next):
                    str_rep += current.data.__repr__() + "* "
                else:
                    worklist.append(current.next)

        str_rep += "\n"
        if not self.tail:
            return str_rep + "emptyTail"
        visited = set()
        visited.add(self.tail)
        worklist = []
        worklist.append(self.tail)
        while worklist:
            current = worklist.pop(0)
            str_rep += current.data.__repr__() + " "
            if current.prev:
                if not DoublyLinkedList.do_add(visited, current.prev):
                    str_rep += current.data.__repr__() + "* "
                else:
                    worklist.append(current.prev)
        return str_rep

    def __repr__(self):
        return self.to_str()

    def repok(self):
        if self.head is None and self.tail is None:
            return True
        if self.head is None and self.tail is not None:
            return False
        if self.head is not None and self.tail is None:
            return False
        if self.head.prev or self.tail.next:
            return False

        visited = set()
        visited.add(self.head)
        tail_added = False

        current = self.head
        next_node = current.next

        while next_node:
            if next_node.prev is not current:
                return False
            if next_node is self.tail and tail_added:
                return False
            else:
                tail_added = True
            if not DoublyLinkedList.do_add(visited, next_node):
                return False
            current = next_node
            next_node = next_node.next

        if not tail_added:
            return False
        return True

    def conservative_repok(self):
        if self.head is None and self.tail is None:
            return True
        if self.head is None and self.tail is not None:
            return False
        if self.head is not None and self.tail is None:
            return False
        if not self.head._prev_is_initialized:
            return True
        if not self.tail._next_is_initialized:
            return True
        if self.head.prev or self.tail.next:
            return False

        visited = set()
        visited.add(self.head)
        tail_added = False

        current = self.head
        if not current._next_is_initialized:
            return True
        next_node = current.next

        while next_node:
            if not current._prev_is_initialized:
                return True
            if next_node.prev is not current:
                return False
            if next_node is self.tail and tail_added:
                return False
            else:
                tail_added = True
            if not DoublyLinkedList.do_add(visited, next_node):
                return False
            current = next_node
            if not next_node._next_is_initialized:
                return True
            next_node = next_node.next

        if not tail_added:
            return False
        return True

    def instrumented_repok(self):
        if self._get_head() is None and self._get_tail() is None:
            return True
        if self._get_head() is None and self._get_tail() is not None:
            return False
        if self._get_head() is not None and self._get_tail() is None:
            return False
        if self._get_head()._get_prev() or self._get_tail()._get_next():
            return False

        visited = set()
        visited.add(self._get_head())
        tail_added = False

        current = self._get_head()
        next_node = current._get_next()

        while next_node:
            if next_node._get_prev() is not current:
                return False
            if next_node is self._get_tail() and tail_added:
                return False
            else:
                tail_added = True
            if not DoublyLinkedList.do_add(visited, next_node):
                return False
            current = next_node
            next_node = next_node._get_next()

        if not tail_added:
            return False
        return True
