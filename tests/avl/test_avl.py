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
    node16 = Node(None, 0)
    node16.data = 0
    node16.right = None
    node16.left = None
    node16.height = 0
    node16.parent = node1
    node1.right = node16
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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


def test_insert2():
    '''
    Self:
        
          1 
         / \
         1 1
        /   
        1   

    Return:
        None
    End Self:
        
          _1 
         /  \
         1  1
        / \  
        0 1  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 1
    node1.parent = None
    node1.height = 0
    node14 = Node(None, 0)
    node14.data = 1
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.right = node14
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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
    assert avl0.root.data == 1
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 1
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == 1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert3():
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
    node13 = Node(None, 0)
    node13.data = 0
    node13.right = None
    node13.left = None
    node13.height = 0
    node13.parent = node1
    node1.right = node13
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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


def test_insert4():
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
    node15 = Node(None, 0)
    node15.data = 0
    node15.right = None
    node15.left = None
    node15.height = 0
    node15.parent = node1
    node1.right = node15
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert5():
    '''
    Self:
        
          1 
         / \
         1 1
        /   
        0   

    Return:
        None
    End Self:
        
          _1 
         /  \
         0  1
        / \  
        0 1  

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 1
    node1.parent = None
    node1.height = 0
    node13 = Node(None, 0)
    node13.data = 1
    node13.right = None
    node13.left = None
    node13.height = 0
    node13.parent = node1
    node1.right = node13
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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
    assert avl0.root.data == 1
    assert avl0.root.parent is None
    assert avl0.root.height == 2
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.height == 1
    assert avl0.root.left.right.data == 1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0
    assert avl0.root.left.left.data == 0
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert6():
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
    node12 = Node(None, 0)
    node12.data = 0
    node12.right = None
    node12.left = None
    node12.height = 0
    node12.parent = node1
    node1.right = node12
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert7():
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
    node16 = Node(None, 0)
    node16.data = 0
    node16.right = None
    node16.left = None
    node16.height = 0
    node16.parent = node1
    node1.right = node16
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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


def test_insert8():
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
    node15 = Node(None, 0)
    node15.data = 0
    node15.right = None
    node15.left = None
    node15.height = 0
    node15.parent = node1
    node1.right = node15
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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


def test_insert9():
    '''
    Self:
        
         1
        / 
        1 

    Return:
        None
    End Self:
        
         1 
        / \
        0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 1
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 1
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


def test_insert10():
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


def test_insert11():
    '''
    Self:
        
         1
        / 
        1 

    Return:
        None
    End Self:
        
         1 
        / \
        0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 1
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 1
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


def test_insert12():
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
          \  \
          0  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node14 = Node(None, 0)
    node14.data = 0
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.right = node14
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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
    assert avl0.root.left.data == -1
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


def test_insert13():
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
          \  \
          0  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node12 = Node(None, 0)
    node12.data = 0
    node12.right = None
    node12.left = None
    node12.height = 0
    node12.parent = node1
    node1.right = node12
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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
    assert avl0.root.left.data == -1
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


def test_insert14():
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
          \  \
          0  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node11 = Node(None, 0)
    node11.data = 0
    node11.right = None
    node11.left = None
    node11.height = 0
    node11.parent = node1
    node1.right = node11
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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
    assert avl0.root.left.data == -1
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


def test_insert15():
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
           \  \
          -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node14 = Node(None, 0)
    node14.data = 0
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.right = node14
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_insert16():
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
           \  \
          -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node12 = Node(None, 0)
    node12.data = 0
    node12.right = None
    node12.left = None
    node12.height = 0
    node12.parent = node1
    node1.right = node12
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.right.data == -1
    assert avl0.root.left.right.right is None
    assert avl0.root.left.right.left is None
    assert avl0.root.left.right.height == 0


def test_insert17():
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
           \  \
          -1  0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node11 = Node(None, 0)
    node11.data = 0
    node11.right = None
    node11.left = None
    node11.height = 0
    node11.parent = node1
    node1.right = node11
    node2 = Node(None, 0)
    node2.data = -1
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
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
        
            0 
           / \
          -1 0
         /    
        -1    

    Return:
        None
    End Self:
        
            0  
           / \ 
          -1 0 
         /    \
        -1    0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node15 = Node(None, 0)
    node15.data = 0
    node15.right = None
    node15.left = None
    node15.height = 0
    node15.parent = node1
    node1.right = node15
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert19():
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
        
            0  
           / \ 
          -1 0 
         /    \
        -1    0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node14 = Node(None, 0)
    node14.data = 0
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.right = node14
    node2 = Node(None, 0)
    node2.data = -1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0
    assert avl0.root.left.left.data == -1
    assert avl0.root.left.left.right is None
    assert avl0.root.left.left.left is None
    assert avl0.root.left.left.height == 0


def test_insert20():
    '''
    Self:
        
          0
         / 
        -1 

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
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert21():
    '''
    Self:
        
          0 
         / \
        -1 0

    Return:
        None
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0
    assert avl0.root.right.right.data == 0
    assert avl0.root.right.right.right is None
    assert avl0.root.right.right.left is None
    assert avl0.root.right.right.height == 0


