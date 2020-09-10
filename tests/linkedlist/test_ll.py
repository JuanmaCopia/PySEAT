from ll import *
import pytest


def test_is_ordered1():
    '''
    Self:
        0 -> 0 -> 0 -> 0 -> 0
    Return:
        False
    End Self:
        0 -> 0 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node5 = Node(0)
    node5.elem = 0
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.next is None


def test_is_ordered2():
    '''
    Self:
        -1 -> 0 -> 0 -> 0 -> 0
    Return:
        False
    End Self:
        -1 -> 0 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node5 = Node(0)
    node5.elem = 0
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == -1
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.next is None


def test_is_ordered3():
    '''
    Self:
        -2 -> -1 -> 0 -> 0 -> 0
    Return:
        False
    End Self:
        -2 -> -1 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -2
    node2 = Node(0)
    node2.elem = -1
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node5 = Node(0)
    node5.elem = 0
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == -2
    assert linkedlist0.head.next.elem == -1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.next is None


def test_is_ordered4():
    '''
    Self:
        -2 -> -1 -> 0 -> 1 -> 1
    Return:
        False
    End Self:
        -2 -> -1 -> 0 -> 1 -> 1
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -2
    node2 = Node(0)
    node2.elem = -1
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 1
    node5 = Node(0)
    node5.elem = 1
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == -2
    assert linkedlist0.head.next.elem == -1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 1
    assert linkedlist0.head.next.next.next.next.elem == 1
    assert linkedlist0.head.next.next.next.next.next is None


def test_is_ordered5():
    '''
    Self:
        -2 -> -1 -> 0 -> 1 -> 2
    Return:
        True
    End Self:
        -2 -> -1 -> 0 -> 1 -> 2
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -2
    node2 = Node(0)
    node2.elem = -1
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 1
    node5 = Node(0)
    node5.elem = 2
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == True
    assert linkedlist0.head.elem == -2
    assert linkedlist0.head.next.elem == -1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 1
    assert linkedlist0.head.next.next.next.next.elem == 2
    assert linkedlist0.head.next.next.next.next.next is None


def test_is_ordered6():
    '''
    Self:
        0 -> 0 -> 0 -> 0
    Return:
        False
    End Self:
        0 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node4.next = None
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next is None


def test_is_ordered7():
    '''
    Self:
        -1 -> 0 -> 0 -> 0
    Return:
        False
    End Self:
        -1 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node4.next = None
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == -1
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next is None


def test_is_ordered8():
    '''
    Self:
        -2 -> -1 -> 0 -> 0
    Return:
        False
    End Self:
        -2 -> -1 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -2
    node2 = Node(0)
    node2.elem = -1
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node4.next = None
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == -2
    assert linkedlist0.head.next.elem == -1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next is None


def test_is_ordered9():
    '''
    Self:
        -2 -> -1 -> 0 -> 1
    Return:
        True
    End Self:
        -2 -> -1 -> 0 -> 1
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -2
    node2 = Node(0)
    node2.elem = -1
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 1
    node4.next = None
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == True
    assert linkedlist0.head.elem == -2
    assert linkedlist0.head.next.elem == -1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 1
    assert linkedlist0.head.next.next.next.next is None


def test_is_ordered10():
    '''
    Self:
        0 -> 0 -> 0
    Return:
        False
    End Self:
        0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node3.next = None
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next is None


def test_is_ordered11():
    '''
    Self:
        -1 -> 0 -> 0
    Return:
        False
    End Self:
        -1 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node3.next = None
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == -1
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next is None


def test_is_ordered12():
    '''
    Self:
        -1 -> 0 -> 1
    Return:
        True
    End Self:
        -1 -> 0 -> 1
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 1
    node3.next = None
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == True
    assert linkedlist0.head.elem == -1
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 1
    assert linkedlist0.head.next.next.next is None


def test_is_ordered13():
    '''
    Self:
        0 -> 0
    Return:
        False
    End Self:
        0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node2.next = None
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == False
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next is None


def test_is_ordered14():
    '''
    Self:
        -1 -> 0
    Return:
        True
    End Self:
        -1 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = -1
    node2 = Node(0)
    node2.elem = 0
    node2.next = None
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == True
    assert linkedlist0.head.elem == -1
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next is None


def test_is_ordered15():
    '''
    Self:
        0
    Return:
        True
    End Self:
        0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node1.next = None
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == True
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next is None


def test_is_ordered16():
    '''
    Self:
        EmptyList
    Return:
        True
    End Self:
        EmptyList
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    linkedlist0.head = None
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.is_ordered()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv == True
    assert linkedlist0.head is None


def test_swap_node1():
    '''
    Self:
        1 -> 0 -> 0 -> 0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 1 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node5 = Node(0)
    node5.elem = 0
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next.elem == 0
    assert returnv.next.next.next.next.elem == 0
    assert returnv.next.next.next.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.next is None


def test_swap_node2():
    '''
    Self:
        0 -> 0 -> 0 -> 0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 0 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node5 = Node(0)
    node5.elem = 0
    node5.next = None
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 0
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next.elem == 0
    assert returnv.next.next.next.next.elem == 0
    assert returnv.next.next.next.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next.next is None


def test_swap_node3():
    '''
    Self:
        1 -> 0 -> 0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 1 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node4.next = None
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next.elem == 0
    assert returnv.next.next.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next is None


def test_swap_node4():
    '''
    Self:
        0 -> 0 -> 0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node4 = Node(0)
    node4.elem = 0
    node4.next = None
    node3.next = node4
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 0
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next.elem == 0
    assert returnv.next.next.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next.elem == 0
    assert linkedlist0.head.next.next.next.next is None


def test_swap_node5():
    '''
    Self:
        1 -> 0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 1 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 1
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node3.next = None
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next is None


def test_swap_node6():
    '''
    Self:
        0 -> 0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node3 = Node(0)
    node3.elem = 0
    node3.next = None
    node2.next = node3
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 0
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next is None


def test_swap_node7():
    '''
    Self:
        1 -> 0
    Return:
        node(0)
    End Self:
        0 -> 1
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 1
    node2 = Node(0)
    node2.elem = 0
    node2.next = None
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next is None


def test_swap_node8():
    '''
    Self:
        0 -> 0
    Return:
        node(0)
    End Self:
        0 -> 0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node2.next = None
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 0
    assert returnv.next.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next is None


def test_swap_node9():
    '''
    Self:
        0
    Return:
        node(0)
    End Self:
        0
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node1.next = None
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next is None
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next is None


def test_swap_node10():
    '''
    Self:
        EmptyList
    Return:
        None
    End Self:
        EmptyList
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    linkedlist0.head = None
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv is None
    assert linkedlist0.head is None


