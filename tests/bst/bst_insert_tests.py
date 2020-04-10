from bst import Node, BST


def insert_test1():
    '''
    Self:
        
                 None <- node0: 0
                 /              \
        node0 <- node1: -1       None
        /                \       
        None                  None       

    Return:
        None
    End Self:
        
                 None <- node0: 0
                 /              \
        node0 <- node1: -1       None
        /                \       
        None                  None       

    '''
    # Self Generation
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node0.parent = None
    node1 = Node(-1)
    node1.data = -1
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(-1)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.parent is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    print('Test1: OK')


def insert_test2():
    '''
    Self:
        
        None <- node0: -1         
        /               \         
        None         node0 <- node1: 0
                 /               \
                 None                 None

    Return:
        None
    End Self:
        
        None <- node0: -1         
        /               \         
        None         node0 <- node1: 0
                 /               \
                 None                 None

    '''
    # Self Generation
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node0.parent = None
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.parent is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    print('Test2: OK')


def insert_test3():
    '''
    Self:
        
        None <- node0: 0
        /              \
        None                None

    Return:
        None
    End Self:
        
        None <- node0: 0
        /              \
        None                None

    '''
    # Self Generation
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node0.left = None
    node0.parent = None
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left is None
    assert bst0.root.parent is None
    print('Test3: OK')


def insert_test4():
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
    bst0 = BST(None)
    bst0.root = None
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left is None
    assert bst0.root.parent is None
    print('Test4: OK')


if __name__ == '__main__':
    insert_test1()
    insert_test2()
    insert_test3()
    insert_test4()
