import subprocess
import sys


ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/linkedlist/ll_instrumented.py",
        "LinkedList",
        "swap_node",
    ]
)

ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/linkedlist/llnr_instrumented.py",
        "LinkedList",
        "swap_node",
    ]
)

ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/doublylinkedlist/dll_instrumented.py",
        "DoublyLinkedList",
        "insert_after",
    ]
)

ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/circulardoublylinkedlist/cdll_instrumented.py",
        "CDLinkedList",
        "insert_after_node",
    ]
)
