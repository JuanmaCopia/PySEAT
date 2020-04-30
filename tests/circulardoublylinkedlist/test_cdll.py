from cdll import *


def test_insert_after_node1():
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
    node0 = Node(0)
    node0.key = 0
    node1 = Node(0)
    node1.key = 0
    node1.next = node0
    node1.prev = node0
    node0.next = node1
    node0.prev = node1
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_after_node2():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node2.next = node0
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node2
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after_node3():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node3 = Node(0)
    node3.key = 0
    node3.next = node0
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node3
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after_node4():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node4 = Node(0)
    node4.key = 0
    node4.next = node0
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node4
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 0


def test_insert_after_node5():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(1)
    node4.key = 1
    node4.next = node0
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node4
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 1


def test_insert_after_node6():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node4 = Node(0)
    node4.key = 0
    node4.next = node0
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node4
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.key == 1


def test_insert_after_node7():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node0
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node3
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_after_node8():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(0)
    node3.key = 0
    node3.next = node0
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node3
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 1
    assert cdlinkedlist0.head.prev.prev.key == 0


def test_insert_after_node9():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node3 = Node(1)
    node3.key = 1
    node3.next = node0
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node3
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1
    assert cdlinkedlist0.head.next.next.key == 1


def test_insert_after_node10():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node2.next = node0
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node2
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_after_node11():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(0)
    node2.key = 0
    node2.next = node0
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node2
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 0
    assert cdlinkedlist0.head.next.next.key == 0


def test_insert_after_node12():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node2.next = node0
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node2
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1
    assert cdlinkedlist0.head.prev.key == 1


def test_insert_after_node13():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node1.next = node0
    node1.prev = node0
    node0.next = node1
    node0.prev = node1
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_after_node14():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node1.next = node0
    node1.prev = node0
    node0.next = node1
    node0.prev = node1
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 0
    assert cdlinkedlist0.head.prev.key == 0


def test_insert_after_node15():
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
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node1.next = node0
    node1.prev = node0
    node0.next = node1
    node0.prev = node1
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1
    assert cdlinkedlist0.head.next.key == 1


def test_insert_after_node16():
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
    node0 = Node(1)
    node0.key = 1
    node0.next = node0
    node0.prev = node0
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_insert_after_node17():
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
    node0 = Node(0)
    node0.key = 0
    node0.next = node0
    node0.prev = node0
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 0
    assert cdlinkedlist0.head.next.key == 0


def test_insert_after_node18():
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
    node0 = Node(1)
    node0.key = 1
    node0.next = node0
    node0.prev = node0
    cdlinkedlist0.head = node0
    # Repok check
    assert cdlinkedlist0.repok()
    # Method call
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head.key == 1


def test_insert_after_node19():
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
    cdlinkedlist0.insert_after_node(0, 0)
    # Assertions
    # Repok check
    assert cdlinkedlist0.repok()
    assert cdlinkedlist0.head is None


