# PySEAT

Python Symbolic Execution and Automated Tester. PySEAT is a python module which automates
test case generation for programs manipulating complex structures (e.g., Binary Search Trees or AVLs) using symbolic execution with lazy initialization.

This project reuses part of the interface with the Z3 SMT solver of an existing python symbolic execution engine called [PEF: Python Error Finder](https://reader.elsevier.com/reader/sd/pii/S1571066118300471?token=FB4433EA85BB1AA956108AB28C94F659FFB4CED02141D87A019D533BEDCF7538C0C78574841E5B3BB27323DBE11E6B9B)

This tool is based on the following papers:

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

Done! If everything went well you are ready to use the tool.

## Running the tests examples

To run the test examples (all tests should pass):
```
python run_tests.py
```

Generated tests are saved, for each structure, into a folder under the ```tests/``` directory.
For example you can find the LinkedList tests on: ```PySEAT/tests/doublylinkedlist/test_dll.py ```These tests are generated from the file ```dll.py```

### Test Example

Let us run the tool on an implementation of Doubly Linked Lists (with bugs), that resides on ```test/should_fail/```.

We can run it using the run_test.py script, by simply adding the ```-f``` option:
```
python run_tests.py -f
```

The program output looks as follows:
```
 Generating instances of DoublyLinkedList...
 Done!

 Exploring insert_after...

   #1 OK
   #2 OK
   #3 OK
   #4 OK
   #5 OK
   #6 OK
   #7 OK
   #8 OK
   #9 OK
   #10 OK
   #11 OK
   #12 OK
   #13 OK
   #14 OK
   #15 OK
   #16 OK
   #17 TIMEOUT
   #18 TIMEOUT
   #19 OK
   #20 OK
   #21 OK

 Exploring find...

   #1 EXCEPTION
   #2 OK
   #3 OK
   #4 OK
   #5 OK
   #6 OK
   #7 EXCEPTION
   #8 OK
   #9 OK
   #10 OK
   #11 OK
   #12 EXCEPTION
   #13 OK
   #14 OK
   #15 OK
   #16 EXCEPTION
   #17 OK
   #18 OK
   #19 EXCEPTION
   #20 OK
   #21 OK

 Exploring insert_at_front...

   #1 OK
   #2 OK
   #3 OK
   #4 OK
   #5 OK
   #6 FAIL

 Exploring insert_at_back...

   #1 FAIL
   #2 FAIL
   #3 FAIL
   #4 FAIL
   #5 OK
   #6 OK

 Exploring pop_front...

   #1 FAIL
   #2 FAIL
   #3 FAIL
   #4 FAIL
   #5 OK
   #6 OK

 Exploring pop_back...

   #1 OK
   #2 OK
   #3 OK
   #4 OK
   #5 FAIL
   #6 OK

------------------ 66 Tests generated in 10.71s ------------------

 49 passed
 10 failed
 5 exceptions
 2 timeouts

 Build time: 0.02s
 File: /home/juan/Documents/PySEAT/tests/should_fail/doublylinkedlist/test_dll_bugged.py

-----------------------------------------------------------------
```
As seen above, there are four possible states of an execution:

* OK: No errors were found. The test is generated.
* FAIL: An error was found. The test that produces the error is generated
* EXCEPTION: An exception was raised. the test that produces the exception is generated.
* TIMEOUT: The execution exceeded the allotted time. The test that produces the timeout is generated.

A generated test looks as follows:
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
and helps to see what the input, the return value, and the final state of self are. We can avoid the generation of this comment through specific arguments
when running the module or by setting the argument in the config file as false (later on
we will see how the config file works).

After the exploration, the program will call pytest to run the generated test suite
and the test report will be shown:
```
Running generated tests...
..........F..F..F.F.F.F.F...FF..F.....F.                                 [100%]
=================================== FAILURES ===================================
          --- Failures description here ---
```

## How the tool works

PySEAT uses the repok() method to generate all partially symbolic valid structures (with a limit in the amount of nodes). After, It performs symbolic execution on each method under test
with these structures, exploring every program path and generating the corresponding test case that exercises that path.

### Repok method:

Captures the representation invariant of the datatype. That is, it takes an instance of the structure, and checks that the assumed representation holds, returning true in such a case, and false if the representation invariant is broken. This method will be called to check whether a partially symbolic structure would satisfy the representation invariant, pruning the cases where this invariant does not hold.
For a deeper understanding of lazy initialization: [Generalized Symbolic Execution for Model Checking and Testing](http://users.ece.utexas.edu/~khurshid/testera/GSE.pdf)

## Instrumentation

Two things are required by PySEAT to work:

1. Annotated types.
2. A repok method for the class (class invariant).

In order to perform symbolic execution, the target method should have the types annotated with python annotations. Also, all the classes involved in that method execution should have its __init__ method arguments and instance attributes annotated.

A method called "repok" is needed to generate the inputs.

### Instrumentation example

Let us see an instrumentation example of a DoublyLinkedList and its "insert_after" method that inserts a new node, with a certain key, after a given key on the doubly
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
    def insert_after(self, key: int, value: int):   # Self annotation can be omitted
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

With this instrumentation, the method "insert_after" can be successfully explored and tests will be generated.
If inside of the method there were other function calls, there is no need to annotate them.

As it can be seen, the repok method checks that the structure is acyclic. This is a very important property to check
if this is an assumption on the structured, as a precondition of the analyzed method. The repok is specific to each datatype. Acyclicity may be a constraint in some cases, and not in other, or sometimes a requirement only on certain fields (e.g., acyclicity in trees with respect to left and right, but not parent).

## Currently supported symbolic types:
  * int
  * bool

Currently, PySEAT supports test generation only for instance methods that take as arguments the "self" (i.e. the user defined structure) as well as types int and bool. Other complex structures apart from self and other builtin data types are not supported yet.

## Running the program

### The configuration file:

The easiest way to run the program is modifying the default configuration file on
```PySEAT/config.ini``` or creating a new configuration file and pass its path
as argument to the program.

The configuration file looks as follows:
```
[DEFAULT]
max_nodes = 5
max_depth = 10
timeout = 5
coverage = false
mutation = false
quiet = false
run_tests = true
test_comments = false
```

To add a program run, the user has to add a new section, and provide the following arguments:
* filepath: The path to the module to test.
* class_name: The name of the class to test.
* methods: The methods of the class to explore

You can add as many runs as you want. For example, with the following config file, the program
will run for DoublyLinkedList and CDLinkedList. They are inside the ```/tests``` folder:
```
[DEFAULT]
max_nodes = 5
max_depth = 10
timeout = 2
coverage = false
mutation = false
quiet = false
run_tests = true
test_comments = true

[Doubly Linked List]
filepath = tests/doublylinkedlist/dll.py
class_name = DoublyLinkedList
methods = insert_after,remove,find,insert_at_back,insert_at_front,top_front,top_back,pop_front,pop_back

[Circular Doubly LinkedList]
filepath = tests/circulardoublylinkedlist/cdll.py
class_name = CDLinkedList
methods = insert_after,insert_before,delete,append,prepend
```

One can also override any of the defaults on each run:
```
[Circular Doubly LinkedList]
filepath = tests/circulardoublylinkedlist/cdll.py
class_name = CDLinkedList
methods = insert_after,insert_before,delete,append,prepend
max_nodes = 4
```

### Arguments:
```
; Required Arguments:
; filepath:       Path to module .py under test.
; class_name:     Name of the class that contains the methods to test.
; methods         Methods to test.

; Optional (has default values in DEFAULT section):
; max_nodes:       Max amount of nodes that can create the method exploration.
; max_depth:       Max depth of the exploration tree made by conditions evalutation.
; timeout:         Max time to execute method exloration.
; coverage:        Measure coverage of generated test suite.
; mutation:        Measure mutation score of generated test suite.
; quiet:           Quiet mode, less output
; run_tests:       Run test with pytest after generation.
; test_comments:   Make a comment with the structure representation on each test.
```

### How to run:

To instruct PySEAT to run and read the configuration file, add the -c option:
```
python <path-to pyseat/__main__.py> -c
```

Or provide a custom config.ini file:
```
python <path-to pyseat/__main__.py> -c <path-to .ini file>
```

One can also execute it as a module:
```
python -m pyseat -c
```

To run the program with command line arguments:
```
python <path-to pyseat/__main__.py> <path-module-to-test.py> <class-name> -m <methods-names>
```

Tests generated would be on the same folder of the module under test, on a file called:
```
test_<module-to.test_name>.py
```

All Arguments in config file can also be supplied via the command line:
```
python <path-to pyseat/__main__.py> -h
```

## Coverage measurement and mutation score

You can measure the coverage and the mutation score of the generated test suite by the arguments coverage and mutation respectively.
A command line report will be shown and a html-report will be be created on the same
folder as the source file. For coverage ```source-folder/htmlcov/index.html```. For mutation ```source-folder/mutscore/index.html```.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details