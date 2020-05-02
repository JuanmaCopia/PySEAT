import subprocess
import sys


verbose = False
if len(sys.argv) > 1:
    if sys.argv[1] == "-v":
        verbose = True
    else:
        print("usage1: run_tests.py")
        print("usage2: run_tests.py -v (Display execution information)")
        sys.exit(-1)


def execute(
    filepath,
    class_name,
    methods,
    max_r_nodes=2,
    max_nodes=5,
    timeout=5,
    max_depth=10,
    verbose=False,
):
    if verbose:
        subprocess.call(
            [
                sys.executable,
                "pygse/__main__.py",
                filepath,
                class_name,
                "-m",
                methods,
                "-r " + str(max_r_nodes),
                "-n " + str(max_nodes),
                "-t " + str(timeout),
                "-d " + str(max_depth),
                "--complete",
                "-v",
            ]
        )
    else:
        subprocess.call(
            [
                sys.executable,
                "pygse/__main__.py",
                filepath,
                class_name,
                "-m",
                methods,
                "-r " + str(max_r_nodes),
                "-n " + str(max_nodes),
                "-t " + str(timeout),
                "-d " + str(max_depth),
                "--complete",
            ]
        )


# Linked List
execute(
    filepath="tests/linkedlist/ll.py",
    class_name="LinkedList",
    methods="swap_node",
    max_r_nodes=0,
    verbose=verbose,
)
# Linked List No Repok
execute(
    filepath="tests/linkedlist/llnr.py",
    class_name="LinkedList",
    methods="swap_node",
    max_r_nodes=0,
    verbose=verbose,
)
# Doubly Linked List
execute(
    filepath="tests/doublylinkedlist/dll.py",
    class_name="DoublyLinkedList",
    methods="insert_after,remove,find,insert_at_back,insert_at_front,top_front,top_back,pop_front,pop_back",
    max_r_nodes=0,
    verbose=verbose,
)
# Circular Doubly Linked List
execute(
    filepath="tests/circulardoublylinkedlist/cdll.py",
    class_name="CDLinkedList",
    methods="insert_after,insert_before,delete,append,prepend",
    max_r_nodes=0,
    verbose=verbose,
)
# Binary Search Tree
execute(
    filepath="tests/bst/bst.py",
    class_name="BST",
    methods="insert,find,height",
    max_r_nodes=0,
    max_nodes=3,
    verbose=verbose,
)
# AVL
execute(
    filepath="tests/avl/avl.py",
    class_name="AVL",
    methods="insert,delete,find_min,next_larger",
    max_r_nodes=0,
    max_nodes=2,
    verbose=verbose,
)
