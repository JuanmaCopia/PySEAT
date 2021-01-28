from bst import *
import pytest


def test_insert1():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
            0 
           / \
          -1 1
         /    
        -2    

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.left_child is None
    assert bst0.root.left_child.left_child.right_child is None


def test_insert2():
    '''
    Self:
        
          0 
         / \
        -2 1

    Return:
        None
    End Self:
        
          __0 
         /   \
        -2_  1
           \  
          -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -2
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.left_child is None
    assert bst0.root.left_child.right_child.right_child is None


def test_insert3():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_insert4():
    '''
    Self:
        
          0 
         / \
        -1 2

    Return:
        None
    End Self:
        
          0_ 
         /  \
        -1  2
           / 
           1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.left_child is None
    assert bst0.root.right_child.left_child.right_child is None


def test_insert5():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0  
         / \ 
        -1 1 
            \
            2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None
    assert bst0.root.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.left_child is None
    assert bst0.root.right_child.right_child.right_child is None


def test_insert6():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_insert7():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_insert8():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
             1
            / 
            0 
           /  
          -1  
         /    
        -2    

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.left_child.left_child is None
    assert bst0.root.left_child.left_child.left_child.right_child is None


def test_insert9():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -2  

    Return:
        None
    End Self:
        
             1
            / 
          __0 
         /    
        -2_   
           \  
          -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.left_child is None
    assert bst0.root.left_child.left_child.right_child.value == -1
    assert bst0.root.left_child.left_child.right_child.left_child is None
    assert bst0.root.left_child.left_child.right_child.right_child is None


def test_insert10():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_insert11():
    '''
    Self:
        
           2
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           _2
          /  
          0  
         / \ 
        -1 1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.left_child is None
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_insert12():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_insert13():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           1 
          / \
          0 2
         /   
        -1   

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_insert14():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_insert15():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        None
    End Self:
        
           _2
          /  
          0  
         / \ 
        -1 1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.left_child is None
    assert bst0.root.left_child.left_child.right_child is None


def test_insert16():
    '''
    Self:
        
         _3
        /  
        0  
         \ 
         2 

    Return:
        None
    End Self:
        
         __3
        /   
        0_  
          \ 
          2 
         /  
         1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 3
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 3
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == 2
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child.value == 1
    assert bst0.root.left_child.right_child.left_child.left_child is None
    assert bst0.root.left_child.right_child.left_child.right_child is None


def test_insert17():
    '''
    Self:
        
         _3
        /  
        0  
         \ 
         1 

    Return:
        None
    End Self:
        
         __3
        /   
        0   
         \  
         1  
          \ 
          2 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 3
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 3
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.left_child is None
    assert bst0.root.left_child.right_child.right_child.value == 2
    assert bst0.root.left_child.right_child.right_child.left_child is None
    assert bst0.root.left_child.right_child.right_child.right_child is None


def test_insert18():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        None
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_insert19():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        None
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_insert20():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0 
         /   \
        -2_  1
           \  
          -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_insert21():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_insert22():
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
         /   
        -2   

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.left_child is None
    assert bst0.root.left_child.left_child.right_child is None


def test_insert23():
    '''
    Self:
        
          0
         / 
        -2 

    Return:
        None
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.left_child is None
    assert bst0.root.left_child.right_child.right_child is None


def test_insert24():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_insert25():
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
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_insert26():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_insert27():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
          0_ 
         /  \
        -1  2
           / 
           1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_insert28():
    '''
    Self:
        
        -3__ 
            \
            0
           / 
          -1 

    Return:
        None
    End Self:
        
        -3____ 
              \
              0
             / 
            -1 
           /   
          -2   

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -3
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -3
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child.value == -2
    assert bst0.root.right_child.left_child.left_child.left_child is None
    assert bst0.root.right_child.left_child.left_child.right_child is None


def test_insert29():
    '''
    Self:
        
        -3__ 
            \
            0
           / 
          -2 

    Return:
        None
    End Self:
        
        -3____ 
              \
            __0
           /   
          -2_  
             \ 
            -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -3
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -3
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -2
    assert bst0.root.right_child.left_child.left_child is None
    assert bst0.root.right_child.left_child.right_child.value == -1
    assert bst0.root.right_child.left_child.right_child.left_child is None
    assert bst0.root.right_child.left_child.right_child.right_child is None


