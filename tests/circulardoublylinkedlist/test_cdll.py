from cdll import *


def test_insert_after1():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_after2():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node3 = Node(0)
    node3.key = 0
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after3():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after4():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node5 = Node(0)
    node5.key = 0
    node5.next = node1
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node5
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_after5():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node5 = Node(1)
    node5.key = 1
    node5.next = node1
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node5
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_insert_after6():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node5 = Node(0)
    node5.key = 0
    node5.next = node1
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node5
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 1


def test_insert_after7():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_after8():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after9():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_after10():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_after11():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after12():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_after13():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_after14():
    '''
    Self:
         <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_after15():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_after16():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_insert_after17():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_insert_after18():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_insert_after19():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_after(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head is None


def test_insert_before1():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_before2():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_insert_before3():
    '''
    Self:
         <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_before4():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_before5():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_before6():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node5 = Node(0)
    node5.key = 0
    node5.next = node1
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node5
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 1


def test_insert_before7():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node5 = Node(1)
    node5.key = 1
    node5.next = node1
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node5
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_insert_before8():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node5 = Node(1)
    node5.key = 1
    node5.next = node1
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node5
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_insert_before9():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_before10():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_before11():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_before12():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_before13():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_before14():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_before15():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_insert_before16():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_insert_before17():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.insert_before(0, 0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head is None


def test_delete1():
    '''
    Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node3 = Node(0)
    node3.key = 0
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_delete2():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0


def test_delete3():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head is None


def test_delete4():
    '''
    Self:
         <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node3 = Node(0)
    node3.key = 0
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0


def test_delete5():
    '''
    Self:
         <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_delete6():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node4.next = node1
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node4
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0


def test_delete7():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_delete8():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_delete9():
    '''
    Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node1
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node3
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_delete10():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_delete11():
    '''
    Self:
         <- 1 ->  <- 1 -> **
    Return:
        None
    End Self:
         <- 1 ->  <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_delete12():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_delete13():
    '''
    Self:
         <- 1 -> **
    Return:
        None
    End Self:
         <- 1 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node1 = Node(1)
    node1.key = 1
    node1.next = node1
    node1.prev = node1
    cdlinkedlist0.head = node1
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_delete14():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
        <Empty list>
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head is None


def test_append1():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_append2():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_append3():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
         <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.append(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0


def test_prepend1():
    '''
    Self:
         <- 0 ->  <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_prepend2():
    '''
    Self:
         <- 0 -> **
    Return:
        None
    End Self:
         <- 0 ->  <- 0 -> **
    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_prepend3():
    '''
    Self:
        <Empty list>
    Return:
        None
    End Self:
         <- 0 -> **
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    cdlinkedlist0.head = None
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    returnv = cdlinkedlist0.prepend(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0


