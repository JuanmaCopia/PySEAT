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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
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
    avl0.insert(0)
    # Assertions
    # Repok check
    assert avl0.repok()
    assert avl0.root.data == 0
    assert avl0.root.right is None
    assert avl0.root.left is None
    assert avl0.root.parent is None
    assert avl0.root.height == 0


