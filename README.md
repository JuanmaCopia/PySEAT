# PySEAT

Python Symbolic Execution and Automatic Tester. PySEAT is a python module which automates
test case generation of complex structures (e.g., Binary Search Trees or AVLs) using symbolic execution with lazy initialization.

This project reuse part of the smt interface with the Z3 theorem prover of an existing python symbolic execution engine called [PEF: Python Error Finder](https://reader.elsevier.com/reader/sd/pii/S1571066118300471?token=FB4433EA85BB1AA956108AB28C94F659FFB4CED02141D87A019D533BEDCF7538C0C78574841E5B3BB27323DBE11E6B9B)

Based on the papers:

[Generalized Symbolic Execution for Model Checking and Testing](http://users.ece.utexas.edu/~khurshid/testera/GSE.pdf)

[Test Input Generation with Java PathFinder](http://users.ece.utexas.edu/~khurshid/papers/JPF-issta04.pdf)

[A Peer Architecture for Lightweight Symbolic Execution](http://hoheinzollern.files.wordpress.com/2008/04/seer1.pdf)


## Getting Started

### Prerequisites
Tested for python 3.8.1

Clone this repository to your local machine:
```
git clone https://github.com/JuanmaCopia/PySEAT
```

### Installing on Linux using python venv

Create virtual environment on the project folder:
```
cd PySEAT/
python3 -m venv env
```

Activate the environment:
```
source env/bin/activate
```

Install the requirements:
```
sudo pip install -r requirements
```

Done! If everything went well you are ready to use it.

## Running the tests examples

To run the tests examples (all tests should pass):
```
python run_tests.py
```

Another useful arguments for ```run_test.py```:
```
Options:
  -h, --help     show this help message and exit
  -v, --verbose  Show statistics of executions
  -f, --fail     Run fail tests
  --coverage     Measure code coverage of the generated test suite
  --mutation     Measure mutation score of the generated test suite
  -q, --quiet    Run test in quiet mode (less console output)
```

Generated test are saved in each structure folder under the ```tests/``` directory.
For example you can find the LinkedList test on: ```PySEAT/tests/doublylinkedlist/test_dll.py ```This tests are generated from the file ```dll.py```


### Test Example

Now we are going to run the example of a Double Linked List with bugs that resides on ```test/should_fail/```.
We can run it through run_test.py script by adding ```-f``` option
```
python run_tests.py -f
```

Or inside the PySEAT folder, directly calling the module:
```
python -m pyseat test/should_fail/dll_bugged.py DoublyLinkedList -m "insert_after,find,insert_at_front,insert_at_back,pop_front,pop_back"
```

So let's run the next command adding also a ```-q``` option to run it in quiet mode:
```
python run_tests.py -f -q
```

The program output for the first three method looks like this:
```
 Method: insert_after
 Class:  DoublyLinkedList

 Performing Exploration...
   #1 OK
   #7 OK
   #13 OK
   #18 OK
   #19 OK
   #24 OK
   #28 OK
   #29 OK
   #33 OK
   #36 OK
   #37 TIMEOUT
   #40 OK
   #42 OK
   #43 TIMEOUT
   #46 OK
   #48 OK

 Done! 16 Tests were generated

 Valid executions: 16 of 48
   14 passed
   0 failed
   0 exceptions
   2 timeouts
   32 pruned

 ------------------------------ 15.52 seconds ------------------------------


 Method: find
 Class:  DoublyLinkedList

 Performing Exploration...
   #1 EXCEPTION
   #7 OK
   #8 EXCEPTION
   #13 OK
   #14 EXCEPTION
   #18 OK
   #19 EXCEPTION
   #22 OK
   #23 EXCEPTION
   #25 OK
   #26 OK

 Done! 11 Tests were generated

 Valid executions: 11 of 26
   6 passed
   0 failed
   5 exceptions
   0 timeouts
   15 pruned

 ------------------------------ 6.81 seconds ------------------------------


 Method: insert_at_front
 Class:  DoublyLinkedList

 Performing Exploration...
   #1 OK
   #2 FAIL

 Done! 2 Tests were generated

 Valid executions: 2 of 2
   1 passed
   1 failed
   0 exceptions
   0 timeouts
   0 pruned

 ------------------------------ 0.06 seconds ------------------------------
```

Each valid execution is an execution that wasn't pruned. Pruned executions are
mostly due to generated inputs that not satisfied the repok method (we will see what
a repok method is later).

As we can see, there are five possibles states of an execution:

* PRUNED or invalid executions. No were generated for this executions.
* OK: No errors were found. The test is generated.
* FAIL: An error was found. The test that produces the error is generated
* EXCEPTION: An exception was raised. the test that produces the exception is generated.
* TIMEOUT: The execution exceeded the time. The test that produces the timeout is generated.

A generated test look like this:
```
def test_insert_after8():
    '''
    Self:
        None <- 1 ->  <- 1 ->  <- 0 -> None
    Return:
        None
    End Self:
        None <- 1 ->  <- 1 ->  <- 0 ->  <- 0 -> None
    '''
    # Input Creation
    doublylinkedlist0 = DoublyLinkedList()
    node1 = Node(0)
    node1.data = 1
    node1.prev = None
    node2 = Node(0)
    node2.data = 1
    node3 = Node(0)
    node3.data = 0
    node3.next = None
    node3.prev = node2
    node2.next = node3
    node2.prev = node1
    node1.next = node2
    doublylinkedlist0.head = node1
    doublylinkedlist0.tail = node3
    # Repok check
    assert doublylinkedlist0.repok()
    # Method call
    returnv = doublylinkedlist0.insert_after(0, 0)
    # Repok check
    assert doublylinkedlist0.repok()
    # Assertions
    assert returnv is None
    assert doublylinkedlist0.head.data == 1
    assert doublylinkedlist0.head.prev is None
    assert doublylinkedlist0.tail.data == 0
    assert doublylinkedlist0.tail.next is None
    assert doublylinkedlist0.head.next.data == 1
    assert doublylinkedlist0.tail.prev.data == 0
```

And we can find all the tests on the same folder of our source code.
In this case: ```/tests/should_fail/test_dll_bugged.py ```

The test comment is created calling to the ```__repr__``` method of the class
and helps to see what the input, the return value, and the final state of
the self are. We can avoid the generation of this comment by adding ```--no-comments```
when running the module but for the run_test.py they are always generated.

After the exploration, te program will call pytest to run the generated test suit
and the test report will be shown:
```
Running generated tests...
..........F..F..F.F.F.F.F...FF..F.....F.                                 [100%]
=================================== FAILURES ===================================
          --- Failures description here ---
```

## How it works

PySEAT tries to explore every possibility of the method under test. i.e. executes
the method with every possible input valid state. This is accomplished by the
use of lazy initialization to get every structural possibility, and by taking
all possible path conditions (i.e. for every condition found, the program takes
the two possibilities, True and False, if possible).

### Lazy Initialization:

Every execution of the program starts with an input with uninitialized fields, whenever
a field is accessed it is initialized as follows:
If it is a reference field (e.g. user-defined class) the possibilities to initialize are:

* A new instance.
* None.
* A previously created instance.

As you can see, due to the third initialization option, cyclic structures are created.

So lazy initialization would explore all structural possibilities but also create invalid
structures (e.g if we are executing over SinglyLinkedList it might create cyclic lists).
That is why we need a repok method that allows us to get rid of those and avoid useless
programs executions.

### Repok method:

It's a bound method of the class under test that implements the invariant of the class, that
is to say, analyze the self structure and returns True if it is a valid structure and False
otherwise. It allow us to prune invalid executions.

For a deeper understanding of lazy initialization: [Generalized Symbolic Execution for Model Checking and Testing](http://users.ece.utexas.edu/~khurshid/testera/GSE.pdf)

## Instrumentation

Two things are required by PySEAT to work:

1. Annotated types.
2. A repok method for the class (class invariant).

In order to perform symbolic execution, the target method should have the types annotated with python annotations. Also, all the classes involved in that method execution should have it's __init__ method arguments and instance attributes annotated.

Also, a repok method is needed to prune invalid executions. On every initialization, the program will check
the repok method for the self class and for the initialized class.

### Instrumentation example

Let's an example of instrumentation of a DoublyLinkedList and its "insert_after" method that
inserts a new node with a certain key after another certain key on the doubly
linked list.

```
class Node:
    # Instance attributes annotations (will be treated as symbolic)
    data: int
    next: "Node"
    prev: "Node"

    # Init params should be annotated also
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Instance attributes annotations (will be treated as symbolic)
    head: "Node"
    tail: "Node"

    # Init params should be also annotated
    def __init__(self):    # You can omit the self annotation
        self.head = None
        self.tail = None

    # Each method's parameter should be annotated
    def insert_after(self, key: int, value: int):   # You can omit the self annotation
        node = Node(value)

        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next

        if curr is None:
            print("Key not found")
            return

        if curr.next is None:
            curr.next = node
            node.prev = curr
            self.tail = node
        else:
            next_node = curr.next
            curr.next = node
            node.prev = curr
            node.next = next_node
            next_node.prev = node

    @staticmethod
    def do_add(s, x):
        length = len(s)
        s.add(x)
        return len(s) != length

    # A repok method should be supplied.
    # returns True if the structure is a valid DoublyLinkedList, False otherwise.
    def repok(self):
        if self.head is None and self.tail is None:
            return True
        if self.head is None or self.tail is None:
            return False
        if self.head.prev is not None or self.tail.next is not None:
            return False

        visited = set()
        visited.add(self.head)

        current = self.head
        next_node = current.next

        while next_node:
            if next_node.prev is not current:
                return False
            if not self.do_add(visited, next_node):
                return False
            current = next_node
            next_node = next_node.next

        if self.do_add(visited, self.tail):
            return False
        return True
```

With this instrumentation, the method "insert_after" can be successfully explored and test will be generated.
If inside of the method there were other function calls, there is no need to annotate them.

As you see, the repok method checks that the structure is acyclic. This is a very important property to check
if you don't want this kind of structures. In other cases you will need to check aciclicity for some attributes
only, for example for a Binary Tree which each node has a parent reference, aciclicty should only be checked for
right and left child's but not for the parent.


## Currently supported symbolic types:
  * int
  * bool

Currently, PySEAT is supporting test generation only for bound methods of classes
that takes as argument structures of the type of the "self" (i.e. the user defined structure) and also the types in and bool. Other complex structures apart from self
and other builtin data types are not supported yet.

## Running the program

To run the program for other files you can:
```
python <path-to pyseat/__main__.py> <path-module-to-test.py> <class-name> -m <methods-names>
```

Test generated would be on the same folder of the module under test, on a file called:
```
test_<module-to.test_name>.py
```

We can measure the branch coverage of our test suite by adding ```--coverage```
parameter. An HTML report will be generated on the same folder as the code in
```htmlcov/index.html``` and a report will be shown on console.

We can also measure the mutation score of our test suite using ```mutpy``` by adding ```--mutation```
parameter. An HTML report will be generated on the same folder as the code in
```mutscore/index.html``` and a report will be shown on console.

Another useful parameters:
```
Usage: __main__.py <path to *.py file> <class-name> -m <method1> [,<method2>] [options]

Options:
  -h, --help            show this help message and exit
  -m METHODS_NAMES, --methods=METHODS_NAMES
                        Methods to explore and generate tests
  -d MAX_DEPTH, --max-depth=MAX_DEPTH
                        Maximum exploration tree depth
  -n MAX_NODES, --max-nodes=MAX_NODES
                        Maximum amount of nodes per structure
  -r MAX_R_NODES        Max nodes that repok can add
  -b BUILD_TIMEOUT, --build-timeout=BUILD_TIMEOUT
                        Max time to build a structure
  -t METHOD_TIMEOUT, --method-timeout=METHOD_TIMEOUT
                        Max execution time for each exploration
  -v, --verbose         Show statistics of executions
  --no-comments         Generate comments on test with the structure
                        representation
  --coverage            Measure code coverage of generated test
  --mutation            Measure mutation score
  -q, --quiet           Measure mutation score
  --no-test-run         Run generated test after the exploration
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

