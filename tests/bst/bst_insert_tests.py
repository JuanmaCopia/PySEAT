from bst import Node, BST


def insert_test1():
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
    node0 = Node(3)
    node0.data = 3
    node0.right = None
    node1 = Node(2)
    node1.data = 2
    node1.right = None
    node2 = Node(1)
    node2.data = 1
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
    assert bst0.root.data == 3
    assert bst0.root.right is None
    assert bst0.root.left.data == 2
    assert bst0.root.left.right is None
    assert bst0.root.left.left.data == 1
    assert bst0.root.left.left.right is None
    assert bst0.root.left.left.left.data == 0
    assert bst0.root.left.left.left.right is None
    assert bst0.root.left.left.left.left is None
    print('Test1: OK')


def insert_test2():
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
          _1 
         /   
        -1   
          \  
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
    node2 = Node(-1)
    node2.data = -1
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
    assert bst0.root.left.left.data == -1
    assert bst0.root.left.left.left is None
    assert bst0.root.left.left.right.data == 0
    assert bst0.root.left.left.right.right is None
    assert bst0.root.left.left.right.left is None
    print('Test2: OK')


def insert_test3():
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
    print('Test3: OK')


def insert_test4():
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
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node1 = Node(-1)
    node1.data = -1
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
    assert bst0.root.data == 0
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    print('Test4: OK')


def insert_test5():
    '''
    Self:
        
          _2
         /  
        -1  
          \ 
          1 

    Return:
        None
    End Self:
        
          _2
         /  
        -1  
          \ 
          1 

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(2)
    node0.data = 2
    node0.right = None
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node2.left = None
    node1.right = node2
    node0.left = node1
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.insert(1)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == -1
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None
    print('Test5: OK')


def insert_test6():
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
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(-1)
    node2.data = -1
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
    assert bst0.root.left.data == -2
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.left is None
    assert bst0.root.left.right.right.data == 0
    assert bst0.root.left.right.right.right is None
    assert bst0.root.left.right.right.left is None
    print('Test6: OK')


def insert_test7():
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
    print('Test7: OK')


def insert_test8():
    '''
    Self:
        
         2
        / 
        0 

    Return:
        None
    End Self:
        
         _2
        /  
        0  
         \ 
         1 

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(2)
    node0.data = 2
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
    bst0.insert(1)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 2
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.left is None
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.right is None
    assert bst0.root.left.right.left is None
    print('Test8: OK')


def insert_test9():
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
    print('Test9: OK')


def insert_test10():
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
    node0 = Node(1)
    node0.data = 1
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
    assert bst0.root.data == 1
    assert bst0.root.right is None
    assert bst0.root.left.data == 0
    assert bst0.root.left.right is None
    assert bst0.root.left.left is None
    print('Test10: OK')


def insert_test11():
    '''
    Self:
        
        -1_ 
           \
           2
          / 
          1 

    Return:
        None
    End Self:
        
        -1__ 
            \
            2
           / 
           1 
          /  
          0  

    '''
    # Self Generation
    bst0 = BST()
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node1 = Node(2)
    node1.data = 2
    node1.right = None
    node2 = Node(1)
    node2.data = 1
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
    assert bst0.root.right.data == 2
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.right is None
    assert bst0.root.right.left.left.data == 0
    assert bst0.root.right.left.left.right is None
    assert bst0.root.right.left.left.left is None
    print('Test11: OK')


def insert_test12():
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
    node0 = Node(-2)
    node0.data = -2
    node0.left = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(-1)
    node2.data = -1
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
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == 1
    assert bst0.root.right.right is None
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.left is None
    assert bst0.root.right.left.right.data == 0
    assert bst0.root.right.left.right.right is None
    assert bst0.root.right.left.right.left is None
    print('Test12: OK')


def insert_test13():
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
    print('Test13: OK')


def insert_test14():
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
    node0 = Node(0)
    node0.data = 0
    node0.left = None
    node1 = Node(2)
    node1.data = 2
    node1.right = None
    node1.left = None
    node0.right = node1
    bst0.root = node0
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
    print('Test14: OK')


def insert_test15():
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
    node0 = Node(-2)
    node0.data = -2
    node0.left = None
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(1)
    node2.data = 1
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
    assert bst0.root.right.right.data == 1
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left.data == 0
    assert bst0.root.right.right.left.right is None
    assert bst0.root.right.right.left.left is None
    print('Test15: OK')


def insert_test16():
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
    node0 = Node(-3)
    node0.data = -3
    node0.left = None
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(-1)
    node2.data = -1
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
    assert bst0.root.data == -3
    assert bst0.root.left is None
    assert bst0.root.right.data == -2
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == -1
    assert bst0.root.right.right.left is None
    assert bst0.root.right.right.right.data == 0
    assert bst0.root.right.right.right.right is None
    assert bst0.root.right.right.right.left is None
    print('Test16: OK')


def insert_test17():
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
    print('Test17: OK')


def insert_test18():
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
    node0 = Node(-2)
    node0.data = -2
    node0.left = None
    node1 = Node(-1)
    node1.data = -1
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
    assert bst0.root.data == -2
    assert bst0.root.left is None
    assert bst0.root.right.data == -1
    assert bst0.root.right.left is None
    assert bst0.root.right.right.data == 0
    assert bst0.root.right.right.right is None
    assert bst0.root.right.right.left is None
    print('Test18: OK')


def insert_test19():
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
    print('Test19: OK')


def insert_test20():
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
    node0 = Node(-1)
    node0.data = -1
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
    assert bst0.root.data == -1
    assert bst0.root.left is None
    assert bst0.root.right.data == 0
    assert bst0.root.right.right is None
    assert bst0.root.right.left is None
    print('Test20: OK')


def insert_test21():
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
    print('Test21: OK')


def insert_test22():
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
    print('Test22: OK')


if __name__ == '__main__':
    insert_test1()
    insert_test2()
    insert_test3()
    insert_test4()
    insert_test5()
    insert_test6()
    insert_test7()
    insert_test8()
    insert_test9()
    insert_test10()
    insert_test11()
    insert_test12()
    insert_test13()
    insert_test14()
    insert_test15()
    insert_test16()
    insert_test17()
    insert_test18()
    insert_test19()
    insert_test20()
    insert_test21()
    insert_test22()
