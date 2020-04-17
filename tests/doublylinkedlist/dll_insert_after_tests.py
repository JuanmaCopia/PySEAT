from dll import Node, DoublyLinkedList


def insert_after_test1():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
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
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    print('Test1: OK')


def insert_after_test2():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node5) (node4 <- node5: 0 -> node90) (node5 <- node90: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node92) (node4 <- node92: 0 -> node5) (node92 <- node5: 0 -> node90) (node5 <- node90: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node90 = Node(0)
    node90.data = 0
    node90.next = None
    node90.prev = node5
    node5.next = node90
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node90
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.prev.data == 0
    print('Test2: OK')


def insert_after_test3():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node64) (node4 <- node64: 0 -> None)  CLOUD
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
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
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 1
    print('Test3: OK')


def insert_after_test4():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(1)
    node2.data = 1
    node3 = Node(1)
    node3.data = 1
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    print('Test4: OK')


def insert_after_test5():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node4) (node3 <- node4: 0 -> node101) (node4 <- node101: 0 -> node100) (node101 <- node100: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node103) (node3 <- node103: 0 -> node4) (node103 <- node4: 0 -> node101) (node4 <- node101: 0 -> node100) (node101 <- node100: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(1)
    node2.data = 1
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node101 = Node(0)
    node101.data = 0
    node100 = Node(0)
    node100.data = 0
    node100.next = None
    node100.prev = node101
    node101.next = node100
    node101.prev = node4
    node4.next = node101
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node100
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.prev.data == 0
    print('Test5: OK')


def insert_after_test6():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node48) (node3 <- node48: 0 -> None)  CLOUD
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(1)
    node2.data = 1
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1
    print('Test6: OK')


def insert_after_test7():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(1)
    node2.data = 1
    node2.next = None
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    print('Test7: OK')


def insert_after_test8():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node3) (node2 <- node3: 0 -> node110) (node3 <- node110: 0 -> node109) (node110 <- node109: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node112) (node2 <- node112: 0 -> node3) (node112 <- node3: 0 -> node110) (node3 <- node110: 0 -> node109) (node110 <- node109: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node110 = Node(0)
    node110.data = 0
    node109 = Node(0)
    node109.data = 0
    node109.next = None
    node109.prev = node110
    node110.next = node109
    node110.prev = node3
    node3.next = node110
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node109
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    print('Test8: OK')


def insert_after_test9():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node34) (node2 <- node34: 0 -> None)  CLOUD
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    print('Test9: OK')


def insert_after_test10():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node1.next = None
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    print('Test10: OK')


def insert_after_test11():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node2) (node1 <- node2: 0 -> node114) (node2 <- node114: 0 -> node115) (node114 <- node115: 0 -> node113) (node115 <- node113: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node117) (node1 <- node117: 0 -> node2) (node117 <- node2: 0 -> node114) (node2 <- node114: 0 -> node115) (node114 <- node115: 0 -> node113) (node115 <- node113: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(0)
    node1.data = 0
    node2 = Node(0)
    node2.data = 0
    node114 = Node(0)
    node114.data = 0
    node115 = Node(0)
    node115.data = 0
    node113 = Node(0)
    node113.data = 0
    node113.next = None
    node113.prev = node115
    node115.next = node113
    node115.prev = node114
    node114.next = node115
    node114.prev = node2
    node2.next = node114
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node113
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    print('Test11: OK')


def insert_after_test12():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node22) (node1 <- node22: 0 -> None)  CLOUD
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    print('Test12: OK')


def insert_after_test13():
    '''
    Self:
        (None <- node0: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.next = None
    node0.prev = None
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node0
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None
    print('Test13: OK')


def insert_after_test14():
    '''
    Self:
        (None <- node0: 0 -> node1) (node0 <- node1: 0 -> node123) (node1 <- node123: 0 -> node124) (node123 <- node124: 0 -> node122) (node124 <- node122: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node126) (node0 <- node126: 0 -> node1) (node126 <- node1: 0 -> node123) (node1 <- node123: 0 -> node124) (node123 <- node124: 0 -> node122) (node124 <- node122: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(0)
    node0.data = 0
    node0.prev = None
    node1 = Node(0)
    node1.data = 0
    node123 = Node(0)
    node123.data = 0
    node124 = Node(0)
    node124.data = 0
    node122 = Node(0)
    node122.data = 0
    node122.next = None
    node122.prev = node124
    node124.next = node122
    node124.prev = node123
    node123.next = node124
    node123.prev = node1
    node1.next = node123
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node122
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0
    print('Test14: OK')


def insert_after_test15():
    '''
    Self:
        (None <- node0: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node12) (node0 <- node12: 0 -> None)  CLOUD
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(0)
    node0.data = 0
    node0.next = None
    node0.prev = None
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node0
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    doublylinkedlist0.insert_after(0, 0)
    # Assertions
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    print('Test15: OK')


def insert_after_test16():
    '''
    Self:
        Empty
    Return:
        None
    End Self:
        Empty
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    assert doublylinkedlist0.tail is None
    print('Test16: OK')


if __name__ == '__main__':
    insert_after_test1()
    insert_after_test2()
    insert_after_test3()
    insert_after_test4()
    insert_after_test5()
    insert_after_test6()
    insert_after_test7()
    insert_after_test8()
    insert_after_test9()
    insert_after_test10()
    insert_after_test11()
    insert_after_test12()
    insert_after_test13()
    insert_after_test14()
    insert_after_test15()
    insert_after_test16()
