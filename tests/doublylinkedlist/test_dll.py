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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    assert doublylinkedlist0.head.next.next.data == 1


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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


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
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1


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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


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
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0


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
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


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
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


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
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


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
    node1 = Node(1)
    node1.data = 1
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


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
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


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
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


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
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_remove1():
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    assert doublylinkedlist0.head.next.next.data == 1


def test_remove2():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove3():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove4():
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove5():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove6():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove7():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove8():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove9():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    node5.next = None
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove10():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove11():
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove12():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove13():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_remove14():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove15():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node3 = Node(0)
    node3.data = 0
    node5 = Node(0)
    node5.data = 0
    node4 = Node(0)
    node4.data = 0
    node4.next = None
    node4.prev = node5
    node5.next = node4
    node5.prev = node3
    node3.next = node5
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0


def test_remove16():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove17():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove18():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_remove19():
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
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_remove20():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_remove21():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove22():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_remove23():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node4 = Node(0)
    node4.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node4
    node4.next = node3
    node4.prev = node2
    node2.next = node4
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_remove24():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_remove25():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_remove26():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove27():
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
    node1 = Node(1)
    node1.data = 1
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove28():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove29():
    '''
    Self:
        None <- 0 -> None
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_remove30():
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
    returnv = doublylinkedlist0.remove(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_find1():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        False
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == False
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    assert doublylinkedlist0.head.next.next.data == 1


def test_find2():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == True
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    assert doublylinkedlist0.head.next.next.data == 1


def test_find3():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        False
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == False
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_find4():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == True
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_find5():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        False
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == False
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_find6():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == True
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_find7():
    '''
    Self:
        None <- 1 ->  <- 1 -> None
    Return:
        False
    End Self:
        None <- 1 ->  <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(1)
    node2.data = 1
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == False
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_find8():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == True
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_find9():
    '''
    Self:
        None <- 1 -> None
    Return:
        False
    End Self:
        None <- 1 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(1)
    node1.data = 1
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == False
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_find10():
    '''
    Self:
        None <- 0 -> None
    Return:
        True
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == True
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_find11():
    '''
    Self:
        <Empty list>
    Return:
        False
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
    returnv = doublylinkedlist0.find(0)
    # Assertions
    assert returnv == False
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_insert_at_back1():
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
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_back(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_insert_at_back2():
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
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_back(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_insert_at_back3():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_back(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_insert_at_front1():
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
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_front(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_insert_at_front2():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_front(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_top_front1():
    '''
    Self:
        None <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.top_front()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_top_front2():
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
    returnv = doublylinkedlist0.top_front()
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_top_back1():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node5
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.top_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_top_back2():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
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
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node4
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.top_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_top_back3():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.top_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_top_back4():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.top_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_top_back5():
    '''
    Self:
        None <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.top_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_top_back6():
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
    returnv = doublylinkedlist0.top_back()
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_front1():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_front()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_front2():
    '''
    Self:
        None <- 0 -> None
    Return:
        0
    End Self:
        <Empty list>
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_front()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_front3():
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
    returnv = doublylinkedlist0.pop_front()
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_back1():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_pop_back2():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_back3():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_back4():
    '''
    Self:
        None <- 0 -> None
    Return:
        0
    End Self:
        <Empty list>
    '''
    # Self Generation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Assertions
    assert returnv == 0
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_back5():
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
    returnv = doublylinkedlist0.pop_back()
    # Assertions
    assert returnv is None
    # Repok check
    assert doublylinkedlist0.repok()
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None

