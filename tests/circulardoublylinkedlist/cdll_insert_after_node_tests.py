from cdll import Node, CDLinkedList


def insert_after_node_test1():
    '''
    Self:
        (node642 <- node0: 0 -> node1) (node0 <- node1: 0 -> node643) (node1 <- node643: 0 -> node644) (node643 <- node644: 0 -> node645) (node644 <- node645: 0 -> node642) (node645 <- node642: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node642 <- node0: 0 -> node646) (node0 <- node646: 0 -> node1) (node646 <- node1: 0 -> node643) (node1 <- node643: 0 -> node644) (node643 <- node644: 0 -> node645) (node644 <- node645: 0 -> node642) (node645 <- node642: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(0)
    node0.key = 0
    node1 = Node(0)
    node1.key = 0
    node643 = Node(0)
    node643.key = 0
    node644 = Node(0)
    node644.key = 0
    node645 = Node(0)
    node645.key = 0
    node642 = Node(0)
    node642.key = 0
    node642.next = node0
    node642.prev = node645
    node645.next = node642
    node645.prev = node644
    node644.next = node645
    node644.prev = node643
    node643.next = node644
    node643.prev = node1
    node1.next = node643
    node1.prev = node0
    node0.next = node1
    node0.prev = node642
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
    assert cdlinkedlist0.head.next.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.prev.key == 0
    print('Test1: OK')


def insert_after_node_test2():
    '''
    Self:
        (node645 <- node0: 1 -> node1) (node0 <- node1: 0 -> node2) (node1 <- node2: 0 -> node646) (node2 <- node646: 0 -> node647) (node646 <- node647: 0 -> node645) (node647 <- node645: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node645 <- node0: 1 -> node1) (node0 <- node1: 0 -> node648) (node1 <- node648: 0 -> node2) (node648 <- node2: 0 -> node646) (node2 <- node646: 0 -> node647) (node646 <- node647: 0 -> node645) (node647 <- node645: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node646 = Node(0)
    node646.key = 0
    node647 = Node(0)
    node647.key = 0
    node645 = Node(0)
    node645.key = 0
    node645.next = node0
    node645.prev = node647
    node647.next = node645
    node647.prev = node646
    node646.next = node647
    node646.prev = node2
    node2.next = node646
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node645
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
    assert cdlinkedlist0.head.next.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.prev.key == 0
    print('Test2: OK')


def insert_after_node_test3():
    '''
    Self:
        (node668 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node3) (node2 <- node3: 0 -> node669) (node3 <- node669: 0 -> node670) (node669 <- node670: 0 -> node668) (node670 <- node668: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node668 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node671) (node2 <- node671: 0 -> node3) (node671 <- node3: 0 -> node669) (node3 <- node669: 0 -> node670) (node669 <- node670: 0 -> node668) (node670 <- node668: 0 -> node0) **node0
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
    node669 = Node(0)
    node669.key = 0
    node670 = Node(0)
    node670.key = 0
    node668 = Node(0)
    node668.key = 0
    node668.next = node0
    node668.prev = node670
    node670.next = node668
    node670.prev = node669
    node669.next = node670
    node669.prev = node3
    node3.next = node669
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node668
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
    assert cdlinkedlist0.head.next.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.next.key == 0
    print('Test3: OK')


def insert_after_node_test4():
    '''
    Self:
        (node610 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node4) (node3 <- node4: 0 -> node611) (node4 <- node611: 0 -> node610) (node611 <- node610: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node610 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node612) (node3 <- node612: 0 -> node4) (node612 <- node4: 0 -> node611) (node4 <- node611: 0 -> node610) (node611 <- node610: 0 -> node0) **node0
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
    node611 = Node(0)
    node611.key = 0
    node610 = Node(0)
    node610.key = 0
    node610.next = node0
    node610.prev = node611
    node611.next = node610
    node611.prev = node4
    node4.next = node611
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node610
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
    assert cdlinkedlist0.head.prev.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.next.key == 0
    print('Test4: OK')


def insert_after_node_test5():
    '''
    Self:
        (node625 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node5) (node4 <- node5: 0 -> node626) (node5 <- node626: 0 -> node625) (node626 <- node625: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node625 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node627) (node4 <- node627: 0 -> node5) (node627 <- node5: 0 -> node626) (node5 <- node626: 0 -> node625) (node626 <- node625: 0 -> node0) **node0
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
    node5 = Node(0)
    node5.key = 0
    node626 = Node(0)
    node626.key = 0
    node625 = Node(0)
    node625.key = 0
    node625.next = node0
    node625.prev = node626
    node626.next = node625
    node626.prev = node5
    node5.next = node626
    node5.prev = node4
    node4.next = node5
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node625
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
    assert cdlinkedlist0.head.prev.prev.prev.key == 0
    assert cdlinkedlist0.head.next.next.next.next.key == 0
    assert cdlinkedlist0.head.prev.prev.prev.prev.key == 0
    print('Test5: OK')


def insert_after_node_test6():
    '''
    Self:
        (node3 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node8 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node8) (node3 <- node8: 0 -> node0) **node0
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
    print('Test6: OK')


def insert_after_node_test7():
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
    print('Test7: OK')


def insert_after_node_test8():
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
    print('Test8: OK')


def insert_after_node_test9():
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
    print('Test9: OK')


def insert_after_node_test10():
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
    print('Test10: OK')


def insert_after_node_test11():
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
    print('Test11: OK')


def insert_after_node_test12():
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
    print('Test12: OK')


def insert_after_node_test13():
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
    print('Test13: OK')


def insert_after_node_test14():
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
    print('Test14: OK')


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
