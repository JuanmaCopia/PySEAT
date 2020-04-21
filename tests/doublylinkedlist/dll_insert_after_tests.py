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
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node6) (node4 <- node6: 0 -> None)  None
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
    print('Test2: OK')


def insert_after_test3():
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
    print('Test3: OK')


def insert_after_test4():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node4) (node3 <- node4: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node6) (node3 <- node6: 0 -> node4) (node6 <- node4: 0 -> None)  None
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
    assert doublylinkedlist0.tail.prev.prev.data == 0
    print('Test4: OK')


def insert_after_test5():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node5) (node3 <- node5: 0 -> None)  None
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
    print('Test5: OK')


def insert_after_test6():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node13) (node2 <- node13: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node13) (node2 <- node13: 0 -> node15) (node13 <- node15: 0 -> None)  None
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
    node13 = Node(0)
    node13.data = 0
    node13.next = None
    node13.prev = node2
    node2.next = node13
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node13
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
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node3) (node2 <- node3: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node5) (node2 <- node5: 0 -> node3) (node5 <- node3: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.next.data == 0
    print('Test7: OK')


def insert_after_test8():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node13) (node2 <- node13: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node15) (node2 <- node15: 0 -> node13) (node15 <- node13: 0 -> None)  None
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
    node13 = Node(0)
    node13.data = 0
    node13.next = None
    node13.prev = node2
    node2.next = node13
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node13
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
    print('Test8: OK')


def insert_after_test9():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node28) (node1 <- node28: 0 -> node27) (node28 <- node27: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node28) (node1 <- node28: 0 -> node30) (node28 <- node30: 0 -> node27) (node30 <- node27: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(1)
    node1.data = 1
    node28 = Node(0)
    node28.data = 0
    node27 = Node(0)
    node27.data = 0
    node27.next = None
    node27.prev = node28
    node28.next = node27
    node28.prev = node1
    node1.next = node28
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node27
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
    print('Test9: OK')


def insert_after_test10():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node2) (node1 <- node2: 0 -> node13) (node2 <- node13: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node15) (node1 <- node15: 0 -> node2) (node15 <- node2: 0 -> node13) (node2 <- node13: 0 -> None)  None
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
    node13 = Node(0)
    node13.data = 0
    node13.next = None
    node13.prev = node2
    node2.next = node13
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node13
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
    print('Test10: OK')


def insert_after_test11():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node28) (node1 <- node28: 0 -> node27) (node28 <- node27: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node30) (node1 <- node30: 0 -> node28) (node30 <- node28: 0 -> node27) (node28 <- node27: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node1 = Node(0)
    node1.data = 0
    node28 = Node(0)
    node28.data = 0
    node27 = Node(0)
    node27.data = 0
    node27.next = None
    node27.prev = node28
    node28.next = node27
    node28.prev = node1
    node1.next = node28
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node27
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
    print('Test11: OK')


def insert_after_test12():
    '''
    Self:
        (None <- node0: 1 -> node38) (node0 <- node38: 0 -> node39) (node38 <- node39: 0 -> node37) (node39 <- node37: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node38) (node0 <- node38: 0 -> node41) (node38 <- node41: 0 -> node39) (node41 <- node39: 0 -> node37) (node39 <- node37: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(1)
    node0.data = 1
    node0.prev = None
    node38 = Node(0)
    node38.data = 0
    node39 = Node(0)
    node39.data = 0
    node37 = Node(0)
    node37.data = 0
    node37.next = None
    node37.prev = node39
    node39.next = node37
    node39.prev = node38
    node38.next = node39
    node38.prev = node0
    node0.next = node38
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node37
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
    print('Test12: OK')


def insert_after_test13():
    '''
    Self:
        (None <- node0: 0 -> node1) (node0 <- node1: 0 -> node28) (node1 <- node28: 0 -> node27) (node28 <- node27: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node30) (node0 <- node30: 0 -> node1) (node30 <- node1: 0 -> node28) (node1 <- node28: 0 -> node27) (node28 <- node27: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(0)
    node0.data = 0
    node0.prev = None
    node1 = Node(0)
    node1.data = 0
    node28 = Node(0)
    node28.data = 0
    node27 = Node(0)
    node27.data = 0
    node27.next = None
    node27.prev = node28
    node28.next = node27
    node28.prev = node1
    node1.next = node28
    node1.prev = node0
    node0.next = node1
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node27
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
    print('Test13: OK')


def insert_after_test14():
    '''
    Self:
        (None <- node0: 0 -> node38) (node0 <- node38: 0 -> node39) (node38 <- node39: 0 -> node37) (node39 <- node37: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node41) (node0 <- node41: 0 -> node38) (node41 <- node38: 0 -> node39) (node38 <- node39: 0 -> node37) (node39 <- node37: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(0)
    node0.data = 0
    node0.prev = None
    node38 = Node(0)
    node38.data = 0
    node39 = Node(0)
    node39.data = 0
    node37 = Node(0)
    node37.data = 0
    node37.next = None
    node37.prev = node39
    node39.next = node37
    node39.prev = node38
    node38.next = node39
    node38.prev = node0
    node0.next = node38
    doublylinkedlist0.head = node0
    doublylinkedlist0.tail = node37
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
    print('Test14: OK')


def insert_after_test15():
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
    print('Test15: OK')


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
