from avl import *
import pytest


def test_insert1():
    '''
    Self:
        
          0 
         / \
         0 0
        /   
        0   

    Return:
        None
    End Self:
        
           _0 
          /  \
          0  0
         / \  
        -1 0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert2():
    '''
    Self:
        
           0 
          / \
          0 0
         /   
        -1   

    Return:
        None
    End Self:
        
            _0 
           /  \
          -1  0
         /  \  
        -1  0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert3():
    '''
    Self:
        
            0 
           / \
          -1 0
         /    
        -1    

    Return:
        None
    End Self:
        
            __0 
           /   \
          -1_  0
         /   \  
        -1  -1  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert4():
    '''
    Self:
        
          0 
         / \
         0 1
        /   
        0   

    Return:
        None
    End Self:
        
          0_ 
         /  \
         0  1
        /  / 
        0  0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert5():
    '''
    Self:
        
          0 
         / \
         0 0
        /   
        0   

    Return:
        None
    End Self:
        
          0  
         / \ 
         0 0 
        /   \
        0   0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert6():
    '''
    Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    Return:
        None
    End Self:
        
           _0 
          /  \
          0  0
         / \  
        -1 0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert7():
    '''
    Self:
        
          _0 
         /  \
        -1  0
          \  
          0  

    Return:
        None
    End Self:
        
            _0 
           /  \
          -1  0
         /  \  
        -1  0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert8():
    '''
    Self:
        
          __0 
         /   \
        -1_  0
           \  
          -1  

    Return:
        None
    End Self:
        
            __0 
           /   \
          -1_  0
         /   \  
        -1  -1  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert9():
    '''
    Self:
        
         _0 
        /  \
        0  1
         \  
         0  

    Return:
        None
    End Self:
        
         _0_ 
        /   \
        0   1
         \ / 
         0 0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_insert10():
    '''
    Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    Return:
        None
    End Self:
        
         _0  
        /  \ 
        0  0 
         \  \
         0  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_insert11():
    '''
    Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    Return:
        None
    End Self:
        
           0_ 
          /  \
          0  0
         /  / 
        -1  0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 1
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert12():
    '''
    Self:
        
          0_ 
         /  \
        -1  0
           / 
           0 

    Return:
        None
    End Self:
        
          __0_ 
         /    \
        -1_   0
           \ / 
          -1 0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 1
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_insert13():
    '''
    Self:
        
          -1_ 
         /   \
        -1   0
            / 
            0 

    Return:
        None
    End Self:
        
          -1__  
         /    \ 
        -1    0 
             / \
            -1 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == -1
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.right.left.data == -1
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert14():
    '''
    Self:
        
          -1__ 
         /    \
        -1    0
             / 
            -1 

    Return:
        None
    End Self:
        
          -1___  
         /     \ 
        -1    -1 
             /  \
            -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = -1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == -1
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == -1
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.right.left.data == -1
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert15():
    '''
    Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    Return:
        None
    End Self:
        
         0_  
        /  \ 
        0  0 
          / \
          0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert16():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           0

    Return:
        None
    End Self:
        
           0  
          / \ 
          0 0 
         /   \
        -1   0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 1
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert17():
    '''
    Self:
        
          0  
         / \ 
        -1 0 
            \
            0

    Return:
        None
    End Self:
        
          __0  
         /   \ 
        -1_  0 
           \  \
          -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 1
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_insert18():
    '''
    Self:
        
          -1  
         /  \ 
        -1  0 
             \
             0

    Return:
        None
    End Self:
        
          -1__  
         /    \ 
        -1    0 
             / \
            -1 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == -1
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.right.left.data == -1
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert19():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           1

    Return:
        None
    End Self:
        
         0_  
        /  \ 
        0  0 
          / \
          0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 1
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert20():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           0

    Return:
        None
    End Self:
        
         0_  
        /  \ 
        0  0 
          / \
          0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert21():
    '''
    Self:
        
         0 
        / \
        0 0

    Return:
        None
    End Self:
        
           0 
          / \
          0 0
         /   
        -1   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 1
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert22():
    '''
    Self:
        
          0 
         / \
        -1 0

    Return:
        None
    End Self:
        
          __0 
         /   \
        -1_  0
           \  
          -1  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
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


def test_insert23():
    '''
    Self:
        
         0 
        / \
        0 1

    Return:
        None
    End Self:
        
         0_ 
        /  \
        0  1
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert24():
    '''
    Self:
        
         0 
        / \
        0 0

    Return:
        None
    End Self:
        
         0  
        / \ 
        0 0 
           \
           0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
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


def test_insert25():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
          0 
         / \
        -1 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
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
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert26():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        None
    End Self:
        
          -1 
         /  \
        -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == -1
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert27():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
         0 
        / \
        0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
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


def test_insert28():
    '''
    Self:
        
        0 
         \
         0

    Return:
        None
    End Self:
        
          0 
         / \
        -1 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert29():
    '''
    Self:
        
        -1 
          \
          0

    Return:
        None
    End Self:
        
          -1 
         /  \
        -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == -1
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert30():
    '''
    Self:
        
        0 
         \
         0

    Return:
        None
    End Self:
        
         0 
        / \
        0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
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


