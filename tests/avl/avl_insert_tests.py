from avl import Node, AVL


def insert_test1():
    '''
    Self:
        
                     None <- node1: 4294753519
                     /                       \
        node1 <- node0: 4294753518            None
        /                        \            
        None                          None            

    Return:
        None
    End Self:
        
                      None <- node2: 4294753518              
                     /                         \             
        node2 <- node0: 4294753518 node2 <- node1: 4294753519
        /                        \ /                        \
        None                          None None                          None

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 4294753519)
    node1.data = 4294753519
    node1.right = None
    node1.parent = None
    node1.height = 1
    node0 = Node(node1, 4294753518)
    node0.data = 4294753518
    node0.right = None
    node0.left = None
    node0.height = 0
    node0.parent = node1
    node1.left = node0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(4294753518)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 4294753518
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 4294753519
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 4294753518
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test1: OK')


def insert_test2():
    '''
    Self:
        
        None <- node1: 4294731024             
        /                       \             
        None            node1 <- node0: 4294731024
                    /                        \
                    None                          None

    Return:
        None
    End Self:
        
                      None <- node0: 4294731024              
                     /                         \             
        node0 <- node1: 4294731024 node0 <- node2: 4294731024
        /                        \ /                        \
        None                          None                           

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 4294731024)
    node1.data = 4294731024
    node1.left = None
    node1.parent = None
    node1.height = 1
    node0 = Node(node1, 4294731024)
    node0.data = 4294731024
    node0.right = None
    node0.left = None
    node0.height = 0
    node0.parent = node1
    node1.right = node0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    avl0.insert(4294731024)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 4294731024
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 4294731024
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 4294731024
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    print('Test2: OK')


def insert_test3():
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
    print('Test3: OK')


if __name__ == '__main__':
    insert_test1()
    insert_test2()
    insert_test3()
