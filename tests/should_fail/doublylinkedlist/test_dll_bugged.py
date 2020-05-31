from dll_bugged import *
import pytest


def test_insert_after1():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node5 = Node(0)
    node5.data = 1
    node2 = Node(0)
    node2.data = 1
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
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
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node5 = Node(0)
    node5.data = 1
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
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
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1
    assert doublylinkedlist0.tail.prev.prev.data == 0


def test_insert_after4():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0


def test_insert_after5():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0


def test_insert_after6():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0


def test_insert_after7():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node2 = Node(0)
    node2.data = 1
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_insert_after8():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1


def test_insert_after9():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_insert_after10():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_insert_after11():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_insert_after12():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node2 = Node(0)
    node2.data = 1
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
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_insert_after13():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
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
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0


def test_insert_after14():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
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
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_insert_after15():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_insert_after16():
    '''
    Self:
        None <- 1 ->  <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


@pytest.mark.timeout(2)
def test_insert_after17():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
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
    # Repok check
    assert doublylinkedlist0.repok()


@pytest.mark.timeout(2)
def test_insert_after18():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()


def test_insert_after19():
    '''
    Self:
        None <- 1 -> None
    Return:
        None
    End Self:
        None <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_insert_after20():
    '''
    Self:
        None <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_insert_after21():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_find1():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node5 = Node(0)
    node5.data = 1
    node2 = Node(0)
    node2.data = 1
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()


def test_find2():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node5 = Node(0)
    node5.data = 1
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
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
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 1


def test_find4():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_find5():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_find6():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_find7():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node2 = Node(0)
    node2.data = 1
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()


def test_find8():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 1
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_find9():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0


def test_find10():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_find11():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_find12():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
    node2 = Node(0)
    node2.data = 1
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()


def test_find13():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node3 = Node(0)
    node3.data = 1
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_find14():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_find15():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_find16():
    '''
    Self:
        None <- 1 ->  <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
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
    # Repok check
    assert doublylinkedlist0.repok()


def test_find17():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 1 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_find18():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        True
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_find19():
    '''
    Self:
        None <- 1 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.next = None
    node1.prev = None
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node1
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()


def test_find20():
    '''
    Self:
        None <- 0 -> None
    Return:
        True
    End Self:
        None <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == True
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_find21():
    '''
    Self:
        <Empty list>
    Return:
        False
    End Self:
        <Empty list>
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == False
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_insert_at_front1():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_front(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0


def test_insert_at_front2():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_front(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_insert_at_front3():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.insert_at_front(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_insert_at_front4():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.insert_at_front(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_insert_at_front5():
    '''
    Self:
        None <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_insert_at_front6():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        None <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_front(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.tail is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_insert_at_back1():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_back(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.next.data == 0


def test_insert_at_back2():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_back(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.head.next.next.next.data == 0


def test_insert_at_back3():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.insert_at_back(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_insert_at_back4():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_insert_at_back5():
    '''
    Self:
        None <- 0 -> None
    Return:
        None
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_insert_at_back6():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        None <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_at_back(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_front1():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_pop_front2():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_pop_front3():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
         <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_pop_front4():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
         <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None


def test_pop_front5():
    '''
    Self:
        None <- 0 -> None
    Return:
        0
    End Self:
        <Empty list>
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_front6():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_back1():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node5 = Node(0)
    node5.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0
    assert doublylinkedlist0.tail.prev.data == 0


def test_pop_back2():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 0
    node1.prev = None
    node3 = Node(0)
    node3.data = 0
    node4 = Node(0)
    node4.data = 0
    node2 = Node(0)
    node2.data = 0
    node2.next = None
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node2
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_pop_back3():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 ->  <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_pop_back4():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_back5():
    '''
    Self:
        None <- 0 -> None
    Return:
        0
    End Self:
        None <- 0 -> None
    '''
    # Input Creation
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.tail is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_back6():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    doublylinkedlist0.head = None
    doublylinkedlist0.tail = None
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.pop_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


