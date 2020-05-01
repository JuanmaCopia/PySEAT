from llnr import *


def test_swap_node1():
    '''
    Self:
        1 -> 0 -> 0 -> None
    Return:
        0 -> 1 -> 0 -> None
    End Self:
        0 -> 1 -> 0 -> None
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node1 = Node(1)
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
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next is None
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next is None


def test_swap_node2():
    '''
    Self:
        1 -> 0 -> None
    Return:
        0 -> 1 -> None
    End Self:
        0 -> 1 -> None
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node1 = Node(1)
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
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next is None
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next is None


def test_swap_node3():
    '''
    Self:
        1 -> 0 ->  **1
    Return:
        0 -> 1 ->  **1
    End Self:
        0 -> 1 ->  **1
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node1 = Node(1)
    node1.elem = 1
    node2 = Node(0)
    node2.elem = 0
    node2.next = node1
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1


def test_swap_node4():
    '''
    Self:
        1 -> 0 ->  **0
    Return:
        0 -> 1 ->  **0
    End Self:
        0 -> 1 ->  **0
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node1 = Node(1)
    node1.elem = 1
    node2 = Node(0)
    node2.elem = 0
    node2.next = node2
    node1.next = node2
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1


def test_swap_node5():
    '''
    Self:
        0 -> 0 -> None
    Return:
        0 -> 0 -> None
    End Self:
        0 -> 0 -> None
    '''
    # Self Generation
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
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 0
    assert returnv.next.next is None
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 0
    assert linkedlist0.head.next.next is None


def test_swap_node6():
    '''
    Self:
        0 -> None
    Return:
        0 -> None
    End Self:
        0 -> None
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node1.next = None
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next is None
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next is None


def test_swap_node7():
    '''
    Self:
        0 ->  **0
    Return:
        0 ->  **0
    End Self:
        0 ->  **0
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node1 = Node(0)
    node1.elem = 0
    node1.next = node1
    linkedlist0.head = node1
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv.elem == 0
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0


def test_swap_node8():
    '''
    Self:
        EmptyList
    Return:
        None
    End Self:
        EmptyList
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    linkedlist0.head = None
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv is None
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head is None


