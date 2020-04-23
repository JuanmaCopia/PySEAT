from cdll import Node, CDLinkedList


def insert_after_node_test1():
    '''
    Self:
        (node40 <- node0: 0 -> node1) (node0 <- node1: 0 -> node41) (node1 <- node41: 0 -> node40) (node41 <- node40: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node40 <- node0: 0 -> node43) (node0 <- node43: 0 -> node1) (node43 <- node1: 0 -> node41) (node1 <- node41: 0 -> node40) (node41 <- node40: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(0)
    node0.key = 0
    node1 = Node(0)
    node1.key = 0
    node41 = Node(0)
    node41.key = 0
    node40 = Node(0)
    node40.key = 0
    node40.next = node0
    node40.prev = node41
    node41.next = node40
    node41.prev = node1
    node1.next = node41
    node1.prev = node0
    node0.next = node1
    node0.prev = node40
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
    assert cdlinkedlist0.head.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.key == 0
    print('Test1: OK')


def insert_after_node_test2():
    '''
    Self:
        (node26 <- node0: 1 -> node1) (node0 <- node1: 0 -> node2) (node1 <- node2: 0 -> node26) (node2 <- node26: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node26 <- node0: 1 -> node1) (node0 <- node1: 0 -> node28) (node1 <- node28: 0 -> node2) (node28 <- node2: 0 -> node26) (node2 <- node26: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node26 = Node(0)
    node26.key = 0
    node26.next = node0
    node26.prev = node2
    node2.next = node26
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node26
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
    assert cdlinkedlist0.head.prev.prev.key == 0
    print('Test2: OK')


def insert_after_node_test3():
    '''
    Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node3) (node2 <- node3: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node5) (node2 <- node5: 0 -> node3) (node5 <- node3: 0 -> node0) **node0
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
    print('Test3: OK')


def insert_after_node_test4():
    '''
    Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node4) (node3 <- node4: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node6) (node3 <- node6: 0 -> node4) (node6 <- node4: 0 -> node0) **node0
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
    print('Test4: OK')


def insert_after_node_test5():
    '''
    Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node0) **node0
    Return:
        None
    End Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node0) **node0
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
    print('Test5: OK')


def insert_after_node_test6():
    '''
    Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node6 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node6) (node4 <- node6: 0 -> node0) **node0
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
    print('Test6: OK')


def insert_after_node_test7():
    '''
    Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node0) **node0
    Return:
        None
    End Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node0) **node0
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
    print('Test7: OK')


def insert_after_node_test8():
    '''
    Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node0) **node0
    Return:
        None
    End Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node0) **node0
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
    print('Test8: OK')


def insert_after_node_test9():
    '''
    Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node5 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node5) (node3 <- node5: 0 -> node0) **node0
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
    print('Test9: OK')


def insert_after_node_test10():
    '''
    Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node0) **node0
    Return:
        None
    End Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node0) **node0
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
    print('Test10: OK')


def insert_after_node_test11():
    '''
    Self:
        (node26 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node26) (node2 <- node26: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node28 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node26) (node2 <- node26: 0 -> node28) (node26 <- node28: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node26 = Node(0)
    node26.key = 0
    node26.next = node0
    node26.prev = node2
    node2.next = node26
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node26
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
    print('Test11: OK')


def insert_after_node_test12():
    '''
    Self:
        (node2 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node6 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node6) (node2 <- node6: 0 -> node0) **node0
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
    print('Test12: OK')


def insert_after_node_test13():
    '''
    Self:
        (node2 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node0) **node0
    Return:
        None
    End Self:
        (node2 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node0) **node0
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
    print('Test13: OK')


def insert_after_node_test14():
    '''
    Self:
        (node40 <- node0: 1 -> node1) (node0 <- node1: 1 -> node41) (node1 <- node41: 0 -> node40) (node41 <- node40: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node40 <- node0: 1 -> node1) (node0 <- node1: 1 -> node41) (node1 <- node41: 0 -> node43) (node41 <- node43: 0 -> node40) (node43 <- node40: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node41 = Node(0)
    node41.key = 0
    node40 = Node(0)
    node40.key = 0
    node40.next = node0
    node40.prev = node41
    node41.next = node40
    node41.prev = node1
    node1.next = node41
    node1.prev = node0
    node0.next = node1
    node0.prev = node40
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
    print('Test14: OK')


def insert_after_node_test15():
    '''
    Self:
        (node1 <- node0: 1 -> node1) (node0 <- node1: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node4 <- node0: 1 -> node1) (node0 <- node1: 0 -> node4) (node1 <- node4: 0 -> node0) **node0
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
    print('Test15: OK')


def insert_after_node_test16():
    '''
    Self:
        (node1 <- node0: 1 -> node1) (node0 <- node1: 1 -> node0) **node0
    Return:
        None
    End Self:
        (node1 <- node0: 1 -> node1) (node0 <- node1: 1 -> node0) **node0
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
    print('Test16: OK')


def insert_after_node_test17():
    '''
    Self:
        (node46 <- node0: 1 -> node47) (node0 <- node47: 0 -> node48) (node47 <- node48: 0 -> node46) (node48 <- node46: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node46 <- node0: 1 -> node47) (node0 <- node47: 0 -> node50) (node47 <- node50: 0 -> node48) (node50 <- node48: 0 -> node46) (node48 <- node46: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node47 = Node(0)
    node47.key = 0
    node48 = Node(0)
    node48.key = 0
    node46 = Node(0)
    node46.key = 0
    node46.next = node0
    node46.prev = node48
    node48.next = node46
    node48.prev = node47
    node47.next = node48
    node47.prev = node0
    node0.next = node47
    node0.prev = node46
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
    assert cdlinkedlist0.head.prev.prev.key == 0
    print('Test17: OK')


def insert_after_node_test18():
    '''
    Self:
        (node0 <- node0: 0 -> node0) 
    Return:
        None
    End Self:
        (node2 <- node0: 0 -> node2) (node0 <- node2: 0 -> node0) **node0
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
    print('Test18: OK')


def insert_after_node_test19():
    '''
    Self:
        (node0 <- node0: 1 -> node0) 
    Return:
        None
    End Self:
        (node0 <- node0: 1 -> node0) 
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
    print('Test19: OK')


def insert_after_node_test20():
    '''
    Self:
        Empty
    Return:
        None
    End Self:
        Empty
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
    print('Test20: OK')


if __name__ == '__main__':
    insert_after_node_test1()
    insert_after_node_test2()
    insert_after_node_test3()
    insert_after_node_test4()
    insert_after_node_test5()
    insert_after_node_test6()
    insert_after_node_test7()
    insert_after_node_test8()
    insert_after_node_test9()
    insert_after_node_test10()
    insert_after_node_test11()
    insert_after_node_test12()
    insert_after_node_test13()
    insert_after_node_test14()
    insert_after_node_test15()
    insert_after_node_test16()
    insert_after_node_test17()
    insert_after_node_test18()
    insert_after_node_test19()
    insert_after_node_test20()