def test_insert22():
    '''
    Self:
        
         1
        / 
        0 

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
    node1.data = 1
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
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert23():
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


def test_insert24():
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
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
    assert avl0.root.data == 1
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert25():
    '''
    Self:
        
         0_ 
        /  \
        0  1
          / 
          1 

    Return:
        None
    End Self:
        
         0_  
        /  \ 
        0  1 
          / \
          0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node14 = Node(None, 0)
    node14.data = 0
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.left = node14
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


def test_insert26():
    '''
    Self:
        
         0_ 
        /  \
        0  1
          / 
          1 

    Return:
        None
    End Self:
        
         0_  
        /  \ 
        0  1 
          / \
          0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node12 = Node(None, 0)
    node12.data = 0
    node12.right = None
    node12.left = None
    node12.height = 0
    node12.parent = node1
    node1.left = node12
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


def test_insert27():
    '''
    Self:
        
         0_ 
        /  \
        0  1
          / 
          1 

    Return:
        None
    End Self:
        
         0_  
        /  \ 
        0  1 
          / \
          0 1

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node11 = Node(None, 0)
    node11.data = 0
    node11.right = None
    node11.left = None
    node11.height = 0
    node11.parent = node1
    node1.left = node11
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


def test_insert28():
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
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node14 = Node(None, 0)
    node14.data = 0
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.left = node14
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


def test_insert29():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node12 = Node(None, 0)
    node12.data = -1
    node12.right = None
    node12.left = None
    node12.height = 0
    node12.parent = node1
    node1.left = node12
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
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


def test_insert30():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node11 = Node(None, 0)
    node11.data = -1
    node11.right = None
    node11.left = None
    node11.height = 0
    node11.parent = node1
    node1.left = node11
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
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


def test_insert31():
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
        
          -1_  
         /   \ 
        -1   0 
            / \
            0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node15 = Node(None, 0)
    node15.data = -1
    node15.right = None
    node15.left = None
    node15.height = 0
    node15.parent = node1
    node1.left = node15
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
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
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert32():
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
        
          -1_  
         /   \ 
        -1   0 
            / \
            0 0

    '''
    # Input Creation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = -1
    node1.parent = None
    node1.height = 0
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node14 = Node(None, 0)
    node14.data = -1
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.left = node14
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
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
    assert avl0.root.right.left.data == 0
    assert avl0.root.right.left.right is None
    assert avl0.root.right.left.left is None
    assert avl0.root.right.left.height == 0


def test_insert33():
    '''
    Self:
        
        -1 
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
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert34():
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
    node2 = Node(None, 0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.left = node3
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


def test_insert35():
    '''
    Self:
        
        0 
         \
         1

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
    returnv = avl0.insert(0)
    # Repok check
    assert avl0.repok()
    # Assertions
    assert returnv is None
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


def test_insert36():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node15 = Node(None, 0)
    node15.data = 0
    node15.right = None
    node15.left = None
    node15.height = 0
    node15.parent = node1
    node1.left = node15
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


def test_insert37():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node13 = Node(None, 0)
    node13.data = 0
    node13.right = None
    node13.left = None
    node13.height = 0
    node13.parent = node1
    node1.left = node13
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


def test_insert38():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node12 = Node(None, 0)
    node12.data = 0
    node12.right = None
    node12.left = None
    node12.height = 0
    node12.parent = node1
    node1.left = node12
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


def test_insert39():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node16 = Node(None, 0)
    node16.data = 0
    node16.right = None
    node16.left = None
    node16.height = 0
    node16.parent = node1
    node1.left = node16
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


def test_insert40():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node14 = Node(None, 0)
    node14.data = 0
    node14.right = None
    node14.left = None
    node14.height = 0
    node14.parent = node1
    node1.left = node14
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


def test_insert41():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.left = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.right = node3
    node2.parent = node1
    node1.right = node2
    node13 = Node(None, 0)
    node13.data = 0
    node13.right = None
    node13.left = None
    node13.height = 0
    node13.parent = node1
    node1.left = node13
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


def test_insert42():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node16 = Node(None, 0)
    node16.data = 0
    node16.right = None
    node16.left = None
    node16.height = 0
    node16.parent = node1
    node1.left = node16
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


def test_insert43():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.height = 0
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node2
    node2.left = node3
    node2.parent = node1
    node1.right = node2
    node15 = Node(None, 0)
    node15.data = 0
    node15.right = None
    node15.left = None
    node15.height = 0
    node15.parent = node1
    node1.left = node15
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


def test_insert44():
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


def test_insert45():
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
    node2 = Node(None, 0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.height = 0
    node2.parent = node1
    node1.right = node2
    node3 = Node(None, 0)
    node3.data = 0
    node3.right = None
    node3.left = None
    node3.height = 0
    node3.parent = node1
    node1.left = node3
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


def test_insert46():
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


def test_insert47():
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


def test_insert48():
    '''
    Self:
        
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
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
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
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_insert49():
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


