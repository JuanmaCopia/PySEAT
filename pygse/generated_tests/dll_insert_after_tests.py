from dll import Node, DoublyLinkedList


def insert_after_test1():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node5) (node4 <- node5: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node5) (node4 <- node5: 1 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.next is None
    print('Test1: OK')


def insert_after_test2():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node5) (node4 <- node5: 0 -> node6) (node5 <- node6: 0 -> node91) (node6 <- node91: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node5) (node4 <- node5: 0 -> node92) (node5 <- node92: 0 -> node6) (node92 <- node6: 0 -> node91) (node6 <- node91: 0 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.next.next is None
    print('Test2: OK')


def insert_after_test3():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node5) (node4 <- node5: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node5) (node4 <- node5: 0 -> node64) (node5 <- node64: 0 -> CLOUD)  CLOUD
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next is None
    print('Test3: OK')


def insert_after_test4():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.next is None
    print('Test4: OK')


def insert_after_test5():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node5) (node4 <- node5: 0 -> node102) (node5 <- node102: 0 -> node101) (node102 <- node101: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node103) (node4 <- node103: 0 -> node5) (node103 <- node5: 0 -> node102) (node5 <- node102: 0 -> node101) (node102 <- node101: 0 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.next.next is None
    print('Test5: OK')


def insert_after_test6():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node48) (node4 <- node48: 0 -> CLOUD)  CLOUD
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next is None
    print('Test6: OK')


def insert_after_test7():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.head.next.next.next is None
    print('Test7: OK')


def insert_after_test8():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node4) (node3 <- node4: 0 -> node111) (node4 <- node111: 0 -> node110) (node111 <- node110: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node112) (node3 <- node112: 0 -> node4) (node112 <- node4: 0 -> node111) (node4 <- node111: 0 -> node110) (node111 <- node110: 0 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.next is None
    print('Test8: OK')


def insert_after_test9():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node34) (node3 <- node34: 0 -> CLOUD)  CLOUD
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next is None
    print('Test9: OK')


def insert_after_test10():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 1 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.head.next.next is None
    print('Test10: OK')


def insert_after_test11():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 0 -> node3) (node2 <- node3: 0 -> node115) (node3 <- node115: 0 -> node116) (node115 <- node116: 0 -> node114) (node116 <- node114: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 0 -> node117) (node2 <- node117: 0 -> node3) (node117 <- node3: 0 -> node115) (node3 <- node115: 0 -> node116) (node115 <- node116: 0 -> node114) (node116 <- node114: 0 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next.next is None
    print('Test11: OK')


def insert_after_test12():
    '''
    Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> node2) (node1 <- node2: 0 -> node22) (node2 <- node22: 0 -> CLOUD)  CLOUD
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next is None
    print('Test12: OK')


def insert_after_test13():
    '''
    Self:
        (None <- node1: 1 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 1 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    print('Test13: OK')


def insert_after_test14():
    '''
    Self:
        (None <- node1: 0 -> node2) (node1 <- node2: 0 -> node124) (node2 <- node124: 0 -> node125) (node124 <- node125: 0 -> node123) (node125 <- node123: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 0 -> node126) (node1 <- node126: 0 -> node2) (node126 <- node2: 0 -> node124) (node2 <- node124: 0 -> node125) (node124 <- node125: 0 -> node123) (node125 <- node123: 0 -> None)  None
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.next.next is None
    print('Test14: OK')


def insert_after_test15():
    '''
    Self:
        (None <- node1: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node1: 0 -> node12) (node1 <- node12: 0 -> CLOUD)  CLOUD
    '''
    # Self Generation
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
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next is None
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
