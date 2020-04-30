from bst import *


def test_insert1():
    '''
    Self:
        
          3
         / 
         2 
        /  
        1  

    Return:
        None
    End Self:
        
           3
          / 
          2 
         /  
         1  
        /   
        0   

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(3)
    node1.data = 3
    node1.right = None
    node2 = Node(2)
    node2.data = 2
    node2.right = None
    node3 = Node(1)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 3
    assert bst0.root.right is None
    assert bst0.root.left.data == 2
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == 1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left.data == 0
    assert bst0.root.left.left.left.right is None
    assert bst0.root.left.left.left.left is None


def test_insert2():
    '''
    Self:
        
           2
          / 
          1 
         /  
        -1  

    Return:
        None
    End Self:
        
           2
          / 
          1 
         /  
        -1  

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(2)
    node1.data = 2
    node1.right = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node3 = Node(-1)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(1)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 1
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_insert3():
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
    node1 = Node(2)
    node1.data = 2
    node1.right = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node3 = Node(0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
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


def test_insert4():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        None
    End Self:
        
          0
         / 
        -1 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(-1)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_insert5():
    '''
    Self:
        
          __0
         /   
        -3_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0
         /   
        -3_  
           \ 
          -1 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(-3)
    node2.data = -3
    node2.left = None
    node3 = Node(-1)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -3
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_insert6():
    '''
    Self:
        
          __1
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          ___1
         /    
        -2_   
           \  
          -1  
            \ 
            0 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(-2)
    node2.data = -2
    node2.left = None
    node3 = Node(-1)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.left is None
    assert bst0.root.left.right.right.data == 0
    assert bst0.root.left.right.right.right is None
    assert bst0.root.left.right.right.left is None


def test_insert7():
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
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(-1)
    node2.data = -1
    node2.left = None
    node3 = Node(0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
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


def test_insert8():
    '''
    Self:
        
          1
         / 
        -1 

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
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(-1)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
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


def test_insert9():
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
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
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


def test_insert10():
    '''
    Self:
        
        1

    Return:
        None
    End Self:
        
         1
        / 
        0 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node1.left = None
    bst0.root = node1
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


def test_insert11():
    '''
    Self:
        
        0_ 
          \
          3
         / 
         2 

    Return:
        None
    End Self:
        
        0_ 
          \
          3
         / 
         2 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(3)
    node2.data = 3
    node2.right = None
    node3 = Node(2)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 3
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 2
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_insert12():
    '''
    Self:
        
        -2__ 
            \
            1
           / 
          -1 

    Return:
        None
    End Self:
        
        -2___ 
             \
            _1
           /  
          -1  
            \ 
            0 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node3 = Node(-1)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.left is None
    assert bst0.root.right.left.right.data == 0
    assert bst0.root.right.left.right.right is None
    assert bst0.root.right.left.right.left is None


def test_insert13():
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
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node3 = Node(0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
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


def test_insert14():
    '''
    Self:
        
        0 
         \
         2

    Return:
        None
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(2)
    node2.data = 2
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(1)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_insert15():
    '''
    Self:
        
        -2_  
           \ 
          -1 
            \
            1

    Return:
        None
    End Self:
        
        -2_   
           \  
          -1_ 
             \
             1
            / 
            0 

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(-1)
    node2.data = -1
    node2.left = None
    node3 = Node(1)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
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
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left.data == 0
    assert bst0.root.right.right.left.right is None
    assert bst0.root.right.right.left.left is None


def test_insert16():
    '''
    Self:
        
        -3_   
           \  
          -2_ 
             \
            -1

    Return:
        None
    End Self:
        
        -3_    
           \   
          -2_  
             \ 
            -1 
              \
              0

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(-3)
    node1.data = -3
    node1.left = None
    node2 = Node(-2)
    node2.data = -2
    node2.left = None
    node3 = Node(-1)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -3
    assert bst0.root.left is None
    assert bst0.root.right.data == -2
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == -1
    assert bst0.root.right.right.left is None
    assert bst0.root.right.right.right.data == 0
    assert bst0.root.right.right.right.right is None
    assert bst0.root.right.right.right.left is None


def test_insert17():
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
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(-1)
    node2.data = -1
    node2.left = None
    node3 = Node(0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
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


def test_insert18():
    '''
    Self:
        
        -2_ 
           \
          -1

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
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(-1)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
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


def test_insert19():
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
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
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


def test_insert20():
    '''
    Self:
        
        -1

    Return:
        None
    End Self:
        
        -1 
          \
          0

    '''
    # Self Generation
    bst0 = BST()
    node1 = Node(-1)
    node1.data = -1
    node1.right = None
    node1.left = None
    bst0.root = node1
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


def test_insert21():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    bst0.root = node1
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


def test_insert22():
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