def test_insert31():
    '''
    Self:
        
        4294889199

    Return:
        None
    End Self:
        
              ____4294889199
             /              
        4294889198          

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 4294889199
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(4294889198)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 4294889199
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.left.data == 4294889198
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert32():
    '''
    Self:
        
        4294967294

    Return:
        None
    End Self:
        
        4294967294_____     
                       \    
                  4294967294

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 4294967294
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(4294967294)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 4294967294
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 4294967294
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_insert33():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_find_min1():
    '''
    Self:
        
          0 
         / \
         0 0
        /   
        0   

    Return:
        node: 0
    End Self:
        
          0 
         / \
         0 0
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.right is None
    assert returnv.parent.height == 0
    assert returnv.parent.parent.data == 0
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.height == 0
    assert returnv.parent.parent.right.data == 0
    assert returnv.parent.parent.right.right is None
    assert returnv.parent.parent.right.left is None
    assert returnv.parent.parent.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_find_min2():
    '''
    Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    Return:
        node: 0
    End Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.right.data == 0
    assert returnv.parent.right.right is None
    assert returnv.parent.right.left is None
    assert returnv.parent.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_find_min3():
    '''
    Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    Return:
        node: 0
    End Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.right.data == 0
    assert returnv.parent.right.right is None
    assert returnv.parent.right.height == 0
    assert returnv.parent.right.left.data == 0
    assert returnv.parent.right.left.right is None
    assert returnv.parent.right.left.left is None
    assert returnv.parent.right.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_find_min4():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           0

    Return:
        node: 0
    End Self:
        
         0  
        / \ 
        0 0 
           \
           0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.right.data == 0
    assert returnv.parent.right.left is None
    assert returnv.parent.right.height == 0
    assert returnv.parent.right.right.data == 0
    assert returnv.parent.right.right.right is None
    assert returnv.parent.right.right.left is None
    assert returnv.parent.right.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_find_min5():
    '''
    Self:
        
         0 
        / \
        0 0

    Return:
        node: 0
    End Self:
        
         0 
        / \
        0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.right.data == 0
    assert returnv.parent.right.right is None
    assert returnv.parent.right.left is None
    assert returnv.parent.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_find_min6():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        node: 0
    End Self:
        
         0
        / 
        0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
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
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.right is None
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_find_min7():
    '''
    Self:
        
        0 
         \
         0

    Return:
        node: 0
    End Self:
        
        0 
         \
         0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.left is None
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_find_min8():
    '''
    Self:
        
        4294967295

    Return:
        node: 4294967295
    End Self:
        
        4294967295

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 4294967295
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 4294967295
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.parent is None
    assert returnv.height == 0
    assert avl0.root.data == 4294967295
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_find_min9():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Input Creation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.find_min()
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root is None


