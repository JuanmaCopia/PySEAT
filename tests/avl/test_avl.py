from avl import *


def test_insert1():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert2():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 1)
    node1.data = 1
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert3():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 1)
    node1.data = 1
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert4():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 1)
    node1.data = 1
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert5():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert6():
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
    avl0 = AVL()
    node1 = Node(None, 1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 1
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_insert7():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert8():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert9():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert10():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert11():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
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


def test_insert12():
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
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 1
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_insert13():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.insert(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete1():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete2():
    '''
    Self:
        
        0 
         \
         0

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete3():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        <empty tree>
    '''
    # Self Generation
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root is None


def test_delete4():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, -1)
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
    returnv = avl0.delete(-1)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete5():
    '''
    Self:
        
          0
         / 
        -1 

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, -1)
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
    returnv = avl0.delete(-1)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete6():
    '''
    Self:
        
         0
        / 
        0 

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete7():
    '''
    Self:
        
          0
         / 
        -2 

    Return:
        None
    End Self:
        
        -2

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, -2)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == -2
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete8():
    '''
    Self:
        
        1

    Return:
        None
    End Self:
        
        1

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 1
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete9():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 1)
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
    returnv = avl0.delete(1)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete10():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, -1)
    node1.data = -1
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == -1
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete11():
    '''
    Self:
        
        0 
         \
         2

    Return:
        None
    End Self:
        
        2

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 2)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 2
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete12():
    '''
    Self:
        
        0 
         \
         0

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete13():
    '''
    Self:
        
        -1

    Return:
        None
    End Self:
        
        -1

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, -1)
    node1.data = -1
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == -1
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_delete14():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Self Generation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.delete(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root is None


def test_find_min1():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.right is None
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_find_min2():
    '''
    Self:
        
        0

    Return:
        node: 0
    End Self:
        
        0

    '''
    # Self Generation
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
    returnv = avl0.find_min()
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.parent is None
    assert returnv.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_find_min3():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Self Generation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.find_min()
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root is None


def test_next_larger1():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.left is None
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger2():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
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
    returnv = avl0.next_larger(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_next_larger3():
    '''
    Self:
        
         1
        / 
        0 

    Return:
        node: 1
    End Self:
        
         1
        / 
        0 

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 1)
    node1.data = 1
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv.data == 1
    assert returnv.right is None
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.left.data == 0
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 1
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger4():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, -1)
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
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.parent is None
    assert returnv.height == 0
    assert returnv.left.data == -1
    assert returnv.left.right is None
    assert returnv.left.left is None
    assert returnv.left.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == -1
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger5():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == 0
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger6():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.right = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, -2)
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
    returnv = avl0.next_larger(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.left.data == -2
    assert avl0.root.left.right is None
    assert avl0.root.left.left is None
    assert avl0.root.left.height == 0


def test_next_larger7():
    '''
    Self:
        
        1

    Return:
        None
    End Self:
        
        1

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.parent = None
    node1.height = 0
    avl0.root = node1
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 1
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_next_larger8():
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
    avl0 = AVL()
    node1 = Node(None, -1)
    node1.data = -1
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == -1
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger9():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 1)
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 1
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger10():
    '''
    Self:
        
        0 
         \
         2

    Return:
        node: 2
    End Self:
        
        0 
         \
         2

    '''
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 2)
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
    returnv = avl0.next_larger(0)
    # Assertions
    assert returnv.data == 2
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.left is None
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 2
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger11():
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
    # Self Generation
    avl0 = AVL()
    node1 = Node(None, 0)
    node1.data = 0
    node1.left = None
    node1.parent = None
    node1.height = 0
    node2 = Node(node1, 0)
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
    # Assertions
    assert returnv.data == 0
    assert returnv.right is None
    assert returnv.left is None
    assert returnv.height == 0
    assert returnv.parent.data == 0
    assert returnv.parent.left is None
    assert returnv.parent.parent is None
    assert returnv.parent.height == 0
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0
    assert avl0.root.right.data == 0
    assert avl0.root.right.right is None
    assert avl0.root.right.left is None
    assert avl0.root.right.height == 0


def test_next_larger12():
    '''
    Self:
        
        0

    Return:
        None
    End Self:
        
        0

    '''
    # Self Generation
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
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


def test_next_larger13():
    '''
    Self:
        <empty tree>
    Return:
        None
    End Self:
        <empty tree>
    '''
    # Self Generation
    avl0 = AVL()
    avl0.root = None
    # Repok check
    assert avl0.repok()
    # Method call
    returnv = avl0.next_larger(0)
    # Assertions
    assert returnv is None
    # Repok check
    assert avl0.repok()
    assert avl0.root is None


