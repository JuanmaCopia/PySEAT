from dll import Node, DoublyLinkedList


def insert_after_test1():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node101) (node4 <- node101: 0 -> node100) (node101 <- node100: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node101) (node4 <- node101: 0 -> node103) (node101 <- node103: 0 -> node100) (node103 <- node100: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.prev.data == 1
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
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node101) (node4 <- node101: 0 -> node100) (node101 <- node100: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node103) (node4 <- node103: 0 -> node101) (node103 <- node101: 0 -> node100) (node101 <- node100: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.prev.data == 0
    print('Test3: OK')


def insert_after_test4():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node110) (node3 <- node110: 0 -> node109) (node110 <- node109: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node110) (node3 <- node110: 0 -> node112) (node110 <- node112: 0 -> node109) (node112 <- node109: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 1
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
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node110) (node3 <- node110: 0 -> node109) (node110 <- node109: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node112) (node3 <- node112: 0 -> node110) (node112 <- node110: 0 -> node109) (node110 <- node109: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    print('Test6: OK')


def insert_after_test7():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node114) (node2 <- node114: 0 -> node115) (node114 <- node115: 0 -> node113) (node115 <- node113: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node114) (node2 <- node114: 0 -> node117) (node114 <- node117: 0 -> node115) (node117 <- node115: 0 -> node113) (node115 <- node113: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
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
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node114) (node2 <- node114: 0 -> node115) (node114 <- node115: 0 -> node113) (node115 <- node113: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node117) (node2 <- node117: 0 -> node114) (node117 <- node114: 0 -> node115) (node114 <- node115: 0 -> node113) (node115 <- node113: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    print('Test9: OK')


def insert_after_test10():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node123) (node1 <- node123: 0 -> node124) (node123 <- node124: 0 -> node122) (node124 <- node122: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node123) (node1 <- node123: 0 -> node126) (node123 <- node126: 0 -> node124) (node126 <- node124: 0 -> node122) (node124 <- node122: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
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
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0
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
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node123) (node1 <- node123: 0 -> node124) (node123 <- node124: 0 -> node122) (node124 <- node122: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node126) (node1 <- node126: 0 -> node123) (node126 <- node123: 0 -> node124) (node123 <- node124: 0 -> node122) (node124 <- node122: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
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
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0
    print('Test12: OK')


def insert_after_test13():
    '''
    Self:
        (None <- node0: 1 -> node119) (node0 <- node119: 0 -> node120) (node119 <- node120: 0 -> node121) (node120 <- node121: 0 -> node118) (node121 <- node118: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node119) (node0 <- node119: 0 -> node123) (node119 <- node123: 0 -> node120) (node123 <- node120: 0 -> node121) (node120 <- node121: 0 -> node118) (node121 <- node118: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node119 = Node(0)
    node119.data = 0
    node120 = Node(0)
    node120.data = 0
    node121 = Node(0)
    node121.data = 0
    node118 = Node(0)
    node118.data = 0
    node118.next = None
    node118.prev = node121
    node121.next = node118
    node121.prev = node120
    node120.next = node121
    node120.prev = node119
    node119.next = node120
    node119.prev = node0
    node0.next = node119
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node118
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
        (None <- node0: 0 -> node119) (node0 <- node119: 0 -> node120) (node119 <- node120: 0 -> node121) (node120 <- node121: 0 -> node118) (node121 <- node118: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node123) (node0 <- node123: 0 -> node119) (node123 <- node119: 0 -> node120) (node119 <- node120: 0 -> node121) (node120 <- node121: 0 -> node118) (node121 <- node118: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(0)
    node0.data = 0
    node0.prev = None
    node119 = Node(0)
    node119.data = 0
    node120 = Node(0)
    node120.data = 0
    node121 = Node(0)
    node121.data = 0
    node118 = Node(0)
    node118.data = 0
    node118.next = None
    node118.prev = node121
    node121.next = node118
    node121.prev = node120
    node120.next = node121
    node120.prev = node119
    node119.next = node120
    node119.prev = node0
    node0.next = node119
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node118
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
