# PySEAT

Python Generalized Symbolic Execution and Test Generator. PySEAT is a python module that
simbolically executes methods of classes and creates it's tests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Tested for python 3.8.1

Clone this repository to your local machine:
```
git clone https://github.com/JuanmaCopia/PySEAT
```

### Installing on Linux using python venv

Create virtual enviroment on the project folder:

```
cd PySEAT/
python3 -m venv env
```

Activate the enviroment:

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
  -v, --verbose  Show statsistics of executions
  -f, --fail     Run fail tests
  --coverage     Measure code coverage of the generated test suite
  --mutation     Measure mutation score of the generated test suite
  -q, --quiet    Run test in quiet mode (less console output)
```

Generated test are saved in each structure folder under the ```tests/``` directory.
For example you can find the LinkedList test on:
```PySEAT/tests/linkedlist/test_ll.py ``` The tests are generated from the file ```ll.py```


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

Each valid execution is an execution that was'nt pruned. Pruned executions are
mostly due to generated inputs that not satisfied the repok method (we will see what
a repok method is later).

As we can see, there are four possibles states of an execution:

PRUNED or invalid executions. No were generated for this executions.
OK: No errors were found. The test is generated.
FAIL: An error was found. The test that produces the error is generated
EXCEPTION: An exception was raised. the test that produces the exception is generated.
TIMEOUT: The execution exeeded the time. The test that produces the timeout is generated.

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
and helps to see what is the input, the return value, and the final state of
the self. We can avoid the generation of this comment by adding ```--no-comments```
when running the module but for the run_test.py is always generated.

After the exploration, te program will call pytest to run the generated test suit
and the test report will be shown:

```
Running generated tests...
..........F..F..F.F.F.F.F...FF..F.....F.                                 [100%]
=================================== FAILURES ===================================
          --- Failures description here ---
```

## Running the program

To run the program for other files you can:
```
python <path-to pyseat/__main__.py> <path-module-to-test.py> <class-name> -m <methods-names>
```

Test generated would be on the same folder of the file.py ins a file called:
```
test_<module-to.test_name>.py
```

We can measure the branch coverage of our test suite by adding ```--coverage```
parameter. An HTML report will be generated on the same folder as the code in
```htmlcov/index.html``` and a report will be shown on console.

We can also measure the mutation score of our test suite using ```mutpy``` by adding ```--mutation```
parameter. An HTML report will be generated on the same folder as the code in
```mutscore/index.html``` and a report witll be shown on console.

Another usefull parameters:

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
  -v, --verbose         Show statsistics of executions
  --no-comments         Generate comments on test with the structure
                        representation
  --coverage            Measure code coverage of generated test
  --mutation            Measure mutation score
  -q, --quiet           Measure mutation score
  --no-test-run         Run generated test after the exploration
```

## Instrumentation

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

