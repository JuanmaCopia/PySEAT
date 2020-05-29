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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -2
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    assert bst0.root.right.right.data == 2
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left.data == -2
    assert bst0.root.left.left.left.right is None
    assert bst0.root.left.left.left.left is None


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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -2
    assert bst0.root.left.left.left is None
    assert bst0.root.left.left.right.data == -1
    assert bst0.root.left.left.right.right is None
    assert bst0.root.left.left.right.left is None


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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


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
    node1 = Node(0)
    node1.data = 2
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_insert13():
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
           / \
          -1 1
         /    
        -2    

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node3 = Node(0)
    node3.data = -2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -2
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_insert14():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node3 = Node(0)
    node3.data = -2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -2
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_insert15():
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
         /   \ 
        -3  -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-3)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None
    assert bst0.root.left.left.data == -3
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_insert16():
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
        
          ____0
         /     
        -3___  
             \ 
            -1 
           /   
          -2   

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -3
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -3
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left.data == -2
    assert bst0.root.left.right.left.right is None
    assert bst0.root.left.right.left.left is None


def test_insert17():
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
        
          ____0
         /     
        -3_    
           \   
          -2_  
             \ 
            -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -3
    node2.left = None
    node3 = Node(0)
    node3.data = -2
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -3
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -2
    assert bst0.root.left.right.left is None
    assert bst0.root.left.right.right.data == -1
    assert bst0.root.left.right.right.right is None
    assert bst0.root.left.right.right.left is None


def test_insert18():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_insert19():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -2
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_insert27():
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
         /    \
        -3    0
             / 
            -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = -2
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-3)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -2
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.left.data == -3
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_insert28():
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
        
        0__ 
           \
           3
          / 
          2 
         /  
         1  

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 3
    node2.right = None
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 3
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 2
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left.data == 1
    assert bst0.root.right.left.left.right is None
    assert bst0.root.right.left.left.left is None


def test_insert29():
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
        
        0__ 
           \
          _3
         /  
         1  
          \ 
          2 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 3
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 3
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.left is None
    assert bst0.root.right.left.right.data == 2
    assert bst0.root.right.left.right.right is None
    assert bst0.root.right.left.right.left is None


