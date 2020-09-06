from avl import *
import pytest


def test_delete_value1():
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
        
     -1   
    /  \   
  -2    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value2():
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
    /  \   
  -1    2   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = 0
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value3():
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
                   

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value4():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = 0
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -1
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_delete_value5():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = 0
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_delete_value6():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = 0
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 3
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 2
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 3
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -1
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_delete_value7():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_delete_value8():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.right_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.left_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.left_child.value == -2
    assert avltree0.root.left_child.left_child.left_child is None
    assert avltree0.root.left_child.left_child.right_child is None
    assert avltree0.root.left_child.left_child.height == 1


def test_delete_value9():
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
        
     -1   
    /  \   
  -2    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value10():
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
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value11():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-3)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_delete_value12():
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
                   

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value13():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -3
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -3
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_delete_value14():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -3
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -3
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.right_child.value == -2
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_delete_value15():
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
        
     -1   
    /  \   
  -2    0   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value16():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_delete_value17():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.height = 2
    node4 = node(0)
    node4.value = -1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node2
    node2.right_child = node4
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1
    assert avltree0.root.left_child.right_child.value == -1
    assert avltree0.root.left_child.right_child.left_child is None
    assert avltree0.root.left_child.right_child.right_child is None
    assert avltree0.root.left_child.right_child.height == 1


def test_delete_value18():
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
        
         1      
       /    \     
     -1     2    
                   

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value19():
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
        
      1    
    /  \   
   0     2   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value20():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_delete_value21():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_delete_value22():
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
    /  \   
  -1    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value23():
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
                   

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value24():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 3
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 3
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child.value == 2
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_delete_value25():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 3
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 3
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_delete_value26():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.right_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.left_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(3)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.left_child.value == 1
    assert avltree0.root.right_child.left_child.left_child is None
    assert avltree0.root.right_child.left_child.right_child is None
    assert avltree0.root.right_child.left_child.height == 1


def test_delete_value27():
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
        
      1    
    /  \   
  -1    2   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value28():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1


def test_delete_value29():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1


def test_delete_value30():
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
    /  \   
  -2    1   
            

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 0
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value31():
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
               \   
               1   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -2
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -3
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 0
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -2
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -3
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1


def test_delete_value32():
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
                   

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value33():
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
     -2     0    
               \   
               2   
                  

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 0
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 2
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child.value == 2
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1


def test_delete_value34():
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
    node1.parent = None
    node1.height = 3
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 0
    node3.left_child = None
    node3.height = 2
    node4 = node(0)
    node4.value = 1
    node4.left_child = None
    node4.right_child = None
    node4.height = 1
    node4.parent = node3
    node3.right_child = node4
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.parent is None
    assert avltree0.root.height == 3
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 0
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.height == 2
    assert avltree0.root.right_child.right_child.value == 1
    assert avltree0.root.right_child.right_child.left_child is None
    assert avltree0.root.right_child.right_child.right_child is None
    assert avltree0.root.right_child.right_child.height == 1


def test_delete_value35():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

    Return:
        None
    End Self:
        
      1    
    /      
  -1      
          

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_delete_value36():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

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
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value37():
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
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value38():
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
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -2
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value39():
    '''
    Self:
        
      0    
    /  \   
  -1    1   
            

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
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_delete_value40():
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
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 2
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value41():
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
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    node3 = node(0)
    node3.value = 1
    node3.left_child = None
    node3.right_child = None
    node3.height = 1
    node3.parent = node1
    node1.right_child = node3
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value42():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.right_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == -1
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_delete_value43():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 1
    node1.right_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 0
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_delete_value44():
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
    node1.right_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 0
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 1
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_delete_value45():
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
    node1.right_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 0
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 2
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == 0
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_delete_value46():
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
    node1.right_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = -1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.left_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.left_child.value == -1
    assert avltree0.root.left_child.left_child is None
    assert avltree0.root.left_child.right_child is None
    assert avltree0.root.left_child.height == 1


def test_delete_value47():
    '''
    Self:
        
     -1   
       \   
       0   
          

    Return:
        None
    End Self:
        
   0   
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = -1
    node1.left_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 0
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_delete_value48():
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
    node1.left_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value49():
    '''
    Self:
        
      0    
       \   
       1   
          

    Return:
        None
    End Self:
        
   0   
      

    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_delete_value50():
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
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 0
    node1.left_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 2
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.right_child.value == 2
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value51():
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
    node1.left_child = None
    node1.parent = None
    node1.height = 2
    node2 = node(0)
    node2.value = 1
    node2.left_child = None
    node2.right_child = None
    node2.height = 1
    node2.parent = node1
    node1.right_child = node2
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(2)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 2
    assert avltree0.root.right_child.value == 1
    assert avltree0.root.right_child.left_child is None
    assert avltree0.root.right_child.right_child is None
    assert avltree0.root.right_child.height == 1


def test_delete_value52():
    '''
    Self:
        
 4294967295 
      

    Return:
        None
    End Self:
        
    '''
    # Input Creation
    avltree0 = AVLTree()
    node1 = node(0)
    node1.value = 4294967295
    node1.left_child = None
    node1.right_child = None
    node1.parent = None
    node1.height = 1
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(4294967295)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root is None


def test_delete_value53():
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
    node1.left_child = None
    node1.right_child = None
    node1.parent = None
    node1.height = 1
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(-1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_delete_value54():
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
    node1.left_child = None
    node1.right_child = None
    node1.parent = None
    node1.height = 1
    avltree0.root = node1
    # Repok check
    assert avltree0.repok()
    # Method call
    returnv = avltree0.delete_value(1)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root.value == 0
    assert avltree0.root.left_child is None
    assert avltree0.root.right_child is None
    assert avltree0.root.parent is None
    assert avltree0.root.height == 1


def test_delete_value55():
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
    returnv = avltree0.delete_value(0)
    # Repok check
    assert avltree0.repok()
    # Assertions
    assert returnv is None
    assert avltree0.root is None


