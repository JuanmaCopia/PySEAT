from avl import Node, AVL


def insert_test1():
    '''
    Self:
        
                 None<- node0: 1
                 /             \
        (node0 <- node1: 1)     None
        /                 \     
        None                   None     

    Return:
        None
    End Self:
        
                  .None<- node1: 1..           
                 /                  \          
        (node1 <- node3: 0) (node1 <- node0: 1)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 1)
    node0.data = 1
    node0.right = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.left = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 1
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test1: OK')


def insert_test2():
    '''
    Self:
        
                 None<- node0: 1
                 /             \
        (node0 <- node1: 0)     None
        /                 \     
        None                   None     

    Return:
        None
    End Self:
        
                  .None<- node3: 0..           
                 /                  \          
        (node3 <- node1: 0) (node3 <- node0: 1)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 1)
    node0.data = 1
    node0.right = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.left = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test2: OK')


def insert_test3():
    '''
    Self:
        
        None<- node0: 0          
        /             \          
        None      (node0 <- node1: 0)
              /                 \
              None                   None

    Return:
        None
    End Self:
        
                  .None<- node1: 0..           
                 /                  \          
        (node1 <- node0: 0) (node1 <- node3: 0)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.left = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.right = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test3: OK')


def insert_test4():
    '''
    Self:
        
        None<- node0: 1
        /             \
        None               None

    Return:
        None
    End Self:
        
                 None<- node0: 1
                 /             \
        (node0 <- node2: 0)     None
        /                 \     
        None                   None     

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 1)
    node0.data = 1
    node0.right = None
    node0.left = None
    node0.parent = None
    node0.height = 0
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 1
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test4: OK')


def insert_test5():
    '''
    Self:
        
        None<- node0: 0          
        /             \          
        None      (node0 <- node1: 1)
              /                 \
              None                   None

    Return:
        None
    End Self:
        
                  .None<- node3: 0..           
                 /                  \          
        (node3 <- node0: 0) (node3 <- node1: 1)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.left = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.right = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test5: OK')


def insert_test6():
    '''
    Self:
        
        None<- node0: 0          
        /             \          
        None      (node0 <- node1: 1)
              /                 \
              None                   None

    Return:
        None
    End Self:
        
                  .None<- node3: 0..           
                 /                  \          
        (node3 <- node0: 0) (node3 <- node1: 1)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.left = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.right = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test6: OK')


def insert_test7():
    '''
    Self:
        
        None<- node0: 0          
        /             \          
        None      (node0 <- node1: 0)
              /                 \
              None                   None

    Return:
        None
    End Self:
        
                  .None<- node1: 0..           
                 /                  \          
        (node1 <- node0: 0) (node1 <- node3: 0)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.left = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.right = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test7: OK')


def insert_test8():
    '''
    Self:
        
        None<- node0: 0          
        /             \          
        None      (node0 <- node1: 0)
              /                 \
              None                   None

    Return:
        None
    End Self:
        
                  .None<- node1: 0..           
                 /                  \          
        (node1 <- node0: 0) (node1 <- node3: 0)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.left = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.right = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test8: OK')


def insert_test9():
    '''
    Self:
        
                 None<- node0: 0
                 /             \
        (node0 <- node1: 0)     None
        /                 \     
        None                   None     

    Return:
        None
    End Self:
        
                  .None<- node0: 0..           
                 /                  \          
        (node0 <- node1: 0) (node0 <- node3: 0)
        /                 \ /                 \
        None                   None None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.right = None
    node0.parent = None
    node0.height = 0
    node1 = Node(node0, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.height = 0
    node1.parent = node0
    node0.left = node1
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test9: OK')


def insert_test10():
    '''
    Self:
        
        None<- node0: 0
        /             \
        None               None

    Return:
        None
    End Self:
        
        None<- node0: 0          
        /             \          
        None      (node0 <- node2: 0)
              /                 \
              None                   None

    '''
    # Self Generation
    avl0 = AVL()
    node0 = Node(None, 0)
    node0.data = 0
    node0.right = None
    node0.left = None
    node0.parent = None
    node0.height = 0
    avl0.root = node0
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    print('Test10: OK')


def insert_test11():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        
        CLOUD<- node1: 0
        /              \
        None                None

    '''
    # Self Generation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    print('Test11: OK')


if __name__ == '__main__':
    insert_test1()
    insert_test2()
    insert_test3()
    insert_test4()
    insert_test5()
    insert_test6()
    insert_test7()
    insert_test8()
    insert_test9()
    insert_test10()
    insert_test11()
