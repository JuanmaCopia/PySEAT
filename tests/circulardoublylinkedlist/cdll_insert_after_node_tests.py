from cdll import Node, CDLinkedList


def insert_after_node_test1():
    '''
    Self:
        (node641 <- node0: 0 -> node1) (node0 <- node1: 0 -> node642) (node1 <- node642: 0 -> node643) (node642 <- node643: 0 -> node644) (node643 <- node644: 0 -> node641) (node644 <- node641: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node641 <- node0: 0 -> node646) (node0 <- node646: 0 -> node1) (node646 <- node1: 0 -> node642) (node1 <- node642: 0 -> node643) (node642 <- node643: 0 -> node644) (node643 <- node644: 0 -> node641) (node644 <- node641: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(0)
    node0.key = 0
    node1 = Node(0)
    node1.key = 0
    node642 = Node(0)
    node642.key = 0
    node643 = Node(0)
    node643.key = 0
    node644 = Node(0)
    node644.key = 0
    node641 = Node(0)
    node641.key = 0
    node641.next = node0
    node641.prev = node644
    node644.next = node641
    node644.prev = node643
    node643.next = node644
    node643.prev = node642
    node642.next = node643
    node642.prev = node1
    node1.next = node642
    node1.prev = node0
    node0.next = node1
    node0.prev = node641
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
        (node644 <- node0: 1 -> node1) (node0 <- node1: 0 -> node2) (node1 <- node2: 0 -> node645) (node2 <- node645: 0 -> node646) (node645 <- node646: 0 -> node644) (node646 <- node644: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node644 <- node0: 1 -> node1) (node0 <- node1: 0 -> node648) (node1 <- node648: 0 -> node2) (node648 <- node2: 0 -> node645) (node2 <- node645: 0 -> node646) (node645 <- node646: 0 -> node644) (node646 <- node644: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(0)
    node1.key = 0
    node2 = Node(0)
    node2.key = 0
    node645 = Node(0)
    node645.key = 0
    node646 = Node(0)
    node646.key = 0
    node644 = Node(0)
    node644.key = 0
    node644.next = node0
    node644.prev = node646
    node646.next = node644
    node646.prev = node645
    node645.next = node646
    node645.prev = node2
    node2.next = node645
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node644
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
        (node667 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node3) (node2 <- node3: 0 -> node668) (node3 <- node668: 0 -> node669) (node668 <- node669: 0 -> node667) (node669 <- node667: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node667 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 0 -> node671) (node2 <- node671: 0 -> node3) (node671 <- node3: 0 -> node668) (node3 <- node668: 0 -> node669) (node668 <- node669: 0 -> node667) (node669 <- node667: 0 -> node0) **node0
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
    node668 = Node(0)
    node668.key = 0
    node669 = Node(0)
    node669.key = 0
    node667 = Node(0)
    node667.key = 0
    node667.next = node0
    node667.prev = node669
    node669.next = node667
    node669.prev = node668
    node668.next = node669
    node668.prev = node3
    node3.next = node668
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node667
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
        (node609 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node4) (node3 <- node4: 0 -> node610) (node4 <- node610: 0 -> node609) (node610 <- node609: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node609 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 0 -> node612) (node3 <- node612: 0 -> node4) (node612 <- node4: 0 -> node610) (node4 <- node610: 0 -> node609) (node610 <- node609: 0 -> node0) **node0
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
    node610 = Node(0)
    node610.key = 0
    node609 = Node(0)
    node609.key = 0
    node609.next = node0
    node609.prev = node610
    node610.next = node609
    node610.prev = node4
    node4.next = node610
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node609
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
        (node624 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node5) (node4 <- node5: 0 -> node625) (node5 <- node625: 0 -> node624) (node625 <- node624: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node624 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 0 -> node627) (node4 <- node627: 0 -> node5) (node627 <- node5: 0 -> node625) (node5 <- node625: 0 -> node624) (node625 <- node624: 0 -> node0) **node0
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
    node625 = Node(0)
    node625.key = 0
    node624 = Node(0)
    node624.key = 0
    node624.next = node0
    node624.prev = node625
    node625.next = node624
    node625.prev = node5
    node5.next = node625
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
    node0.prev = node624
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
        (node609 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node610) (node4 <- node610: 0 -> node609) (node610 <- node609: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node609 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node4) (node3 <- node4: 1 -> node610) (node4 <- node610: 0 -> node612) (node610 <- node612: 0 -> node609) (node612 <- node609: 0 -> node0) **node0
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
    node610 = Node(0)
    node610.key = 0
    node609 = Node(0)
    node609.key = 0
    node609.next = node0
    node609.prev = node610
    node610.next = node609
    node610.prev = node4
    node4.next = node610
    node4.prev = node3
    node3.next = node4
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node609
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
    assert cdlinkedlist0.head.next.next.next.next.key == 1
    print('Test6: OK')


def insert_after_node_test7():
    '''
    Self:
        (node667 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node668) (node3 <- node668: 0 -> node669) (node668 <- node669: 0 -> node667) (node669 <- node667: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node667 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node3) (node2 <- node3: 1 -> node668) (node3 <- node668: 0 -> node671) (node668 <- node671: 0 -> node669) (node671 <- node669: 0 -> node667) (node669 <- node667: 0 -> node0) **node0
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
    node668 = Node(0)
    node668.key = 0
    node669 = Node(0)
    node669.key = 0
    node667 = Node(0)
    node667.key = 0
    node667.next = node0
    node667.prev = node669
    node669.next = node667
    node669.prev = node668
    node668.next = node669
    node668.prev = node3
    node3.next = node668
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node667
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
    print('Test7: OK')