def test_insert30():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        None
    End Self:
        
        -2__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_insert31():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        None
    End Self:
        
        -2__  
            \ 
            0 
           / \
          -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.left_child is None
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_insert32():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        None
    End Self:
        
        -2__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_insert33():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_insert34():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
          -1  
         /  \ 
        -2  0 
             \
             1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_insert35():
    '''
    Self:
        
        -2  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -2__  
            \ 
            0 
           / \
          -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.left_child is None
    assert bst0.root.right_child.left_child.right_child is None


def test_insert36():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           2

    Return:
        None
    End Self:
        
        -1   
          \  
          0_ 
            \
            2
           / 
           1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child.value == 1
    assert bst0.root.right_child.right_child.left_child.left_child is None
    assert bst0.root.right_child.right_child.left_child.right_child is None


def test_insert37():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1   
          \  
          0  
           \ 
           1 
            \
            2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.left_child is None
    assert bst0.root.right_child.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.right_child.left_child is None
    assert bst0.root.right_child.right_child.right_child.right_child is None


def test_insert38():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_insert39():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_insert40():
    '''
    Self:
        
        0  
         \ 
         1 
          \
          2

    Return:
        None
    End Self:
        
        0  
         \ 
         1 
          \
          2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.left_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_insert41():
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
        -2  0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child is None


def test_insert42():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.left_child is None
    assert bst0.root.right_child.left_child.right_child is None


def test_insert43():
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
          \
          2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.left_child is None
    assert bst0.root.right_child.right_child.right_child is None


