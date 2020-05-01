class Node:
    # Instance attributes annotations (will be treated as symbolic)
    data: int
    next: "Node"
    prev: "Node"

    # Init params should be annotated also
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

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

        return (ps + self.data.__repr__() + ns)

    def repok(self):
        return True


class DoublyLinkedList:
    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"
    tail: "Node"

    # Init params should be annotated also
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert 'value' at the front of the list
    def insert_at_front(self, value: int):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    #  insert value at the back of the linked list
    def insert_at_back(self, value: int):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # inserts value after key
    def insert_after(self, key: int, value: int):
        node = Node(value)

        # find the position of key
        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next

        if curr is None:
            print("Key not found")
            return

        if curr.next is None:
            curr.next = node
            node.prev = curr
            self.tail = node
        else:
            next_node = curr.next
            curr.next = node
            node.prev = curr
            node.next = next_node
            next_node.prev = node

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
    def remove(self, key: int):
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
            if curr.next is None:
                self.head = None
                self.tail = None
            else:
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
    def find(self, key: int):
        if self.is_empty():
            print("List is empty")
            return False

        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next

        if curr is None:
            return False

        return True

    def is_empty(self):
        return self.head is None

    @staticmethod
    def do_add(s, x):
        length = len(s)
        s.add(x)
        return len(s) != length

    def __repr__(self):
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
                    str_rep += "**" + str(current.next.__repr__())
                else:
                    worklist.append(current.next)
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
