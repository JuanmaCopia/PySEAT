class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def repok(self):
        return True

    def conservative_repok(self):
        return True

    def instrumented_repok(self):
        return True


class CDLinkedList:
    def __init__(self, head=None):
        self.head = head

    def pretty_print(self):

        cir_dbl_list_str = ""

        current_node = self.head

        while current_node:
            cir_dbl_list_str += "-({0:1d})-".format(current_node.key)

            current_node = current_node.next
            if current_node == self.head:
                break

        return cir_dbl_list_str

    # Insert node at the end of the circular doubly linked list
    def append(self, key):
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
    def insert_after_node(self, afterkey, key):
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


def insert_after_node_test1():
    '''
    Self: (5 <- node0: 0 -> 1) (0 <- node1: 0 -> 5) (1 <- node165: 0 -> 0) **node0
    Return: None
    End Self: (CLOUD <- node0: 0 -> 2) (0 <- node2: 0 -> 1) (2 <- node1: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node0 = Node(0)
    node0.key = 0
    node1 = Node(0)
    node1.key = 0
    node165 = Node(0)
    node165.key = 0
    node165.next = node0
    node165.prev = node1
    node1.next = node165
    node1.prev = node0
    node0.next = node1
    node0.prev = node165
    cdlinkedlist0 = CDLinkedList(node0)
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    print('Test1: OK')


def insert_after_node_test2():
    '''
    Self: (9 <- node0: 1 -> 1) (0 <- node1: 0 -> 2) (1 <- node2: 0 -> 9) (2 <- node169: 0 -> 0) **node0
    Return: None
    End Self: (CLOUD <- node0: 1 -> 1) (CLOUD <- node1: 0 -> 3) (1 <- node3: 0 -> 2) (3 <- node2: 0 -> CLOUD)  CLOUD
    '''
    # Input Generation
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node169 = Node(0)
    node169.key = 0
    node169.next = node0
    node169.prev = node2
    node2.next = node169
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node169
    cdlinkedlist0 = CDLinkedList(node0)
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0
    print('Test2: OK')


def insert_after_node_test6():
    '''
    Self: (1 <- node0: 1 -> 1) (0 <- node1: 0 -> 0) **node0
    Return: None
    End Self: (2 <- node0: 1 -> 1) (CLOUD <- node1: 0 -> 2) (1 <- node2: 0 -> 0) **node0
    '''
    # Input Generation
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node1.next = node0
    node1.prev = node0
    node0.next = node1
    node0.prev = node1
    cdlinkedlist0 = CDLinkedList(node0)
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    print('Test6: OK')


def insert_after_node_test7():
    '''
    Self: (1 <- node0: 1 -> 1) (0 <- node1: 1 -> 0) **node0
    Return: None
    End Self: (CLOUD <- node0: 1 -> 1) (CLOUD <- node1: 1 -> 0) **node0
    '''
    # Input Generation
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node1.next = node0
    node1.prev = node0
    node0.next = node1
    node0.prev = node1
    cdlinkedlist0 = CDLinkedList(node0)
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    print('Test7: OK')


def insert_after_node_test11():
    '''
    Self: (0 <- node0: 0 -> 0)
    Return: None
    End Self: (1 <- node0: 0 -> 1) (0 <- node1: 0 -> 0) **node0
    '''
    # Input Generation
    node0 = Node(0)
    node0.key = 0
    node0.next = node0
    node0.prev = node0
    cdlinkedlist0 = CDLinkedList(node0)
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    print('Test11: OK')


def insert_after_node_test12():
    '''
    Self: (0 <- node0: 1 -> 0)
    Return: None
    End Self: (CLOUD <- node0: 1 -> 0) **node0
    '''
    # Input Generation
    node0 = Node(1)
    node0.key = 1
    node0.next = node0
    node0.prev = node0
    cdlinkedlist0 = CDLinkedList(node0)
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    print('Test12: OK')


def insert_after_node_test13():
    '''
    Self: Empty
    Return: None
    End Self: Empty
    '''
    # Input Generation
    cdlinkedlist0 = CDLinkedList(None)
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head is None
    print('Test13: OK')


if __name__ == "__main__":
    insert_after_node_test1()
    insert_after_node_test2()
    insert_after_node_test7()
    insert_after_node_test6()
    insert_after_node_test11()
    insert_after_node_test12()
    insert_after_node_test13()
# if __name__ == "__main__":
#     cir_dbl_list = CDLinkedList()
#     data = [48, 41, 33, 56]
#     for value in data:
#         cir_dbl_list.append(value)
#         assert cir_dbl_list.repok()

# if __name__ == "__main__":

#     # Create circular doubly linked list
#     cir_dbl_list = CDLinkedList()

#     print('\n---------------- Insert Operations ----------------  ')

#     print('\nFirst Insert operation is an append into an empty list ')
#     print('Subsequently it becomes an append into existing list ')

#     data = [48, 41, 33, 56]

#     for value in data:
#         cir_dbl_list.append(value)

#     # Expected -(48)--(41)--(33)--(56)-
#     print('\nCircular Doubly linked list elements using append --->\n',
#           cir_dbl_list.pretty_print())

#     # Create circular doubly linked list
#     cir_dbl_list_2 = CDLinkedList()

#     print('\nFirst Insert operation is a prepend into an empty list ')
#     print('Subsequently it becomes a prepend into existing list ')

#     data_2 = [37, 14, 21, 8]

#     for value in data_2:
#         cir_dbl_list_2.prepend(value)

#     # Expected -(8)--(21)--(14)--(37)-
#     print('\nCircular Doubly linked list elements using prepend --->\n',
#           cir_dbl_list_2.pretty_print())

#     # Insertion after the last node - Append
#     # Expected -(48)--(41)--(33)--(56)--(17)-
#     cir_dbl_list.insert_after_node(56, 17)
#     print('\nInsert after last node -- key 17 after 56 --->\n',
#           cir_dbl_list.pretty_print())

#     # Insertion in between nodes - After first node
#     # Expected -(48)--(27)--(41)--(33)--(56)--(17)-
#     cir_dbl_list.insert_after_node(48, 27)
#     print('\nInsert after first node -- key 27 after 48 --->\n',
#           cir_dbl_list.pretty_print())

#     # Insertion between nodes
#     # Expected -(48)--(27)--(41)--(33)--(37)--(56)--(17)-
#     cir_dbl_list.insert_after_node(33, 37)
#     print('\nInsert in between nodes -- key 37 after 33  --->\n',
#           cir_dbl_list.pretty_print())

#     # Try to insert after a non existing node
#     # Expected - -(48)--(27)--(41)--(33)--(37)--(56)--(17)-
#     cir_dbl_list.insert_after_node(11, 55)
#     print('\nNo change - Insert after a non existing node  --->\n',
#           cir_dbl_list.pretty_print())

#     # Insertion before a node - prepend operation
#     # Expected -(16)--(48)--(27)--(41)--(33)--(37)--(56)--(17)-
#     cir_dbl_list.insert_before_node(48, 16)
#     print('\nInsert in between nodes -- key 16 before 48  --->\n',
#           cir_dbl_list.pretty_print())

#     # Insertion before a node - In between nodes
#     # Expected -(16)--(48)--(27)--(41)--(33)--(37)--(29)--(56)--(17)-
#     cir_dbl_list.insert_before_node(56, 29)
#     print('\nInsert in between nodes -- key 29 before 56  --->\n',
#           cir_dbl_list.pretty_print())

#     # Try to insert after a non existing node
#     # Expected - -(16)--(48)--(27)--(41)--(33)--(37)--(29)--(56)--(17)-
#     cir_dbl_list.insert_after_node(11, 55)
#     print('\nNo change - Insert before a non existing node  --->\n',
#           cir_dbl_list.pretty_print())

#     print('\n---------------- Delete Operations ---------------- ')

#     del_cir_dbl_list0 = CDLinkedList()
#     del_cir_dbl_list0.append(77)

#     # Expected - -(77)-
#     print('\nSingle element circular doubly linked list before deletion --->\n',
#           del_cir_dbl_list0.pretty_print())

#     # Case 1 - Node to be deleted is head and there is only a single element
#     # in the circular doubly linked list
#     # Expected - To see nothing printed
#     del_cir_dbl_list0.delete(77)
#     print('\nNo linked list present after deleting only node  --->',
#           del_cir_dbl_list0.pretty_print())

#     # Expected -(16)--(48)--(27)--(41)--(33)--(37)--(29)--(56)--(17)-
#     print('\nCircular Doubly linked list before deletion --->\n',
#           cir_dbl_list.pretty_print())

#     # Case 2 - Node to be deleted is head and there are more elements in list
#     # Expected - --(48)--(27)--(41)--(33)--(37)--(29)--(56)--(17)-
#     cir_dbl_list.delete(16)
#     print('\nList after deletion of head -- key 16 --->\n',
#           cir_dbl_list.pretty_print())

#     # Case 3 - Node to be deleted is in between nodes
#     # Expected - -(48)--(27)--(41)--(33)--(29)--(56)--(17)-
#     cir_dbl_list.delete(37)
#     print('\nList node to be deleted is between nodes -- key 37 --->\n',
#           cir_dbl_list.pretty_print())

#     # Case 4 - Node to be deleted is the last node
#     # Expected - -(48)--(27)--(41)--(33)--(29)--(56)-
#     cir_dbl_list.delete(17)
#     print('\nList Node to be deleted is last node -- key 17 --->\n',
#           cir_dbl_list.pretty_print())

#     # Try to delete a non existing key
#     # Expected - -(48)--(27)--(41)--(33)--(29)--(56)-
#     cir_dbl_list.delete(88)
#     print('\nNo change - When trying to delete non existing key--->\n',
#           cir_dbl_list.pretty_print())

#     '''
#     Sample Input : array = { 48, 27, 41, 33, 29, 56 }

#     Sample Output : -(48)--(27)--(41)--(33)--(29)--(56)-

#     '''
