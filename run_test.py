import subprocess
import sys


ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/ll_instrumented.py",
        "LinkedList",
        "swap_node",
    ]
)

ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/llnr_instrumented.py",
        "LinkedList",
        "swap_node",
    ]
)

ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/dll_instrumented.py",
        "DoublyLinkedList",
        "insert_after",
    ]
)

ret = subprocess.call(
    [
        sys.executable,
        "pygse/__main__.py",
        "tests/cdll_instrumented.py",
        "CDLinkedList",
        "insert_after_node",
    ]
)
