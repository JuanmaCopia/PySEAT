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


def execute(filepath, class_name, method_name, verbose, max_depth=10):
    if verbose:
        subprocess.call(
            [
                sys.executable,
                "pygse/__main__.py",
                "-v",
                "-d" + str(max_depth),
                filepath,
                class_name,
                method_name,
            ]
        )
    else:
        subprocess.call(
            [
                sys.executable,
                "pygse/__main__.py",
                "-d" + str(max_depth),
                filepath,
                class_name,
                method_name,
            ]
        )


execute("tests/linkedlist/ll_instrumented.py", "LinkedList", "swap_node", verbose)
execute("tests/linkedlist/llnr_instrumented.py", "LinkedList", "swap_node", verbose)
execute(
    "tests/doublylinkedlist/dll_instrumented.py",
    "DoublyLinkedList",
    "insert_after",
    verbose,
)
execute(
    "tests/circulardoublylinkedlist/cdll_instrumented.py",
    "CDLinkedList",
    "insert_after_node",
    verbose,
)
execute("tests/bst/bst_instrumented.py", "BST", "insert", verbose, 8)
execute("tests/avl/avl_instrumented.py", "AVL", "insert", verbose, 8)
