from llnr import Node, LinkedList


def swap_node_test1():
    '''
    Self:
         node0(1) -> node1(0) -> node2(0) -> None
    Return:
         node1(0) -> node0(1) -> node2(0) -> None
    End Self:
         node1(0) -> node0(1) -> node2(0) -> None
    '''
    # Self Generation
    node0 = Node(1)
    node0.elem = 1
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node2.next = None
    node1.next = node2
    node0.next = node1
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
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
    print('Test1: OK')


def swap_node_test2():
    '''
    Self:
         node0(1) -> node1(0) -> None
    Return:
         node1(0) -> node0(1) -> None
    End Self:
         node1(0) -> node0(1) -> None
    '''
    # Self Generation
    node0 = Node(1)
    node0.elem = 1
    node1 = Node(0)
    node1.elem = 0
    node1.next = None
    node0.next = node1
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
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
    print('Test2: OK')


def swap_node_test3():
    '''
    Self:
         node0(1) -> node1(0) -> **node0(1)
    Return:
         node1(0) -> node0(1) -> **node0(1)
    End Self:
         node1(0) -> node0(1) -> **node0(1)
    '''
    # Self Generation
    node0 = Node(1)
    node0.elem = 1
    node1 = Node(0)
    node1.elem = 0
    node1.next = node0
    node0.next = node1
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
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
    print('Test3: OK')


def swap_node_test4():
    '''
    Self:
         node0(1) -> node1(0) -> **node1(0)
    Return:
         node1(0) -> node0(1) -> **node1(0)
    End Self:
         node1(0) -> node0(1) -> **node1(0)
    '''
    # Self Generation
    node0 = Node(1)
    node0.elem = 1
    node1 = Node(0)
    node1.elem = 0
    node1.next = node1
    node0.next = node1
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
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
    print('Test4: OK')


def swap_node_test5():
    '''
    Self:
         node0(0) -> node1(0) -> None
    Return:
         node0(0) -> node1(0) -> None
    End Self:
         node0(0) -> node1(0) -> None
    '''
    # Self Generation
    node0 = Node(0)
    node0.elem = 0
    node1 = Node(0)
    node1.elem = 0
    node1.next = None
    node0.next = node1
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
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
    print('Test5: OK')


def swap_node_test6():
    '''
    Self:
         node0(0) -> None
    Return:
         node0(0) -> None
    End Self:
         node0(0) -> None
    '''
    # Self Generation
    node0 = Node(0)
    node0.elem = 0
    node0.next = None
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
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
    print('Test6: OK')


def swap_node_test7():
    '''
    Self:
         node0(0) -> **node0(0)
    Return:
         node0(0) -> **node0(0)
    End Self:
         node0(0) -> **node0(0)
    '''
    # Self Generation
    node0 = Node(0)
    node0.elem = 0
    node0.next = node0
    linkedlist0 = LinkedList(node0)
    linkedlist0.head = node0
    # Repok check
    assert linkedlist0.repok()
    
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv.elem == 0
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    print('Test7: OK')


def swap_node_test8():
    '''
    Self:
        EmptyList
    Return:
        None
    End Self:
        EmptyList
    '''
    # Self Generation
    linkedlist0 = LinkedList(None)
    linkedlist0.head = None
    # Repok check
    assert linkedlist0.repok()
    
    # Method call
    linkedlist0.swap_node()
    # Assertions
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head is None
    print('Test8: OK')


if __name__ == '__main__':
    swap_node_test1()
    swap_node_test2()
    swap_node_test3()
    swap_node_test4()
    swap_node_test5()
    swap_node_test6()
    swap_node_test7()
    swap_node_test8()