def test_insert44():
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
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_insert45():
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
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_insert46():
    '''
    Self:
        
        -3527946359080215006

    Return:
        None
    End Self:
        
                   _________-3527946359080215006
                  /                             
        -3527946359080215007                    

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -3527946359080215006
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-3527946359080215007)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -3527946359080215006
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -3527946359080215007
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child is None


def test_insert47():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child is None


def test_insert48():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


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
    bst0 = BST()
    bst0.root = None
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.right_child is None
    assert bst0.root.parent is None


def test_find1():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        node: 0
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.parent is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.parent is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find2():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        node: -1
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find3():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find4():
    '''
    Self:
        
          0 
         / \
        -2 1

    Return:
        None
    End Self:
        
          0 
         / \
        -2 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -2
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find5():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        node: 1
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find6():
    '''
    Self:
        
          0 
         / \
        -1 2

    Return:
        None
    End Self:
        
          0 
         / \
        -1 2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find7():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find8():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        node: 1
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.right_child is None
    assert returnv.parent is None
    assert returnv.left_child.value == 0
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child.value == -1
    assert returnv.left_child.left_child.right_child is None
    assert returnv.left_child.left_child.left_child is None
    assert returnv.left_child.parent.value == 1
    assert returnv.left_child.parent.right_child is None
    assert returnv.left_child.parent.parent is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find9():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        node: 0
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.right_child is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.parent.value == 1
    assert returnv.parent.right_child is None
    assert returnv.parent.parent is None
    assert returnv.left_child.parent.value == 0
    assert returnv.left_child.parent.right_child is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find10():
    '''
    Self:
        
            0
           / 
          -1 
         /   
        -2   

    Return:
        node: -2
    End Self:
        
            0
           / 
          -1 
         /   
        -2   

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -2
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == -1
    assert returnv.parent.right_child is None
    assert returnv.parent.left_child.value == -2
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.right_child is None
    assert returnv.parent.parent.parent is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find11():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find12():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -2  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -2  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find13():
    '''
    Self:
        
           2
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           2
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find14():
    '''
    Self:
        
            0
           / 
          -1 
         /   
        -2   

    Return:
        None
    End Self:
        
            0
           / 
          -1 
         /   
        -2   

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_find15():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        node: 2
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 2
    assert returnv.right_child is None
    assert returnv.parent is None
    assert returnv.left_child.value == 0
    assert returnv.left_child.left_child is None
    assert returnv.left_child.right_child.value == 1
    assert returnv.left_child.right_child.right_child is None
    assert returnv.left_child.right_child.left_child is None
    assert returnv.left_child.parent.value == 2
    assert returnv.left_child.parent.right_child is None
    assert returnv.left_child.parent.parent is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find16():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        node: -2
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -2
    assert returnv.left_child is None
    assert returnv.right_child.value == -1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.right_child is None
    assert returnv.parent.parent is None
    assert returnv.right_child.parent.value == -2
    assert returnv.right_child.parent.left_child is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find17():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-3)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find18():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        node: -1
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == -2
    assert returnv.parent.left_child is None
    assert returnv.parent.right_child.value == -1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.right_child is None
    assert returnv.parent.parent.parent is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find19():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -3
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -3
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find20():
    '''
    Self:
        
          __0
         /   
        -3_  
           \ 
          -2 

    Return:
        None
    End Self:
        
          __0
         /   
        -3_  
           \ 
          -2 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -3
    node1.left_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -3
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -2
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find21():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_find22():
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
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.right_child is None
    assert returnv.parent is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.left_child.parent.value == 0
    assert returnv.left_child.parent.right_child is None
    assert returnv.left_child.parent.parent is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find23():
    '''
    Self:
        
         1
        / 
        0 

    Return:
        node: 0
    End Self:
        
         1
        / 
        0 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 1
    assert returnv.parent.right_child is None
    assert returnv.parent.parent is None
    assert returnv.parent.left_child.value == 0
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find24():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find25():
    '''
    Self:
        
         2
        / 
        0 

    Return:
        None
    End Self:
        
         2
        / 
        0 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find26():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_find27():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        node: -2
    End Self:
        
        -2__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -2
    assert returnv.left_child is None
    assert returnv.parent is None
    assert returnv.right_child.value == 0
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child.value == -1
    assert returnv.right_child.left_child.right_child is None
    assert returnv.right_child.left_child.left_child is None
    assert returnv.right_child.parent.value == -2
    assert returnv.right_child.parent.left_child is None
    assert returnv.right_child.parent.parent is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find28():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find29():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        node: 2
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 2
    assert returnv.right_child is None
    assert returnv.left_child.value == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.left_child is None
    assert returnv.parent.parent is None
    assert returnv.left_child.parent.value == 2
    assert returnv.left_child.parent.right_child is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find30():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        node: 1
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 2
    assert returnv.parent.right_child is None
    assert returnv.parent.left_child.value == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.left_child is None
    assert returnv.parent.parent.parent is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find31():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 3
    node1.right_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 3
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 2
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find32():
    '''
    Self:
        
        0_ 
          \
          3
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          3
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 3
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 3
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find33():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(3)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_find34():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        node: -1
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.left_child is None
    assert returnv.parent is None
    assert returnv.right_child.value == 0
    assert returnv.right_child.left_child is None
    assert returnv.right_child.right_child.value == 1
    assert returnv.right_child.right_child.right_child is None
    assert returnv.right_child.right_child.left_child is None
    assert returnv.right_child.parent.value == -1
    assert returnv.right_child.parent.left_child is None
    assert returnv.right_child.parent.parent is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find35():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find36():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        node: 0
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.left_child is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.parent.value == -1
    assert returnv.parent.left_child is None
    assert returnv.parent.parent is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.left_child is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find37():
    '''
    Self:
        
        -2  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -2  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find38():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        node: 1
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.left_child is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.parent.value == -1
    assert returnv.parent.parent.left_child is None
    assert returnv.parent.parent.parent is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find39():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           2

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find40():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_find41():
    '''
    Self:
        
        0 
         \
         1

    Return:
        node: 0
    End Self:
        
        0 
         \
         1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.left_child is None
    assert returnv.parent is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.left_child is None
    assert returnv.right_child.parent.parent is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_find42():
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
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_find43():
    '''
    Self:
        
        -1 
          \
          0

    Return:
        node: 0
    End Self:
        
        -1 
          \
          0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == -1
    assert returnv.parent.left_child is None
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 0
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_find44():
    '''
    Self:
        
        -2 
          \
          0

    Return:
        None
    End Self:
        
        -2 
          \
          0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_find45():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_find46():
    '''
    Self:
        
        -9187343239835287550

    Return:
        node: -9187343239835287550
    End Self:
        
        -9187343239835287550

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -9187343239835287550
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-9187343239835287550)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -9187343239835287550
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent is None
    assert bst0.root.value == -9187343239835287550
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_find47():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_find48():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_find49():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Input Creation
    bst0 = BST()
    bst0.root = None
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root is None


def test_height1():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        2
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 2
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_height2():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        3
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_height3():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        3
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == 1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_height4():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        2
    End Self:
        
          0
         / 
        -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 2
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_height5():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        3
    End Self:
        
        -2__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == -1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_height6():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        3
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_height7():
    '''
    Self:
        
        0 
         \
         1

    Return:
        2
    End Self:
        
        0 
         \
         1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 2
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_height8():
    '''
    Self:
        
        -5255629292185747262

    Return:
        1
    End Self:
        
        -5255629292185747262

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -5255629292185747262
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 1
    assert bst0.root.value == -5255629292185747262
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_height9():
    '''
    Self:
        <empty tree>
    Return:
        0
    End Self:
        <empty tree>
    '''
    # Input Creation
    bst0 = BST()
    bst0.root = None
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 0
    assert bst0.root is None


def test_delete_value1():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          1
         / 
        -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value2():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
        0 
         \
         1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value3():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value4():
    '''
    Self:
        
          0 
         / \
        -2 1

    Return:
        None
    End Self:
        
          0 
         / \
        -2 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -2
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value5():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0
         / 
        -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value6():
    '''
    Self:
        
          0 
         / \
        -1 2

    Return:
        None
    End Self:
        
          0 
         / \
        -1 2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value7():
    '''
    Self:
        
          0 
         / \
        -1 1

    Return:
        None
    End Self:
        
          0 
         / \
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.parent = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node0
    node0.right_child = node2
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value8():
    '''
    Self:
        
           1
          / 
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value9():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
          1
         / 
        -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value10():
    '''
    Self:
        
            0
           / 
          -1 
         /   
        -2   

    Return:
        None
    End Self:
        
          0
         / 
        -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value11():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_delete_value12():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -2  

    Return:
        None
    End Self:
        
           1
          / 
          0 
         /  
        -2  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_delete_value13():
    '''
    Self:
        
           2
          / 
          0 
         /  
        -1  

    Return:
        None
    End Self:
        
           2
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -1
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_delete_value14():
    '''
    Self:
        
            0
           / 
          -1 
         /   
        -2   

    Return:
        None
    End Self:
        
            0
           / 
          -1 
         /   
        -2   

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child.value == -2
    assert bst0.root.left_child.left_child.right_child is None
    assert bst0.root.left_child.left_child.left_child is None


