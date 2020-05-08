import subprocess
import sys
from optparse import OptionParser

parser = OptionParser("usage: %prog [options]")
parser.add_option(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    default=False,
    help="Show statsistics of executions",
)
parser.add_option(
    "-f",
    "--fail",
    dest="fail",
    action="store_true",
    default=False,
    help="Run fail tests",
)
parser.add_option(
    "--coverage",
    dest="coverage",
    action="store_true",
    default=False,
    help="Measure code coverage of generated test",
)
parser.add_option(
    "--mutation",
    dest="mutation",
    action="store_true",
    default=False,
    help="Measure mutation score",
)
parser.add_option(
    "-q",
    "--quiet",
    dest="quiet",
    action="store_true",
    default=False,
    help="Measure mutation score",
)

(options, args) = parser.parse_args()

coverage = options.coverage
mutation = options.mutation
verbose = options.verbose
quiet = options.quiet
run_fail_tests = options.fail


def execute(
    filepath,
    class_name,
    methods,
    max_r_nodes=2,
    max_nodes=5,
    m_timeout=2,
    b_timeout=5,
    max_depth=10,
):
    params = [
        sys.executable,
        "pyseat/__main__.py",
        filepath,
        class_name,
        "-m",
        methods,
        "-r " + str(max_r_nodes),
        "-n " + str(max_nodes),
        "-b " + str(b_timeout),
        "-t " + str(m_timeout),
        "-d " + str(max_depth),
        "--test-comments",
    ]
    if verbose:
        params.append("-v")
    if mutation:
        params.append("--mutation")
    if coverage:
        params.append("--coverage")
    if quiet:
        params.append("-q")
    subprocess.call(params)


if not run_fail_tests:
    # Linked List
    execute(
        filepath="tests/linkedlist/ll.py",
        class_name="LinkedList",
        methods="swap_node",
        max_r_nodes=0,
    )
    # Linked List No Repok
    execute(
        filepath="tests/linkedlist/llnr.py",
        class_name="LinkedList",
        methods="swap_node",
        max_r_nodes=0,
    )
    # Doubly Linked List
    execute(
        filepath="tests/doublylinkedlist/dll.py",
        class_name="DoublyLinkedList",
        methods="insert_after,remove,find,insert_at_back,insert_at_front,top_front,top_back,pop_front,pop_back",
        max_r_nodes=0,
    )
    # Circular Doubly Linked List
    execute(
        filepath="tests/circulardoublylinkedlist/cdll.py",
        class_name="CDLinkedList",
        methods="insert_after,insert_before,delete,append,prepend",
        max_r_nodes=0,
    )
    # Binary Search Tree
    execute(
        filepath="tests/bst/bst.py",
        class_name="BST",
        methods="insert,find,height",
        max_r_nodes=0,
        max_nodes=3,
    )
    # AVL
    execute(
        filepath="tests/avl/avl.py",
        class_name="AVL",
        methods="insert,delete,find_min,next_larger",
        max_r_nodes=0,
        max_nodes=2,
    )
else:
    # Bugged Doubly Linked List
    execute(
        filepath="tests/should_fail/doublylinkedlist/dll_bugged.py",
        class_name="DoublyLinkedList",
        methods="insert_after,find,insert_at_front,insert_at_back,pop_front,pop_back",
        max_r_nodes=0,
    )
