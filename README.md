# PyGSE

Python Generalized Symbolic Execution and Test Generator. PyGSE is a python module that
simbolically executes methods of classes and creates it's tests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Tested for python 3.8.1

Clone this repository to your local machine:
```
git clone https://github.com/JuanmaCopia/PyGSE
```

### Installing on Linux using python venv

Create virtual enviroment on the project folder:

```
cd PyGSE
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

## Running the tests

To run the tests:

```
python run_test.py
```

To see more information of the exploration paths like pruned paths or fully explored
and it's extructures run in verbose mode:

```
python run_test.py -v
```

All tests should pass and no exceptions should be raised. Generated test are saved
in each structure folder under the tests/ directory.
For example you can finde the swap_node method tests of class LinkedList on:
```PyGSE/tests/linkedlist/ll_swap_node_test.py ``` The tests are generated from the file ```ll_instrumented.py``` but when you run them they will test the original file: ```ll.py```
The other test behave in the same way.


### Test Example

Let's take the swap_node example of above, a successful execution looks like this:

```
 ========================  PyGSE  =====================

Method swap_node of class LinkedList

Performing Exploration...

#1: OK
#2: OK
#3: PRUNED
#4: PRUNED
#5: OK
#6: OK
#7: PRUNED
#8: OK

DONE! 5 Tests were generated

Exploration Statistiscs:

  5 of 8 paths explored
  5 passed
  0 failed
  3 pruned:
    0 by depth
    0 by error
    0 by invalid
    0 by rec limit
    3 by repok
    0 by exception

Running generated tests...

Test1: OK
Test2: OK
Test3: OK
Test4: OK
Test5: OK
```

Let's see each part separately. The first part represents each path explored and it's
status, that could be OK, FAIL, or PRUNED. Each OK path will result in a writen test.

```
Performing Exploration...

#1: OK
#2: OK
#3: PRUNED
#4: PRUNED
#5: OK
#6: OK
#7: PRUNED
#8: OK

DONE! 5 Tests were generated
```

The second part are the statistics of all program paths exploration:

```
Exploration Statistiscs:

  5 of 8 paths explored
  5 passed
  0 failed
  3 pruned:
    0 by depth
    0 by error
    0 by invalid
    0 by rec limit
    3 by repok
    0 by exception
```

And the final section are the actual execution of the generated tests an it's outputs:

```
Running generated tests...

Test1: OK
Test2: OK
Test3: OK
Test4: OK
Test5: OK
```

A generated test will look like this:

```
def swap_node_test1():
    '''
    Self:
         node0(1) -> node1(0) -> node2(0) -> None
    Return:
         node1(0) -> node0(1) -> node2(0) -> None
    End Self:
         node1(0) -> node0(1) -> node2(0) -> None
    '''
    # Self Generation
    linkedlist0 = LinkedList()
    node0 = Node(1)
    node0.elem = 1
    node1 = Node(0)
    node1.elem = 0
    node2 = Node(0)
    node2.elem = 0
    node2.next = None
    node1.next = node2
    node0.next = node1
    linkedlist0.head = node0
    # Repok check
    assert linkedlist0.repok()
    # Method call
    returnv = linkedlist0.swap_node()
    # Assertions
    assert returnv.elem == 0
    assert returnv.next.elem == 1
    assert returnv.next.next.elem == 0
    assert returnv.next.next.next is None
    # Repok check
    assert linkedlist0.repok()
    assert linkedlist0.head.elem == 0
    assert linkedlist0.head.next.elem == 1
    assert linkedlist0.head.next.next.elem == 0
    assert linkedlist0.head.next.next.next is None
    print('Test1: OK')
```

And we can find all the tests on the file: ```/tests/linkedlist/ll_swap_node_test.py ```

## Running the program

To run the program for other files you can:

Execute it as a module:

```
python -m pygse <path-to-instrumented-module.py> <class-name> <method-name>
```

Or execute the main file:

```
python pygse/__main__.py <path-to-instrumented-module.py> <class-name> <method-name>
```

Test generated would be on the same folder of the file.py ins a file callled:

```
<module-name>_<method_name>_tests.py
```

For example to run the program on the swap_node method of LinkedList:

```
python -m pygse tests/linkedlist/ll_instrumented.py LinkedList swap_node
```

Test generated at:

```
tests/linkedlist/ll_swap_node_tests.py
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

