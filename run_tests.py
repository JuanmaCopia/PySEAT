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


def execute(filepath, cls, method, verb, max_nodes=5, max_r_nodes=2, max_depth=10):
    if verb:
        subprocess.call(
            [
                sys.executable,
                "pygse/__main__.py",
                "-v",
                "-d " + str(max_depth),
                "-n " + str(max_nodes),
                "-r " + str(max_r_nodes),
                filepath,
                cls,
                method,
            ]
        )
    else:
        subprocess.call(
            [
                sys.executable,
                "pygse/__main__.py",
                "-d " + str(max_depth),
                "-n " + str(max_nodes),
                "-r " + str(max_r_nodes),
                filepath,
                cls,
                method,
            ]
        )


execute("tests/linkedlist/ll_instrumented.py", "LinkedList", "swap_node", verbose, 5, 0)
execute(
    "tests/linkedlist/llnr_instrumented.py", "LinkedList", "swap_node", verbose, 5, 0
)
execute(
    "tests/doublylinkedlist/dll_instrumented.py",
    "DoublyLinkedList",
    "insert_after",
    verbose,
    5,
    0,
)
execute(
    "tests/circulardoublylinkedlist/cdll_instrumented.py",
    "CDLinkedList",
    "insert_after_node",
    verbose,
    5,
    0,
)
execute("tests/bst/bst_instrumented.py", "BST", "insert", verbose, 3, 0)
execute("tests/avl/avl_instrumented.py", "AVL", "insert", verbose, 2, 0)
