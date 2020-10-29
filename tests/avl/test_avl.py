from avl import *
import pytest


def test_insert1():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
    /  \           
  -3   -1          
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-3)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.left_child.value == -3
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_insert2():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -3              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
    /  \           
  -3   -1          
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -3
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child.value == -3
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert3():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert4():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
    /              
  -3              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
    /  \           
  -3   -1          
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -3
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -3
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert5():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert6():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
    /       /      
  -2        1       
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert7():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /          \   
  -2            2   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert8():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert9():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert10():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
    /  \           
  -3   -1          
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-3)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.left_child.value == -3
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_insert11():
    '''
    Self:
        
         0      
       /    \     
     -3     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
    /  \           
  -3   -1          
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -3
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child.value == -3
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert12():
    '''
    Self:
        
         0      
       /    \     
     -3     1    
       \           
      -2          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
    /  \           
  -3   -1          
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -3
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -3
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_insert13():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert14():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert15():
    '''
    Self:
        
         0      
       /    \     
     -2     2    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     2    
       \    /      
      -1    1       
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert16():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \       \   
      -1        2   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert17():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert18():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_insert19():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
    /       /      
  -2        1       
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_insert20():
    '''
    Self:
        
         0      
       /    \     
     -2     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     2    
       \    /      
      -1    1       
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_insert21():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_insert22():
    '''
    Self:
        
         0      
       /    \     
     -1     3    
            /      
           2       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /  \   
           1     3   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 3
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 3
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_insert23():
    '''
    Self:
        
         0      
       /    \     
     -1     3    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /  \   
           1     3   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 3
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 3
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_insert24():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_insert25():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /  \   
           1     3   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(3)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 3
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_insert26():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_insert27():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_insert28():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /          \   
  -2            2   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_insert29():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \       \   
      -1        2   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_insert30():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_insert31():
    '''
    Self:
        
        -2     
       /    \     
     -3     0    
               \   
               1   
                  

    Return:
        None
    End Self:
        
        -2     
       /    \     
     -3     0    
            /  \   
          -1    1   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -2
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -3
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -2
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.left_child.value == -3
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.left_child.value == -1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_insert32():
    '''
    Self:
        
        -1     
       /    \     
     -2     0    
               \   
               2   
                  

    Return:
        None
    End Self:
        
        -1     
       /    \     
     -2     1    
            /  \   
           0     2   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 0
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_insert33():
    '''
    Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    Return:
        None
    End Self:
        
        -1     
       /    \     
     -2     1    
            /  \   
           0     2   
                    

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.left_child.value == 0
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_insert34():
    '''
    Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    Return:
        None
    End Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_insert35():
    '''
    Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    Return:
        None
    End Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_insert36():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_insert37():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_insert38():
    '''
    Self:
        
      0    
    /  \   
  -2    1   
            

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_insert39():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert40():
    '''
    Self:
        
      0    
    /  \   
  -1    2   
            

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_insert41():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1


def test_insert42():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert43():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert44():
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
  -2    0   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_insert45():
    '''
    Self:
        
      0    
    /      
  -2      
          

    Return:
        None
    End Self:
        
     -1   
    /  \   
  -2    0   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_insert46():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert47():
    '''
    Self:
        
      0    
    /      
  -1      
          

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert48():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert49():
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
  -2    0   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_insert50():
    '''
    Self:
        
      0    
       \   
       2   
          

    Return:
        None
    End Self:
        
      1    
    /  \   
   0     2   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_insert51():
    '''
    Self:
        
      0    
       \   
       1   
          

    Return:
        None
    End Self:
        
      1    
    /  \   
   0     2   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_insert52():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_insert53():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_insert54():
    '''
    Self:
        
 -7718823657129427434 
      

    Return:
        None
    End Self:
        
    -7718823657129427434  
    /      
 -7718823657129427435     
          

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -7718823657129427434
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(-7718823657129427435)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -7718823657129427434
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == -7718823657129427435
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_insert55():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_insert56():
    '''
    Self:
        
   0   
      

    Return:
        None
    End Self:
        
   0   
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None


def test_insert57():
    '''
    Self:
        
    Return:
        None
    End Self:
        
   0   
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    avltree0.root = None
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.insert(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_find1():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        node: 0
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 3
    assert returnv.parent is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.height == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.height == 2
    assert returnv.left_child.right_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.height == 3
    assert returnv.right_child.parent.parent is None
    assert returnv.left_child.left_child.value == -2
    assert returnv.left_child.left_child.height == 1
    assert returnv.left_child.left_child.right_child is None
    assert returnv.left_child.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find2():
    '''
    Self:
        
         1      
       /    \     
      0      2    
    /              
  -1              
                  

    Return:
        node: 0
    End Self:
        
         1      
       /    \     
      0      2    
    /              
  -1              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = 0
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 2
    assert returnv.right_child is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.height == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.parent.value == 1
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.left_child.parent.value == 0
    assert returnv.left_child.parent.height == 2
    assert returnv.left_child.parent.right_child is None
    assert returnv.parent.right_child.value == 2
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -1
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find3():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        node: -2
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -2
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == -1
    assert returnv.parent.height == 2
    assert returnv.parent.right_child is None
    assert returnv.parent.left_child.value == -2
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.height == 3
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.right_child.value == 1
    assert returnv.parent.parent.right_child.height == 1
    assert returnv.parent.parent.right_child.right_child is None
    assert returnv.parent.parent.right_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find4():
    '''
    Self:
        
         1      
       /    \     
      0      2    
    /              
  -1              
                  

    Return:
        None
    End Self:
        
         1      
       /    \     
      0      2    
    /              
  -1              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = 0
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -1
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find5():
    '''
    Self:
        
         1      
       /    \     
      0      2    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         1      
       /    \     
      0      2    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = 0
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find6():
    '''
    Self:
        
         2      
       /    \     
      0      3    
    /              
  -1              
                  

    Return:
        None
    End Self:
        
         2      
       /    \     
      0      3    
    /              
  -1              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 2
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 3
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = 0
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 2
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 3
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -1
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find7():
    '''
    Self:
        
         1      
       /    \     
      0      2    
    /              
  -1              
                  

    Return:
        node: 2
    End Self:
        
         1      
       /    \     
      0      2    
    /              
  -1              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = 0
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 2
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 1
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 2
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == 0
    assert returnv.parent.left_child.height == 2
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child.value == -1
    assert returnv.parent.left_child.left_child.height == 1
    assert returnv.parent.left_child.left_child.right_child is None
    assert returnv.parent.left_child.left_child.left_child is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -1
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find8():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find9():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_find10():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        node: 0
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 3
    assert returnv.parent is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.height == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.left_child.value == -2
    assert returnv.left_child.height == 2
    assert returnv.left_child.left_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.height == 3
    assert returnv.right_child.parent.parent is None
    assert returnv.left_child.right_child.value == -1
    assert returnv.left_child.right_child.height == 1
    assert returnv.left_child.right_child.right_child is None
    assert returnv.left_child.right_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find11():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        node: -2
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -2
    assert returnv.height == 2
    assert returnv.left_child is None
    assert returnv.right_child.value == -1
    assert returnv.right_child.height == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.right_child.parent.value == -2
    assert returnv.right_child.parent.height == 2
    assert returnv.right_child.parent.left_child is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find12():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-3)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find13():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        node: -1
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == -2
    assert returnv.parent.height == 2
    assert returnv.parent.left_child is None
    assert returnv.parent.right_child.value == -1
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.height == 3
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.right_child.value == 1
    assert returnv.parent.parent.right_child.height == 1
    assert returnv.parent.parent.right_child.right_child is None
    assert returnv.parent.parent.right_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find14():
    '''
    Self:
        
         0      
       /    \     
     -3     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -3     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -3
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -3
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find15():
    '''
    Self:
        
         0      
       /    \     
     -3     1    
       \           
      -2          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -3     1    
       \           
      -2          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -3
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -3
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -2
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find16():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        node: 1
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == -2
    assert returnv.parent.left_child.height == 2
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.left_child.right_child.value == -1
    assert returnv.parent.left_child.right_child.height == 1
    assert returnv.parent.left_child.right_child.right_child is None
    assert returnv.parent.left_child.right_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find17():
    '''
    Self:
        
         0      
       /    \     
     -2     2    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     2    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find18():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_find19():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        node: 0
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 3
    assert returnv.parent is None
    assert returnv.right_child.value == 2
    assert returnv.right_child.height == 2
    assert returnv.right_child.right_child is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.height == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.right_child.left_child.value == 1
    assert returnv.right_child.left_child.height == 1
    assert returnv.right_child.left_child.right_child is None
    assert returnv.right_child.left_child.left_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.height == 3
    assert returnv.right_child.parent.parent is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find20():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        node: -1
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 2
    assert returnv.parent.right_child.height == 2
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.right_child.left_child.value == 1
    assert returnv.parent.right_child.left_child.height == 1
    assert returnv.parent.right_child.left_child.right_child is None
    assert returnv.parent.right_child.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find21():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find22():
    '''
    Self:
        
         0      
       /    \     
     -2     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find23():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        node: 2
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 2
    assert returnv.height == 2
    assert returnv.right_child is None
    assert returnv.left_child.value == 1
    assert returnv.left_child.height == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.left_child.parent.value == 2
    assert returnv.left_child.parent.height == 2
    assert returnv.left_child.parent.right_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find24():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        node: 1
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 2
    assert returnv.parent.height == 2
    assert returnv.parent.right_child is None
    assert returnv.parent.left_child.value == 1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.height == 3
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.left_child.value == -1
    assert returnv.parent.parent.left_child.height == 1
    assert returnv.parent.parent.left_child.right_child is None
    assert returnv.parent.parent.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find25():
    '''
    Self:
        
         0      
       /    \     
     -1     3    
            /      
           2       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     3    
            /      
           2       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 3
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 3
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 2
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find26():
    '''
    Self:
        
         0      
       /    \     
     -1     3    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     3    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 3
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 3
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find27():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(3)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_find28():
    '''
    Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    Return:
        node: -1
    End Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.height == 3
    assert returnv.parent is None
    assert returnv.right_child.value == 0
    assert returnv.right_child.height == 2
    assert returnv.right_child.left_child is None
    assert returnv.left_child.value == -2
    assert returnv.left_child.height == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.right_child.right_child.value == 1
    assert returnv.right_child.right_child.height == 1
    assert returnv.right_child.right_child.right_child is None
    assert returnv.right_child.right_child.left_child is None
    assert returnv.right_child.parent.value == -1
    assert returnv.right_child.parent.height == 3
    assert returnv.right_child.parent.parent is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find29():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        node: -1
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.height == 2
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert returnv.parent.right_child.right_child.value == 2
    assert returnv.parent.right_child.right_child.height == 1
    assert returnv.parent.right_child.right_child.right_child is None
    assert returnv.parent.right_child.right_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find30():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find31():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -2     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find32():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        node: 1
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.height == 2
    assert returnv.left_child is None
    assert returnv.right_child.value == 2
    assert returnv.right_child.height == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 3
    assert returnv.parent.parent is None
    assert returnv.right_child.parent.value == 1
    assert returnv.right_child.parent.height == 2
    assert returnv.right_child.parent.left_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find33():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
               \   
               3   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     2    
               \   
               3   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 3
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 3
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find34():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        node: 2
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 2
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 1
    assert returnv.parent.height == 2
    assert returnv.parent.left_child is None
    assert returnv.parent.right_child.value == 2
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.parent.value == 0
    assert returnv.parent.parent.height == 3
    assert returnv.parent.parent.parent is None
    assert returnv.parent.parent.left_child.value == -1
    assert returnv.parent.parent.left_child.height == 1
    assert returnv.parent.parent.left_child.right_child is None
    assert returnv.parent.parent.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find35():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               3   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               3   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 3
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 3
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find36():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    Return:
        None
    End Self:
        
         0      
       /    \     
     -1     1    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(3)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_find37():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        node: 0
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 2
    assert returnv.parent is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.height == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.height == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.height == 2
    assert returnv.right_child.parent.parent is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find38():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        node: -1
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 2
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find39():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find40():
    '''
    Self:
        
      0    
    /  \   
  -2    1   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -2    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find41():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        node: 1
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 1
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 0
    assert returnv.parent.height == 2
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 1
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert returnv.parent.left_child.value == -1
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find42():
    '''
    Self:
        
      0    
    /  \   
  -1    2   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    2   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find43():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(2)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find44():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 2
    assert returnv.right_child is None
    assert returnv.parent is None
    assert returnv.left_child.value == -1
    assert returnv.left_child.height == 1
    assert returnv.left_child.right_child is None
    assert returnv.left_child.left_child is None
    assert returnv.left_child.parent.value == 0
    assert returnv.left_child.parent.height == 2
    assert returnv.left_child.parent.right_child is None
    assert returnv.left_child.parent.parent is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find45():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == 1
    assert returnv.parent.height == 2
    assert returnv.parent.right_child is None
    assert returnv.parent.parent is None
    assert returnv.parent.left_child.value == 0
    assert returnv.parent.left_child.height == 1
    assert returnv.parent.left_child.right_child is None
    assert returnv.parent.left_child.left_child is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find46():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find47():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 2
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 2
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find48():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_find49():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 2
    assert returnv.left_child is None
    assert returnv.parent is None
    assert returnv.right_child.value == 1
    assert returnv.right_child.height == 1
    assert returnv.right_child.right_child is None
    assert returnv.right_child.left_child is None
    assert returnv.right_child.parent.value == 0
    assert returnv.right_child.parent.height == 2
    assert returnv.right_child.parent.left_child is None
    assert returnv.right_child.parent.parent is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_find50():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_find51():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == 0
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent.value == -1
    assert returnv.parent.height == 2
    assert returnv.parent.left_child is None
    assert returnv.parent.parent is None
    assert returnv.parent.right_child.value == 0
    assert returnv.parent.right_child.height == 1
    assert returnv.parent.right_child.right_child is None
    assert returnv.parent.right_child.left_child is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_find52():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -2
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -2
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_find53():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 0
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_find54():
    '''
    Self:
        
 -9223367638808264694 
      

    Return:
        node: -9223367638808264694
    End Self:
        
 -9223367638808264694 
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -9223367638808264694
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-9223367638808264694)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv.value == -9223367638808264694
    assert returnv.height == 1
    assert returnv.right_child is None
    assert returnv.left_child is None
    assert returnv.parent is None
    assert avltree0.root.value == -9223367638808264694
    assert avltree0.root.height == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None


def test_find55():
    '''
    Self:
        
   0   
      

    Return:
        None
    End Self:
        
   0   
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(-1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None


def test_find56():
    '''
    Self:
        
   0   
      

    Return:
        None
    End Self:
        
   0   
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(1)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.height == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None


def test_find57():
    '''
    Self:
        
    Return:
        None
    End Self:
        
    '''
    # Input Creation
    avltree0 = AVLTree()
    avltree0.root = None
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.find(0)
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv is None
    assert avltree0.root is None


def test_height1():
    '''
    Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    Return:
        3
    End Self:
        
         0      
       /    \     
     -1     1    
    /              
  -2              
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 2
    node2.right_child = None
    node4 = node(0)
    node4.value = -2
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.height == 1
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.left_child is None


def test_height2():
    '''
    Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    Return:
        3
    End Self:
        
         0      
       /    \     
     -2     1    
       \           
      -1          
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 2
    node2.left_child = None
    node4 = node(0)
    node4.value = -1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.height == 1
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.left_child is None


def test_height3():
    '''
    Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    Return:
        3
    End Self:
        
         0      
       /    \     
     -1     2    
            /      
           1       
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 2
    node3.height = 2
    node3.right_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert avltree0.root.value == 0
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.height == 1
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.left_child is None


def test_height4():
    '''
    Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    Return:
        3
    End Self:
        
        -1     
       /    \     
     -2     0    
               \   
               1   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.height = 3
    node1.parent = None
    node3 = node(0)
    node3.value = 0
    node3.height = 2
    node3.left_child = None
    node4 = node(0)
    node4.value = 1
    node4.height = 1
    node4.right_child = None
    node4.left_child = None
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -2
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 3
    assert avltree0.root.value == -1
    assert avltree0.root.height == 3
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.height == 1
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.left_child is None


def test_height5():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        2
    End Self:
        
      0    
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.parent = None
    node3 = node(0)
    node3.value = 1
    node3.height = 1
    node3.right_child = None
    node3.left_child = None
    node3.parent = node1
    node1.right_child = node3
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 2
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


def test_height6():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.right_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = -1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 2
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.left_child is None


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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.height = 2
    node1.left_child = None
    node1.parent = None
    node2 = node(0)
    node2.value = 1
    node2.height = 1
    node2.right_child = None
    node2.left_child = None
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 2
    assert avltree0.root.value == 0
    assert avltree0.root.height == 2
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.left_child is None


def test_height8():
    '''
    Self:
        
 9063274951741954 
      

    Return:
        1
    End Self:
        
 9063274951741954 
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 9063274951741954
    node1.height = 1
    node1.right_child = None
    node1.left_child = None
    node1.parent = None
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 1
    assert avltree0.root.value == 9063274951741954
    assert avltree0.root.height == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None


def test_height9():
    '''
    Self:
        
    Return:
        0
    End Self:
        
    '''
    # Input Creation
    avltree0 = AVLTree()
    avltree0.root = None
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.height()
    # Repok check
    assert avltree0.repok()
    # Regression assertions (Captures the current behavior)
    assert returnv == 0
    assert avltree0.root is None