def insert_after_node_test8():
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
    print('Test8: OK')


def insert_after_node_test9():
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
    print('Test9: OK')


def insert_after_node_test10():
    '''
    Self:
        (node644 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node645) (node2 <- node645: 0 -> node646) (node645 <- node646: 0 -> node644) (node646 <- node644: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node644 <- node0: 1 -> node1) (node0 <- node1: 1 -> node2) (node1 <- node2: 1 -> node645) (node2 <- node645: 0 -> node648) (node645 <- node648: 0 -> node646) (node648 <- node646: 0 -> node644) (node646 <- node644: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node2 = Node(1)
    node2.key = 1
    node645 = Node(0)
    node645.key = 0
    node646 = Node(0)
    node646.key = 0
    node644 = Node(0)
    node644.key = 0
    node644.next = node0
    node644.prev = node646
    node646.next = node644
    node646.prev = node645
    node645.next = node646
    node645.prev = node2
    node2.next = node645
    node2.prev = node1
    node1.next = node2
    node1.prev = node0
    node0.next = node1
    node0.prev = node644
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
    print('Test10: OK')


def insert_after_node_test11():
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
    print('Test11: OK')


def insert_after_node_test12():
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
    print('Test12: OK')


def insert_after_node_test13():
    '''
    Self:
        (node641 <- node0: 1 -> node1) (node0 <- node1: 1 -> node642) (node1 <- node642: 0 -> node643) (node642 <- node643: 0 -> node644) (node643 <- node644: 0 -> node641) (node644 <- node641: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node641 <- node0: 1 -> node1) (node0 <- node1: 1 -> node642) (node1 <- node642: 0 -> node646) (node642 <- node646: 0 -> node643) (node646 <- node643: 0 -> node644) (node643 <- node644: 0 -> node641) (node644 <- node641: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node1 = Node(1)
    node1.key = 1
    node642 = Node(0)
    node642.key = 0
    node643 = Node(0)
    node643.key = 0
    node644 = Node(0)
    node644.key = 0
    node641 = Node(0)
    node641.key = 0
    node641.next = node0
    node641.prev = node644
    node644.next = node641
    node644.prev = node643
    node643.next = node644
    node643.prev = node642
    node642.next = node643
    node642.prev = node1
    node1.next = node642
    node1.prev = node0
    node0.next = node1
    node0.prev = node641
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
    print('Test13: OK')


def insert_after_node_test14():
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
    print('Test14: OK')


def insert_after_node_test15():
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
    print('Test15: OK')


def insert_after_node_test16():
    '''
    Self:
        (node612 <- node0: 1 -> node613) (node0 <- node613: 0 -> node614) (node613 <- node614: 0 -> node615) (node614 <- node615: 0 -> node612) (node615 <- node612: 0 -> node0) **node0
    Return:
        None
    End Self:
        (node612 <- node0: 1 -> node613) (node0 <- node613: 0 -> node617) (node613 <- node617: 0 -> node614) (node617 <- node614: 0 -> node615) (node614 <- node615: 0 -> node612) (node615 <- node612: 0 -> node0) **node0
    '''
    # Self Generation
    cdlinkedlist0 = CDLinkedList()
    node0 = Node(1)
    node0.key = 1
    node613 = Node(0)
    node613.key = 0
    node614 = Node(0)
    node614.key = 0
    node615 = Node(0)
    node615.key = 0
    node612 = Node(0)
    node612.key = 0
    node612.next = node0
    node612.prev = node615
    node615.next = node612
    node615.prev = node614
    node614.next = node615
    node614.prev = node613
    node613.next = node614
    node613.prev = node0
    node0.next = node613
    node0.prev = node612
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
    print('Test16: OK')


def insert_after_node_test17():
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
    print('Test17: OK')


def insert_after_node_test18():
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
    print('Test18: OK')


def insert_after_node_test19():
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
    print('Test19: OK')


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
