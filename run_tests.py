import subprocess
import sys


# verbose = False
# if len(sys.argv) > 1:
#     if sys.argv[1] == "-v":
#         verbose = True
#     else:
#         print("usage1: run_tests.py")
#         print("usage2: run_tests.py -v (Display execution information)")
#         sys.exit(-1)


# def execute(filepath, cls, method, verb, max_nodes=5, max_r_nodes=2, max_depth=10):
#     if verb:
#         subprocess.call(
#             [
#                 sys.executable,
#                 "pygse/__main__.py",
#                 "-v",
#                 "-d " + str(max_depth),
#                 "-n " + str(max_nodes),
#                 "-r " + str(max_r_nodes),
#                 "-c",
#                 filepath,
#                 cls,
#                 method,
#             ]
#         )
#     else:
#         subprocess.call(
#             [
#                 sys.executable,
#                 "pygse/__main__.py",
#                 "-d " + str(max_depth),
#                 "-n " + str(max_nodes),
#                 "-r " + str(max_r_nodes),
#                 "-c",
#                 filepath,
#                 cls,
#                 method,
#             ]
#         )


# execute("tests/linkedlist/ll.py", "LinkedList", "swap_node", verbose, 5, 0)
# execute("tests/linkedlist/llnr.py", "LinkedList", "swap_node", verbose, 5, 0)
# execute(
#     "tests/doublylinkedlist/dll.py", "DoublyLinkedList", "insert_after", verbose, 5, 0,
# )
# execute(
#     "tests/circulardoublylinkedlist/cdll.py",
#     "CDLinkedList",
#     "insert_after_node",
#     verbose,
#     5,
#     0,
# )
# execute("tests/bst/bst.py", "BST", "insert", verbose, 3, 0)
# execute("tests/avl/avl.py", "AVL", "insert", verbose, 2, 0)

# Linked List
subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "-d 10",
        "-n 5",
        "-r 0",
        "-c",
        "tests/linkedlist/ll.py",
        "LinkedList",
        "-m",
        "swap_node",
    ]
)

# Linked List No Repok
subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "-d 10",
        "-n 5",
        "-r 0",
        "-c",
        "tests/linkedlist/llnr.py",
        "LinkedList",
        "-m",
        "swap_node",
    ]
)
# Doubly Linked List
subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "-d 10",
        "-n 5",
        "-r 0",
        "-c",
        "tests/doublylinkedlist/dll.py",
        "DoublyLinkedList",
        "-m",
        "insert_after,remove,find,insert_at_back,insert_at_front,top_front,top_back",
    ]
)
# Circular Doubly Linked List
subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "-d 10",
        "-n 5",
        "-r 0",
        "-c",
        "tests/circulardoublylinkedlist/cdll.py",
        "CDLinkedList",
        "-m",
        "insert_after,insert_before,delete",
    ]
)
# Binary Search Tree
subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "-d 10",
        "-n 3",
        "-r 0",
        "-c",
        "tests/bst/bst.py",
        "BST",
        "-m",
        "insert,find",
    ]
)
# AVL
subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "-d 10",
        "-n 2",
        "-r 0",
        "-c",
        "tests/avl/avl.py",
        "AVL",
        "-m",
        "insert,delete",
    ]
)