def test_next_larger1():
    '''
    Self:
        
          0 
         / \
         0 0
        /   
        0   

    Return:
        node: 0
    End Self:
        
          0 
         / \
         0 0
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.left.data == 0
    assert returnv.parent.left.right is None
    assert returnv.parent.left.height == 0
    assert returnv.parent.left.left.data == 0
    assert returnv.parent.left.left.right is None
    assert returnv.parent.left.left.left is None
    assert returnv.parent.left.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger2():
    '''
    Self:
        
            0 
           / \
          -1 0
         /    
        -1    

    Return:
        node: 0
    End Self:
        
            0 
           / \
          -1 0
         /    
        -1    

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.height == 0
    assert returnv.left.left.data == -1
    assert returnv.left.left.right is None
    assert returnv.left.left.left is None
    assert returnv.left.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger3():
    '''
    Self:
        
          1 
         / \
         1 1
        /   
        0   

    Return:
        node: 1
    End Self:
        
          1 
         / \
         1 1
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 1
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 1
    assert returnv.right is None
    assert returnv.height == 0
    assert returnv.left.data == 0
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert returnv.parent.data == 1
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.right.data == 1
    assert returnv.parent.right.right is None
    assert returnv.parent.right.left is None
    assert returnv.parent.right.height == 0
    assert avl0.root.data == 1
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 1
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger4():
    '''
    Self:
        
          0 
         / \
         0 0
        /   
        0   

    Return:
        None
    End Self:
        
          0 
         / \
         0 0
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger5():
    '''
    Self:
        
           0 
          / \
          0 0
         /   
        -2   

    Return:
        None
    End Self:
        
           0 
          / \
          0 0
         /   
        -2   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -2
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == -2
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger6():
    '''
    Self:
        
            0 
           / \
          -2 0
         /    
        -2    

    Return:
        None
    End Self:
        
            0 
           / \
          -2 0
         /    
        -2    

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -2
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == -2
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger7():
    '''
    Self:
        
          0 
         / \
         0 1
        /   
        0   

    Return:
        None
    End Self:
        
          0 
         / \
         0 1
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger8():
    '''
    Self:
        
          0 
         / \
         0 2
        /   
        0   

    Return:
        None
    End Self:
        
          0 
         / \
         0 2
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger9():
    '''
    Self:
        
          0 
         / \
         0 0
        /   
        0   

    Return:
        None
    End Self:
        
          0 
         / \
         0 0
        /   
        0   

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.left = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_next_larger10():
    '''
    Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    Return:
        node: 0
    End Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.left.data == 0
    assert returnv.parent.left.left is None
    assert returnv.parent.left.height == 0
    assert returnv.parent.left.right.data == 0
    assert returnv.parent.left.right.right is None
    assert returnv.parent.left.right.left is None
    assert returnv.parent.left.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger11():
    '''
    Self:
        
          _0 
         /  \
        -1  0
          \  
          0  

    Return:
        node: 0
    End Self:
        
          _0 
         /  \
        -1  0
          \  
          0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == -1
    assert returnv.parent.left is None
    assert returnv.parent.height == 0
    assert returnv.parent.parent.data == 0
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.height == 0
    assert returnv.parent.parent.right.data == 0
    assert returnv.parent.parent.right.right is None
    assert returnv.parent.parent.right.left is None
    assert returnv.parent.parent.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger12():
    '''
    Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    Return:
        None
    End Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger13():
    '''
    Self:
        
          __0 
         /   \
        -2_  0
           \  
          -1  

    Return:
        node: 0
    End Self:
        
          __0 
         /   \
        -2_  0
           \  
          -1  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert returnv.left.data == -2
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert returnv.left.right.data == -1
    assert returnv.left.right.right is None
    assert returnv.left.right.left is None
    assert returnv.left.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger14():
    '''
    Self:
        
          _0 
         /  \
        -2  0
          \  
          0  

    Return:
        None
    End Self:
        
          _0 
         /  \
        -2  0
          \  
          0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger15():
    '''
    Self:
        
          __0 
         /   \
        -2_  0
           \  
          -2  

    Return:
        None
    End Self:
        
          __0 
         /   \
        -2_  0
           \  
          -2  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = -2
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == -2
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger16():
    '''
    Self:
        
         _0 
        /  \
        0  1
         \  
         0  

    Return:
        None
    End Self:
        
         _0 
        /  \
        0  1
         \  
         0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger17():
    '''
    Self:
        
         _0 
        /  \
        0  2
         \  
         0  

    Return:
        None
    End Self:
        
         _0 
        /  \
        0  2
         \  
         0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger18():
    '''
    Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    Return:
        None
    End Self:
        
         _0 
        /  \
        0  0
         \  
         0  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node2
    node2.right = node4
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.left.right.data == 0
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_next_larger19():
    '''
    Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    Return:
        node: 0
    End Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.right is None
    assert returnv.parent.height == 0
    assert returnv.parent.parent.data == 0
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.height == 0
    assert returnv.parent.parent.left.data == 0
    assert returnv.parent.parent.left.right is None
    assert returnv.parent.parent.left.left is None
    assert returnv.parent.parent.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger20():
    '''
    Self:
        
          0_ 
         /  \
        -1  0
           / 
           0 

    Return:
        node: 0
    End Self:
        
          0_ 
         /  \
        -1  0
           / 
           0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.height == 0
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert returnv.right.left.data == 0
    assert returnv.right.left.right is None
    assert returnv.right.left.left is None
    assert returnv.right.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger21():
    '''
    Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    Return:
        None
    End Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger22():
    '''
    Self:
        
          0_ 
         /  \
        -2  0
           / 
           0 

    Return:
        None
    End Self:
        
          0_ 
         /  \
        -2  0
           / 
           0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger23():
    '''
    Self:
        
         0_ 
        /  \
        0  1
          / 
          0 

    Return:
        None
    End Self:
        
         0_ 
        /  \
        0  1
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger24():
    '''
    Self:
        
         0_ 
        /  \
        0  2
          / 
          1 

    Return:
        node: 2
    End Self:
        
         0_ 
        /  \
        0  2
          / 
          1 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 2
    assert returnv.right is None
    assert returnv.height == 0
    assert returnv.left.data == 1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.left.data == 0
    assert returnv.parent.left.right is None
    assert returnv.parent.left.left is None
    assert returnv.parent.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 1
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger25():
    '''
    Self:
        
         0_ 
        /  \
        0  2
          / 
          2 

    Return:
        None
    End Self:
        
         0_ 
        /  \
        0  2
          / 
          2 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 2
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 2
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger26():
    '''
    Self:
        
         0_ 
        /  \
        0  2
          / 
          0 

    Return:
        None
    End Self:
        
         0_ 
        /  \
        0  2
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger27():
    '''
    Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    Return:
        None
    End Self:
        
         0_ 
        /  \
        0  0
          / 
          0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.left = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_next_larger28():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           0

    Return:
        node: 0
    End Self:
        
         0  
        / \ 
        0 0 
           \
           0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.left.data == 0
    assert returnv.parent.left.right is None
    assert returnv.parent.left.left is None
    assert returnv.parent.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger29():
    '''
    Self:
        
          0  
         / \ 
        -1 0 
            \
            0

    Return:
        node: 0
    End Self:
        
          0  
         / \ 
        -1 0 
            \
            0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert returnv.right.right.data == 0
    assert returnv.right.right.right is None
    assert returnv.right.right.left is None
    assert returnv.right.right.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger30():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           0

    Return:
        None
    End Self:
        
         0  
        / \ 
        0 0 
           \
           0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger31():
    '''
    Self:
        
          0  
         / \ 
        -2 0 
            \
            0

    Return:
        None
    End Self:
        
          0  
         / \ 
        -2 0 
            \
            0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger32():
    '''
    Self:
        
          -1  
         /  \ 
        -1  0 
             \
             0

    Return:
        node: 0
    End Self:
        
          -1  
         /  \ 
        -1  0 
             \
             0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.left is None
    assert returnv.parent.height == 0
    assert returnv.parent.parent.data == -1
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.height == 0
    assert returnv.parent.parent.left.data == -1
    assert returnv.parent.parent.left.right is None
    assert returnv.parent.parent.left.left is None
    assert returnv.parent.parent.left.height == 0
    assert avl0.root.data == -1
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger33():
    '''
    Self:
        
         0  
        / \ 
        0 2 
           \
           2

    Return:
        None
    End Self:
        
         0  
        / \ 
        0 2 
           \
           2

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 2
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 2
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger34():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           1

    Return:
        None
    End Self:
        
         0  
        / \ 
        0 0 
           \
           1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 1
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 1
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger35():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           2

    Return:
        None
    End Self:
        
         0  
        / \ 
        0 0 
           \
           2

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 2
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 2
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger36():
    '''
    Self:
        
         0  
        / \ 
        0 0 
           \
           0

    Return:
        None
    End Self:
        
         0  
        / \ 
        0 0 
           \
           0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.left = None
    node3.height = 0
    node4 = Node(None, 0)
    node4.data = 0
    node4.right = None
    node4.left = None
    node4.height = 0
    node4.parent = node3
    node3.right = node4
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_next_larger37():
    '''
    Self:
        
         0 
        / \
        0 0

    Return:
        node: 0
    End Self:
        
         0 
        / \
        0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert returnv.parent.left.data == 0
    assert returnv.parent.left.right is None
    assert returnv.parent.left.left is None
    assert returnv.parent.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger38():
    '''
    Self:
        
          0 
         / \
        -1 0

    Return:
        node: 0
    End Self:
        
          0 
         / \
        -1 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.right.height == 0
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger39():
    '''
    Self:
        
         0 
        / \
        0 0

    Return:
        None
    End Self:
        
         0 
        / \
        0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger40():
    '''
    Self:
        
          0 
         / \
        -2 0

    Return:
        None
    End Self:
        
          0 
         / \
        -2 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger41():
    '''
    Self:
        
         0 
        / \
        0 1

    Return:
        None
    End Self:
        
         0 
        / \
        0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger42():
    '''
    Self:
        
         0 
        / \
        0 2

    Return:
        None
    End Self:
        
         0 
        / \
        0 2

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger43():
    '''
    Self:
        
         0 
        / \
        0 0

    Return:
        None
    End Self:
        
         0 
        / \
        0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.right = node3
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger44():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
         0
        / 
        0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger45():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        node: 0
    End Self:
        
          0
         / 
        -1 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger46():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
         0
        / 
        0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger47():
    '''
    Self:
        
          0
         / 
        -2 

    Return:
        None
    End Self:
        
          0
         / 
        -2 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.left = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger48():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
         0
        / 
        0 

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
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
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger49():
    '''
    Self:
        
        0 
         \
         0

    Return:
        node: 0
    End Self:
        
        0 
         \
         0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.left is None
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger50():
    '''
    Self:
        
        0 
         \
         0

    Return:
        None
    End Self:
        
        0 
         \
         0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger51():
    '''
    Self:
        
        0 
         \
         1

    Return:
        None
    End Self:
        
        0 
         \
         1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger52():
    '''
    Self:
        
        0 
         \
         2

    Return:
        None
    End Self:
        
        0 
         \
         2

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 2
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger53():
    '''
    Self:
        
        0 
         \
         0

    Return:
        None
    End Self:
        
        0 
         \
         0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger54():
    '''
    Self:
        
        4294967294

    Return:
        None
    End Self:
        
        4294967294

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 4294967294
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(4294967294)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 4294967294
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_next_larger55():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(-1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_next_larger56():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(1)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_next_larger57():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Input Creation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root is None


