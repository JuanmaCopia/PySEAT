from avl import Node, AVL


def insert_test1():
    '''
    Self:
        
                  None <- node1: 0          
                 /                \         
        node1 <- node0: -1 node1 <- node2: 0
        /                \ /               \
        None                  None None                 None

    Return:
        None
    End Self:
        
                  .....None <- node1: 0.....          
                 /                          \         
        node1 <- node0: -1           node1 <- node2: 0
        /                \           /               \
        None        node0 <- node124: -1 None                 None
                /                  \                  

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 1
    node2 = Node(node1, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    node0 = Node(node1, -1)
    node0.data = -1
    node0.right = None
    node0.left = None
    node0.height = 0
    node0.parent = node1
    node1.left = node0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(-1)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    print('Test1: OK')


def insert_test2():
    '''
    Self:
        
                     None <- node1: 4294967296
                     /                       \
        node1 <- node0: 4294967295            None
        /                        \            
        None                          None            

    Return:
        None
    End Self:
        
                      None <- node2: 4294967295              
                     /                         \             
        node2 <- node0: 4294967295 node2 <- node1: 4294967296
        /                        \ /                        \
        None                          None None                          None

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 4294967296)
    node1.data = 4294967296
    node1.right = None
    node1.parent = None
    node1.height = 1
    node0 = Node(node1, 4294967295)
    node0.data = 4294967295
    node0.right = None
    node0.left = None
    node0.height = 0
    node0.parent = node1
    node1.left = node0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(4294967295)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 4294967295
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 4294967296
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 4294967295
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test2: OK')


def insert_test3():
    '''
    Self:
        
                 None <- node1: 0          
                /                \         
        node1 <- node2: 0 node1 <- node0: 0
        /               \ /               \
        None                 None None                 None

    Return:
        None
    End Self:
        
                 None <- node1: 0                    
                /                \                   
        node1 <- node2: 0 node1 <- node0: 0          
        /               \ /               \          
        None                 None None        node0 <- node124: 0
                                  /                 \

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 1
    node0 = Node(node1, 0)
    node0.data = 0
    node0.right = None
    node0.left = None
    node0.height = 0
    node0.parent = node1
    node1.right = node0
    node2 = Node(node1, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    print('Test3: OK')


def insert_test4():
    '''
    Self:
        
        None <- node1: 4294870719             
        /                       \             
        None            node1 <- node0: 4294870719
                    /                        \
                    None                          None

    Return:
        None
    End Self:
        
                      None <- node0: 4294870719              
                     /                         \             
        node0 <- node1: 4294870719 node0 <- node2: 4294870719
        /                        \ /                        \
        None                          None                           

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 4294870719)
    node1.data = 4294870719
    node1.left = None
    node1.parent = None
    node1.height = 1
    node0 = Node(node1, 4294870719)
    node0.data = 4294870719
    node0.right = None
    node0.left = None
    node0.height = 0
    node0.parent = node1
    node1.right = node0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(4294870719)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 4294870719
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 4294870719
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 4294870719
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test4: OK')


def insert_test5():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        
        CLOUD <- node1: 0
        /               \

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
    print('Test5: OK')


if __name__ == '__main__':
    insert_test1()
    insert_test2()
    insert_test3()
    insert_test4()
    insert_test5()