def test_delete_value15():
    '''
    Self:
        
         _2
        /  
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
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value16():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          0
         / 
        -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value17():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-3)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_delete_value18():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          0
         / 
        -2 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value19():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -3
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -3
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_delete_value20():
    '''
    Self:
        
          __0
         /   
        -3_  
           \ 
          -2 

    Return:
        None
    End Self:
        
          __0
         /   
        -3_  
           \ 
          -2 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -3
    node1.left_child = None
    node2 = node(0)
    node2.value = -2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -3
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -2
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_delete_value21():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        None
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -2
    node1.left_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -2
    assert bst0.root.left_child.left_child is None
    assert bst0.root.left_child.right_child.value == -1
    assert bst0.root.left_child.right_child.right_child is None
    assert bst0.root.left_child.right_child.left_child is None


def test_delete_value22():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        None
    End Self:
        
        -1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_delete_value23():
    '''
    Self:
        
         1
        / 
        0 

    Return:
        None
    End Self:
        
        1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_delete_value24():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 1
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value25():
    '''
    Self:
        
         2
        / 
        0 

    Return:
        None
    End Self:
        
         2
        / 
        0 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 2
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 2
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == 0
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value26():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = -1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.left_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value27():
    '''
    Self:
        
        -2__ 
            \
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.parent is None
    assert bst0.root.left_child.value == -1
    assert bst0.root.left_child.right_child is None
    assert bst0.root.left_child.left_child is None


def test_delete_value28():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_delete_value29():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0 
         \
         1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value30():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0 
         \
         2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value31():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 3
    node1.right_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 3
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 2
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_delete_value32():
    '''
    Self:
        
        0_ 
          \
          3
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          3
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 3
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 3
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_delete_value33():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        None
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 2
    node1.right_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(3)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 2
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child.value == 1
    assert bst0.root.right_child.left_child.right_child is None
    assert bst0.root.right_child.left_child.left_child is None