def test_insert30():
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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_insert31():
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
         / \
         1 3

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(3)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right.data == 3
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_insert32():
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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


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
    node1 = Node(0)
    node1.data = -2
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 2
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left.data == 1
    assert bst0.root.right.right.left.right is None
    assert bst0.root.right.right.left.left is None


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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.left is None
    assert bst0.root.right.right.right.data == 2
    assert bst0.root.right.right.right.right is None
    assert bst0.root.right.right.right.left is None


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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_insert40():
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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_insert41():
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
        -1 1

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_insert42():
    '''
    Self:
        
        -2 
          \
          0

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
    node1 = Node(0)
    node1.data = -2
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
    returnv = bst0.insert(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_insert43():
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
           \
           1

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
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
    returnv = bst0.insert(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_insert44():
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
    node1 = Node(0)
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
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_insert46():
    '''
    Self:
        
        4294967295

    Return:
        None
    End Self:
        
              ____4294967295
             /              
        4294967294          

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 4294967295
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(4294967294)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 4294967295
    assert bst0.root.right is None
    assert bst0.root.left.data == 4294967294
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


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
    node1 = Node(0)
    node1.data = -1
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.insert(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left is None


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
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left is None


def test_find50():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right.data == 1
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find51():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == -1
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find52():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find53():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -2
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find54():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 1
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find55():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find56():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find57():
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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 1
    assert returnv.right is None
    assert returnv.left.data == 0
    assert returnv.left.right is None
    assert returnv.left.left.data == -1
    assert returnv.left.left.right is None
    assert returnv.left.left.left is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find58():
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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find59():
    '''
    Self:
        
           1
          / 
          0 
         /  
        -1  

    Return:
        node: -1
    End Self:
        
           1
          / 
          0 
         /  
        -1  

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == -1
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find60():
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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find61():
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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -2
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find62():
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
    node1 = Node(0)
    node1.data = 2
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find63():
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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_find64():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        node: 0
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left.data == -2
    assert returnv.left.left is None
    assert returnv.left.right.data == -1
    assert returnv.left.right.right is None
    assert returnv.left.right.left is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find65():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        node: 0
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 2
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.left is None
    assert returnv.right.data == 1
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find66():
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
    node1 = Node(0)
    node1.data = 2
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find67():
    '''
    Self:
        
         _2
        /  
        0  
         \ 
         1 

    Return:
        node: 1
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 2
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 1
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find68():
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
        
         _3
        /  
        0  
         \ 
         2 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 3
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 3
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 2
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find69():
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
        
         _3
        /  
        0  
         \ 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 3
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 3
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find70():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_find71():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find72():
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
    node1 = Node(0)
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
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find73():
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
    node1 = Node(0)
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
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find74():
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
    node1 = Node(0)
    node1.data = 2
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
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find75():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_find76():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        node: 0
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.left is None
    assert returnv.right.data == 2
    assert returnv.right.right is None
    assert returnv.right.left.data == 1
    assert returnv.right.left.right is None
    assert returnv.right.left.left is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find77():
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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find78():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        node: 0
    End Self:
        
        -2__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = -2
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find79():
    '''
    Self:
        
        -2__ 
            \
            0
           / 
          -1 

    Return:
        node: -1
    End Self:
        
        -2__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = -2
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == -1
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find80():
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
        
        -3__ 
            \
            0
           / 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = -3
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -3
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find81():
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
        
        -3__ 
            \
            0
           / 
          -2 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = -3
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -2
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -3
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -2
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find82():
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
    node1 = Node(0)
    node1.data = -2
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_find83():
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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == -1
    assert returnv.left is None
    assert returnv.right.data == 0
    assert returnv.right.left is None
    assert returnv.right.right.data == 1
    assert returnv.right.right.right is None
    assert returnv.right.right.left is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find84():
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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.left = None
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 2
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find85():
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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 0
    assert returnv.left is None
    assert returnv.right.data == 1
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find86():
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
    node1 = Node(0)
    node1.data = -2
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find87():
    '''
    Self:
        
        0  
         \ 
         1 
          \
          2

    Return:
        node: 2
    End Self:
        
        0  
         \ 
         1 
          \
          2

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.left = None
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 2
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 2
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find88():
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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 2
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 2
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find89():
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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_find90():
    '''
    Self:
        
        -1 
          \
          0

    Return:
        node: -1
    End Self:
        
        -1 
          \
          0

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
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
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == -1
    assert returnv.left is None
    assert returnv.right.data == 0
    assert returnv.right.right is None
    assert returnv.right.left is None
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_find91():
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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_find92():
    '''
    Self:
        
        0 
         \
         1

    Return:
        node: 1
    End Self:
        
        0 
         \
         1

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 1
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_find93():
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
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_find94():
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
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 1
    node2.right = None
    node2.left = None
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(2)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_find95():
    '''
    Self:
        
        4294967295

    Return:
        node: 4294967295
    End Self:
        
        4294967295

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 4294967295
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(4294967295)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv.data == 4294967295
    assert returnv.right is None
    assert returnv.left is None
    assert bst0.root.data == 4294967295
    assert bst0.root.right is None
    assert bst0.root.left is None


def test_find96():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left is None


def test_find97():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(1)
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv is None
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left is None


def test_find98():
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
    # Assertions
    assert returnv is None
    assert bst0.root is None


def test_height99():
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
    node1 = Node(0)
    node1.data = 0
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node1.right = node3
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 2
    assert bst0.root.data == 0
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_height100():
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
    node1 = Node(0)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 3
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left is None


def test_height101():
    '''
    Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    Return:
        3
    End Self:
        
          __0
         /   
        -2_  
           \ 
          -1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -2
    node2.left = None
    node3 = Node(0)
    node3.data = -1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 3
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None


def test_height102():
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
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node2 = Node(0)
    node2.data = -1
    node2.right = None
    node2.left = None
    node1.left = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 2
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None


def test_height103():
    '''
    Self:
        
        0_ 
          \
          2
         / 
         1 

    Return:
        3
    End Self:
        
        0_ 
          \
          2
         / 
         1 

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 0
    node1.left = None
    node2 = Node(0)
    node2.data = 2
    node2.right = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.left = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 3
    assert bst0.root.data == 0
    assert bst0.root.left is None
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left is None


def test_height104():
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
    node1 = Node(0)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.left = None
    node3 = Node(0)
    node3.data = 1
    node3.right = None
    node3.left = None
    node2.right = node3
    node1.right = node2
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 3
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None


def test_height105():
    '''
    Self:
        
        -1 
          \
          0

    Return:
        2
    End Self:
        
        -1 
          \
          0

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
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
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 2
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None


def test_height106():
    '''
    Self:
        
        4294967295

    Return:
        1
    End Self:
        
        4294967295

    '''
    # Input Creation
    bst0 = BST()
    node1 = Node(0)
    node1.data = 4294967295
    node1.right = None
    node1.left = None
    bst0.root = node1
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.height()
    # Repok check
    assert bst0.repok()
    # Assertions
    assert returnv == 1
    assert bst0.root.data == 4294967295
    assert bst0.root.right is None
    assert bst0.root.left is None


def test_height107():
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
    # Assertions
    assert returnv == 0
    assert bst0.root is None


