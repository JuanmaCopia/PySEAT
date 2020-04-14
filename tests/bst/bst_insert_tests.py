from bst import Node, BST


def insert_test1():
    '''
    Self:
        
          2
         / 
         1 
        /  
        0  

    Return:
        None
    End Self:
        
          2
         / 
         1 
        /  
        0  

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(2)
    node0.data = 2
    node0.right = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node1.left = node2
    node0.left = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 1
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == 0
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None
    print('Test1: OK')


def insert_test2():
    '''
    Self:
        
          _1
         /  
        -1  
          \ 
          0 

    Return:
        None
    End Self:
        
          _1
         /  
        -1  
          \ 
          0 

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node1.right = node2
    node0.left = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 0
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None
    print('Test2: OK')


def insert_test3():
    '''
    Self:
        
         1
        / 
        0 

    Return:
        None
    End Self:
        
         1
        / 
        0 

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node0.left = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    print('Test3: OK')


def insert_test4():
    '''
    Self:
        
        -1_ 
           \
           1
          / 
          0 

    Return:
        None
    End Self:
        
        -1_ 
           \
           1
          / 
          0 

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node1.left = node2
    node0.right = node1
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
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 0
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None
    print('Test4: OK')


def insert_test5():
    '''
    Self:
        
        -2_  
           \ 
          -1 
            \
            0

    Return:
        None
    End Self:
        
        -2_  
           \ 
          -1 
            \
            0

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(-2)
    node0.data = -2
    node0.left = None
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node1.right = node2
    node0.right = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == -1
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 0
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None
    print('Test5: OK')


def insert_test6():
    '''
    Self:
        
        -1 
          \
          0

    Return:
        None
    End Self:
        
        -1 
          \
          0

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node0.right = node1
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
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    print('Test6: OK')


def insert_test7():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node0.left = None
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
    print('Test7: OK')


def insert_test8():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    bst0 = BST()
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
    print('Test8: OK')


if __name__ == '__main__':
    insert_test1()
    insert_test2()
    insert_test3()
    insert_test4()
    insert_test5()
    insert_test6()
    insert_test7()
    insert_test8()
