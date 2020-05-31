from llnr import *
import pytest


def test_swap_node1():
    '''
    Self:
        EmptyList
    Return:
        None
    End Self:
        EmptyList
    '''
    # Input Creation
    linkedlist0 = LinkedList()
    linkedlist0.head = None
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Repok check
    assert linkedlist0.repok()
    # Assertions
    assert returnv is None
    assert linkedlist0.head is None


