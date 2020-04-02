import sys


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    # Insert 'value' at the front of the list
    def insert_at_front(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    #  insert value at the back of the linked list
    def insert_at_back(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # inserts value after key
    def insert_after(self, key, value):
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
        return str_rep

    def __repr__(self):
        return self.to_str()

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



def insert_after_test1():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> 4) (3 <- node4: 1 -> 5) (4 <- node5: 1 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> 4) (CLOUD <- node4: 1 -> 5) (CLOUD <- node5: 1 -> None)  None
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(1)
    node4.data = 1
    node5 = Node(1)
    node5.data = 1
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node5)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.next is None
    print('Test1: OK')


def insert_after_test2():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> 4) (3 <- node4: 1 -> 5) (4 <- node5: 0 -> 6) (5 <- node6: 0 -> 1) (6 <- node91: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> 4) (CLOUD <- node4: 1 -> 5) (CLOUD <- node5: 0 -> 0) (5 <- node0: 0 -> 6) (0 <- node6: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(1)
    node4.data = 1
    node5 = Node(0)
    node5.data = 0
    node6 = Node(0)
    node6.data = 0
    node91 = Node(0)
    node91.data = 0
    node91.next = None
    node91.prev = node6
    node6.next = node91
    node6.prev = node5
    node5.next = node6
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node91)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node91
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.data == 0
    print('Test2: OK')


def insert_after_test3():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> 4) (3 <- node4: 1 -> 5) (4 <- node5: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> 4) (CLOUD <- node4: 1 -> 5) (CLOUD <- node5: 0 -> 0) (5 <- node0: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(1)
    node4.data = 1
    node5 = Node(0)
    node5.data = 0
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node5)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    print('Test3: OK')


def insert_after_test9():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> 4) (3 <- node4: 1 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> 4) (CLOUD <- node4: 1 -> None)  None
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(1)
    node4.data = 1
    node4.next = None
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node4)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next is None
    print('Test9: OK')


def insert_after_test10():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> 4) (3 <- node4: 0 -> 5) (4 <- node5: 0 -> 2) (5 <- node102: 0 -> 1) (2 <- node101: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> 4) (CLOUD <- node4: 0 -> 0) (4 <- node0: 0 -> 5) (0 <- node5: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node102 = Node(0)
    node102.data = 0
    node101 = Node(0)
    node101.data = 0
    node101.next = None
    node101.prev = node102
    node102.next = node101
    node102.prev = node5
    node5.next = node102
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node101)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node101
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    print('Test10: OK')


def insert_after_test11():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> 4) (3 <- node4: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> 4) (CLOUD <- node4: 0 -> 0) (4 <- node0: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node4.next = None
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node4)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    print('Test11: OK')


def insert_after_test16():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 1 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 1 -> None)  None
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node3)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next is None
    print('Test16: OK')


def insert_after_test17():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 0 -> 4) (3 <- node4: 0 -> 1) (4 <- node111: 0 -> 0) (1 <- node110: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 0 -> 0) (3 <- node0: 0 -> 4) (0 <- node4: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node111 = Node(0)
    node111.data = 0
    node110 = Node(0)
    node110.data = 0
    node110.next = None
    node110.prev = node111
    node111.next = node110
    node111.prev = node4
    node4.next = node111
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node110)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node110
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    print('Test17: OK')


def insert_after_test18():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> 3) (2 <- node3: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> 3) (CLOUD <- node3: 0 -> 0) (3 <- node0: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node3)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    print('Test18: OK')


def insert_after_test22():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 1 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 1 -> None)  None
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node2)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next is None
    print('Test22: OK')


def insert_after_test23():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 0 -> 3) (2 <- node3: 0 -> 5) (3 <- node115: 0 -> 6) (5 <- node116: 0 -> 4) (6 <- node114: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 0 -> 0) (2 <- node0: 0 -> 3) (0 <- node3: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node115 = Node(0)
    node115.data = 0
    node116 = Node(0)
    node116.data = 0
    node114 = Node(0)
    node114.data = 0
    node114.next = None
    node114.prev = node116
    node116.next = node114
    node116.prev = node115
    node115.next = node116
    node115.prev = node3
    node3.next = node115
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node114)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node114
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    print('Test23: OK')


def insert_after_test24():
    '''
    Self: (None <- node1: 1 -> 2) (1 <- node2: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> 2) (CLOUD <- node2: 0 -> 0) (2 <- node0: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node2)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    print('Test24: OK')


def insert_after_test27():
    '''
    Self: (None <- node1: 1 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 1 -> None)  None
    '''
    # Input Generation
    node1 = Node(1)
    node1.data = 1
    node1.next = None
    node1.prev = None
    doublylinkedlist0 = DoublyLinkedList(node1, node1)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    print('Test27: OK')


def insert_after_test28():
    '''
    Self: (None <- node1: 0 -> 2) (1 <- node2: 0 -> 4) (2 <- node124: 0 -> 5) (4 <- node125: 0 -> 3) (5 <- node123: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 0 -> 0) (1 <- node0: 0 -> 2) (0 <- node2: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node124 = Node(0)
    node124.data = 0
    node125 = Node(0)
    node125.data = 0
    node123 = Node(0)
    node123.data = 0
    node123.next = None
    node123.prev = node125
    node125.next = node123
    node125.prev = node124
    node124.next = node125
    node124.prev = node2
    node2.next = node124
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0 = DoublyLinkedList(node1, node123)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node123
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    print('Test28: OK')


def insert_after_test29():
    '''
    Self: (None <- node1: 0 -> None)  None
    Return: None
    End Self: (CLOUD <- node1: 0 -> 0) (1 <- node0: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0 = DoublyLinkedList(node1, node1)
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next.data == 0
    print('Test29: OK')


def insert_after_test31():
    '''
    Self: Empty
    Return: None
    End Self: Empty
    '''
    # Input Generation
    doublylinkedlist0 = DoublyLinkedList(None, None)
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    print('Test31: OK')


if __name__ == "__main__":
    insert_after_test1()
    insert_after_test2()
    insert_after_test3()
    insert_after_test9()
    insert_after_test10()
    insert_after_test11()
    insert_after_test16()
    insert_after_test17()
    insert_after_test18()
    insert_after_test22()
    insert_after_test23()
    insert_after_test24()
    insert_after_test27()
    insert_after_test28()
    insert_after_test29()
    insert_after_test31()

# if __name__ == "__main__":
#     l = DoublyLinkedList()
#     l.insert_at_front(44)
#     l.insert_at_front(66)
#     l.insert_at_back(21)
#     l.insert_at_back(43)
#     print(str(l.repok()))
#     print(l.__repr__())
#     l.insert_after(43, 49)
#     l.insert_after(21, 33)
#     print(str(l.repok()))
#     print(l.__repr__())
#     print(l.pop_front())
#     print(str(l.repok()))
#     print(l.__repr__())
#     print(l.pop_back())
#     print(str(l.repok()))
#     print(l.__repr__())
#     l.remove(21)
#     print(str(l.repok()))
#     print(l.__repr__())