def test_delete_value34():
    '''
    Self:
        
        -1  
          \ 
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
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value35():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_delete_value36():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1 
          \
          1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value37():
    '''
    Self:
        
        -2  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -2  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_delete_value38():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1 
          \
          0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value39():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           2

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           2

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 2
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 2
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_delete_value40():
    '''
    Self:
        
        -1  
          \ 
          0 
           \
           1

    Return:
        None
    End Self:
        
        -1  
          \ 
          0 
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node2 = node(0)
    node2.value = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(2)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.left_child is None
    assert bst0.root.right_child.right_child.value == 1
    assert bst0.root.right_child.right_child.right_child is None
    assert bst0.root.right_child.right_child.left_child is None


def test_delete_value41():
    '''
    Self:
        
        0 
         \
         1

    Return:
        None
    End Self:
        
        1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 1
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_delete_value42():
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
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 1
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value43():
    '''
    Self:
        
        -1 
          \
          0

    Return:
        None
    End Self:
        
        -1

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_delete_value44():
    '''
    Self:
        
        -2 
          \
          0

    Return:
        None
    End Self:
        
        -2 
          \
          0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -2
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -2
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value45():
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
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -1
    node0.left_child = None
    node0.parent = None
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.left_child = None
    node1.parent = node0
    node0.right_child = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == -1
    assert bst0.root.left_child is None
    assert bst0.root.parent is None
    assert bst0.root.right_child.value == 0
    assert bst0.root.right_child.right_child is None
    assert bst0.root.right_child.left_child is None


def test_delete_value46():
    '''
    Self:
        
        -4122599998122094746

    Return:
        None
    End Self:
        <empty tree>
    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = -4122599998122094746
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-4122599998122094746)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root is None


def test_delete_value47():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(-1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_delete_value48():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Input Creation
    bst0 = BST()
    node0 = node(0)
    node0.value = 0
    node0.right_child = None
    node0.left_child = None
    node0.parent = None
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(1)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root.value == 0
    assert bst0.root.right_child is None
    assert bst0.root.left_child is None
    assert bst0.root.parent is None


def test_delete_value49():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Input Creation
    bst0 = BST()
    bst0.root = None
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.delete_value(0)
    # Repok check
    assert bst0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert bst0.root is None


