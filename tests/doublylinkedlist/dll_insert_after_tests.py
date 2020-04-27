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
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node4) (node2 <- node4: 0 -> None)  None
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
    print('Test8: OK')


def insert_after_test9():
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
    print('Test9: OK')


def insert_after_test10():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node2) (node1 <- node2: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node4) (node1 <- node4: 0 -> node2) (node4 <- node2: 0 -> None)  None
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
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    print('Test10: OK')


def insert_after_test11():
    '''
    Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 1 -> node1) (node0 <- node1: 0 -> node3) (node1 <- node3: 0 -> None)  None
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
    print('Test11: OK')


def insert_after_test12():
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
    print('Test12: OK')


def insert_after_test13():
    '''
    Self:
        (None <- node0: 0 -> node1) (node0 <- node1: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node3) (node0 <- node3: 0 -> node1) (node3 <- node1: 0 -> None)  None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node0 = Node(0)
    node0.data = 0
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
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    print('Test13: OK')


def insert_after_test14():
    '''
    Self:
        (None <- node0: 0 -> None)  None
    Return:
        None
    End Self:
        (None <- node0: 0 -> node2) (node0 <- node2: 0 -> None)  None
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
