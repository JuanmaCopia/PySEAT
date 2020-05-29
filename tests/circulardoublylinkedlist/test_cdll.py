from cdll import *
import pytest


def test_insert_after1():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_after2():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_after3():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_after4():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_after5():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 1


def test_insert_after6():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_insert_after7():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after8():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after9():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after10():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after11():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_after12():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after13():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after14():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after15():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_after16():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_after17():
    '''
    Self:
         <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_after18():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_after19():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_insert_after20():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1


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
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head is None


def test_insert_before22():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_before23():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_before24():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_before25():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_before26():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 1


def test_insert_before27():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_insert_before28():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_before29():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_before30():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_before31():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_before32():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_before33():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_before34():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_before35():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_before36():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_before37():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_before38():
    '''
    Self:
         <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_before39():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_before40():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_insert_before41():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1


def test_insert_before42():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head is None


def test_delete43():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_delete44():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_delete45():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_delete46():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1


def test_delete47():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_delete48():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node5 = Node(0)
    node5.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_delete49():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_delete50():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_delete51():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0


def test_delete52():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_delete53():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node4 = Node(0)
    node4.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_delete54():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_delete55():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0


def test_delete56():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_delete57():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node3 = Node(0)
    node3.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_delete58():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0


def test_delete59():
    '''
    Self:
         <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1


def test_delete60():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node2 = Node(0)
    node2.key = 1
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_delete61():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head is None


def test_delete62():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 1


def test_delete63():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head is None


def test_append64():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_append65():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_append66():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_append67():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_append68():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_append69():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
         <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0


def test_prepend70():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node5
    node5.next = node2
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_prepend71():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node4
    node4.next = node2
    node4.prev = node3
    node3.next = node4
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_prepend72():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node3 = Node(0)
    node3.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node3
    node3.next = node2
    node3.prev = node1
    node1.next = node3
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_prepend73():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node1
    node2.prev = node1
    node1.next = node2
    node1.prev = node2
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_prepend74():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_prepend75():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
         <- 0 -> **
    '''
    # Input Creation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Repok check
    assert cdlinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert cdlinkedlist0.head.key == 0


