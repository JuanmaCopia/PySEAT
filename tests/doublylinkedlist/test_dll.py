from dll import *


def test_insert_after1():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
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


def test_insert_after2():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after3():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
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


def test_insert_after4():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after5():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after6():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
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


def test_insert_after7():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after8():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after9():
    '''
    Self:
        None <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 -> None
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


def test_insert_after10():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after11():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after12():
    '''
    Self:
        None <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 -> None
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


def test_insert_after13():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
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


def test_insert_after14():
    '''
    Self:
        None <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 -> None
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


def test_insert_after15():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
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


