from dll import *
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


def test_insert_after17():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
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
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_insert_after18():
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


def test_remove22():
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
    returnv = doublylinkedlist0.remove(0)
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


def test_remove23():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
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


def test_remove24():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_remove25():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
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


def test_remove26():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
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


def test_remove27():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
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


def test_remove28():
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
    returnv = doublylinkedlist0.remove(0)
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


def test_remove29():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove30():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove31():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_remove32():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_remove33():
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_remove34():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_remove35():
    '''
    Self:
        None <- 1 ->  <- 0 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_remove36():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_remove37():
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_remove38():
    '''
    Self:
        None <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 -> None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove39():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
    Return:
        None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove40():
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_remove41():
    '''
    Self:
        None <- 0 -> None
    Return:
        None
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_remove42():
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
    returnv = doublylinkedlist0.remove(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_find43():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        False
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == False
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1
    assert doublylinkedlist0.head.next.next.data == 1


def test_find44():
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


def test_find45():
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


def test_find46():
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


def test_find47():
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


def test_find48():
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


def test_find49():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        False
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == False
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 1


def test_find50():
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


def test_find51():
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


def test_find52():
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


def test_find53():
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


def test_find54():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 1 -> None
    Return:
        False
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == False
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1


def test_find55():
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


def test_find56():
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


def test_find57():
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


def test_find58():
    '''
    Self:
        None <- 1 ->  <- 1 -> None
    Return:
        False
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == False
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 1
    assert doublylinkedlist0.tail.next is None


def test_find59():
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


def test_find60():
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


def test_find61():
    '''
    Self:
        None <- 1 -> None
    Return:
        False
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
    returnv = doublylinkedlist0.find(0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == False
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_find62():
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


def test_find63():
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


def test_insert_at_back64():
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
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0
    assert doublylinkedlist0.tail.prev.prev.data == 0


def test_insert_at_back65():
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
    assert doublylinkedlist0.tail.prev.data == 0
    assert doublylinkedlist0.head.next.next.data == 0


def test_insert_at_back66():
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
    assert doublylinkedlist0.tail.prev.data == 0


def test_insert_at_back67():
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


def test_insert_at_back68():
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


def test_insert_at_back69():
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


def test_insert_at_front70():
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


def test_insert_at_front71():
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


def test_insert_at_front72():
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


def test_insert_at_front73():
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


def test_insert_at_front74():
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


def test_insert_at_front75():
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
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_top_front76():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
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
    returnv = doublylinkedlist0.top_front()
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
    assert doublylinkedlist0.head.next.next.data == 0


def test_top_front77():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.top_front()
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


def test_top_front78():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.top_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_top_front79():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.top_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_top_front80():
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
    returnv = doublylinkedlist0.top_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_top_front81():
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
    returnv = doublylinkedlist0.top_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_top_back82():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
    Return:
        0
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
    returnv = doublylinkedlist0.top_back()
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
    assert doublylinkedlist0.head.next.next.data == 0


def test_top_back83():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.top_back()
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


def test_top_back84():
    '''
    Self:
        None <- 0 ->  <- 0 ->  <- 0 -> None
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
    returnv = doublylinkedlist0.top_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_top_back85():
    '''
    Self:
        None <- 0 ->  <- 0 -> None
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
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_top_back86():
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
    returnv = doublylinkedlist0.top_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_top_back87():
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
    returnv = doublylinkedlist0.top_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_front88():
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
    returnv = doublylinkedlist0.pop_front()
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


def test_pop_front89():
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
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 0


def test_pop_front90():
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
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None


def test_pop_front91():
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
    returnv = doublylinkedlist0.pop_front()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head.data == 0
    assert doublylinkedlist0.head.next is None
    assert doublylinkedlist0.head.prev is None


def test_pop_front92():
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


def test_pop_front93():
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


def test_pop_back94():
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


def test_pop_back95():
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


def test_pop_back96():
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


def test_pop_back97():
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


def test_pop_back98():
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
    returnv = doublylinkedlist0.pop_back()
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv == 0
    assert doublylinkedlist0.head is None
    assert doublylinkedlist0.tail is None


def test_pop_back99():
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


