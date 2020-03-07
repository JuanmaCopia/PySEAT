# AVL Binary search tree implementation in Python
# Author: AlgorithmTutor

# data structure that represents a node in the tree

import sys
import pygse.symbolic_execution_engine as see


class Node:
    # Instrumentations class attributes
    _vector = [None]
    _is_user_defined = True
    _id = 0

    def __init__(self, data: int):

        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0
        # Instrumentations instance attributes
        self._data_is_initialized = False
        self._parent_is_initialized = False
        self._left_is_initialized = False
        self._right_is_initialized = False
        self._bf_is_initialized = False

        self._concretized = False
        self._generated = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1

    # ========================== Instrumentation ============================ #
    def _get_parent(self):
        if not self._parent_is_initialized and self in self._vector:
            self._parent_is_initialized = True
            self.parent = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.parent

    def _set_parent(self, value):
        self.parent = value
        self._parent_is_initialized = True
        see.SEEngine.ignore_if(not self.conservative_repok(), self)

    def _get_left(self):
        if not self._left_is_initialized and self in self._vector:
            self._left_is_initialized = True
            self.left = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.left

    def _set_left(self, value):
        self.left = value
        self._left_is_initialized = True
        see.SEEngine.ignore_if(not self.conservative_repok(), self)

    def _get_right(self):
        if not self._right_is_initialized and self in self._vector:
            self._right_is_initialized = True
            self.right = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.right

    def _set_right(self, value):
        self.right = value
        self._right_is_initialized = True
        see.SEEngine.ignore_if(not self.conservative_repok(), self)

    def conservative_repok(self):
        return True

    def repok(self):
        return True


class AVLTree:
    # Instrumentations class attributes
    _vector = [None]
    _is_user_defined = True
    _id = 0

    def __init__(self, root: "Node" = None):
        self.root = None
        # Instrumentations instance attributes
        self._root_is_initialized = False

        self._concretized = False
        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._generated = False

    # ========================== Instrumentation ============================ #

    def _get_root(self):
        if not self._root_is_initialized and self in self._vector:
            self._root_is_initialized = True
            self.root = see.SEEngine.get_next_lazy_step(Node, Node._vector)
            see.SEEngine.save_lazy_step(Node)
            see.SEEngine.ignore_if(not self.conservative_repok(), self)
        return self.root

    def _set_root(self, value):
        self.root = value
        self._root_is_initialized = True
        see.SEEngine.ignore_if(not self.conservative_repok(), self)

    @staticmethod
    def do_add(s, x):
        length = len(s)
        s.add(x)
        return len(s) != length

    def repok(self):
        if not self.root:
            return True
        if self.root.parent is not None:
            return False
        if not (
            self.is_acyclic() and
            self.is_ordered() and
            self.is_balanced()
        ):
            return False
        return True

    def is_acyclic(self):
        visited = set()
        visited.add(self.root)
        worklist = []
        worklist.append(self.root)
        while worklist:
            current = worklist.pop(0)
            if current.left:
                if not AVLTree.do_add(visited, current.left):
                    return False
                worklist.append(current.left)
            if current.right:
                if not AVLTree.do_add(visited, current.right):
                    return False
                worklist.append(current.right)
        return True

    def is_ordered(self):
        return self.is_ordered2(self.root, None, None)

    def is_ordered2(self, node, min, max):
        if (
            (min is not None and node.data <= min) or
            (max is not None and node.data >= max)
        ):
            return False
        if node.left:
            if not self.is_ordered2(node.left, min, node.data):
                return False
        if node.right:
            if not self.is_ordered2(node.right, node.data, max):
                return False
        return True

    def is_balanced(self):
        queue = []
        queue.append(self.root)
        while queue:
            current = queue.pop(0)
            if current.bf > 1 or current.bf < -1:
                return False
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return True
    # ======================== instrumented repok ========================== #

    def instrumented_repok(self):
        if not self._get_root():
            return True
        if self._get_root()._get_parent() is not None:
            return False
        if not (
            self.instrumented_is_acyclic() and
            self.instrumented_is_ordered() and
            self.instrumented_is_balanced()
        ):
            return False
        return True

    def instrumented_is_acyclic(self):
        visited = set()
        visited.add(self._get_root())
        worklist = []
        worklist.append(self._get_root())
        while worklist:
            current = worklist.pop(0)
            if current._get_left():
                if not AVLTree.do_add(visited, current._get_left()):
                    return False
                worklist.append(current._get_left())
            if current._get_right():
                if not AVLTree.do_add(visited, current._get_right()):
                    return False
                worklist.append(current._get_right())
        return True

    def instrumented_is_ordered(self):
        return self.instrumented_is_ordered2(self._get_root(), None, None)

    def instrumented_is_ordered2(self, node, min, max):
        if (
            (min is not None and node.data <= min) or
            (max is not None and node.data >= max)
        ):
            return False
        if node._get_left():
            if not self.instrumented_is_ordered2(node._get_left(), min, node.data):
                return False
        if node._get_right():
            if not self.instrumented_is_ordered2(node._get_right(), node.data, max):
                return False
        return True

    def instrumented_is_balanced(self):
        queue = []
        queue.append(self._get_root())
        while queue:
            current = queue.pop(0)
            if current.bf > 1 or current.bf < -1:
                return False
            if current._get_left():
                queue.append(current._get_left())
            if current._get_right():
                queue.append(current._get_right())
        return True

    # ======================== conservative repok ========================== #

    def conservative_repok(self):
        if not self._root_is_initialized:
            return True
        if not self.root:
            return True
        if not self.root._parent_is_initialized:
            return True
        if self.root.parent is not None:
            return False
        if not (
            self.conservative_is_acyclic() and
            self.conservative_is_ordered() and
            self.conservative_is_balanced()
        ):
            return False
        return True

    def conservative_is_acyclic(self):
        visited = set()
        if not self._root_is_initialized:
            return True
        visited.add(self.root)
        worklist = []
        worklist.append(self.root)
        while worklist:
            current = worklist.pop(0)
            if not current._left_is_initialized:
                return True
            if current.left:
                if not AVLTree.do_add(visited, current.left):
                    return False
                worklist.append(current.left)
            if not current._right_is_initialized:
                return True
            if current.right:
                if not AVLTree.do_add(visited, current.right):
                    return False
                worklist.append(current.right)
        return True

    def conservative_is_ordered(self):
        if not self._root_is_initialized:
            return True
        return self.conservative_is_ordered2(self.root, None, None)

    def conservative_is_ordered2(self, node, min, max):
        if (
            (min is not None and node.data <= min) or
            (max is not None and node.data >= max)
        ):
            return False
        if not node._left_is_initialized:
            return True
        if node.left:
            if not self.conservative_is_ordered2(node.left, min, node.data):
                return False
        if not node._right_is_initialized:
            return True
        if node.right:
            if not self.conservative_is_ordered2(node.right, node.data, max):
                return False
        return True

    def conservative_is_balanced(self):
        queue = []
        if not self._root_is_initialized:
            return True
        queue.append(self.root)
        while queue:
            current = queue.pop(0)
            if current.bf > 1 or current.bf < -1:
                return False
            if not current._left_is_initialized:
                return True
            if current.left:
                queue.append(current.left)
            if not current._right_is_initialized:
                return True
            if current.right:
                queue.append(current.right)
        return True

    # =================================================================== #

    # The instrumented method should have replaced accesses to fields by
    # the above getters and setters, and types annotated.
    def instrumented_insert(self, key: int):
        # PART 1: Ordinary BST insert
        node = Node(key)
        y = None
        x = self._get_root()

        while x:
            y = x
            if node.data < x.data:
                x = x._get_left()
            else:
                x = x._get_right()

        # y is parent of x
        node._set_parent(y)
        if not y:
            self._set_root(node)
        elif node.data < y.data:
            y._set_left(node)
        else:
            y._set_right(node)

        # PART 2: re-balance the node if necessary
        self.instrumented_updateBalance(node)

    # Methods called inside method under test should be also instrumented.
    def instrumented_updateBalance(self, node):
        if node.bf < -1 or node.bf > 1:
            self.instrumented_rebalance(node)
            return

        if node._get_parent() is not None:
            if node == node._get_parent()._get_left():
                node._get_parent().bf -= 1

            if node == node._get_parent()._get_right():
                node._get_parent().bf += 1

            if node._get_parent().bf != 0:
                self.instrumented_updateBalance(node._get_parent())

    def instrumented_rebalance(self, node):
        if node.bf > 0:
            if node._get_right().bf < 0:
                self.instrumented_rightRotate(node._get_right())
                self.instrumented_leftRotate(node)
            else:
                self.instrumented_leftRotate(node)
        elif node.bf < 0:
            if node._get_left().bf > 0:
                self.instrumented_leftRotate(node._get_left())
                self.instrumented_rightRotate(node)
            else:
                self.instrumented_rightRotate(node)

    def instrumented_leftRotate(self, x):
        y = x._get_right()
        x._set_right(y._get_left())
        if y._get_left() is not None:
            y._set_parent(x)

        y._set_parent(x._get_parent())
        if x._get_parent() is None:
            self._set_root(y)
        elif x == x._get_parent()._get_left():
            x._get_parent()._set_left(y)
        else:
            x._get_parent()._set_right(y)
        y._set_left(x)
        x._set_parent(y)

        # update the balance factor
        x.bf = x.bf - 1 - max(0, y.bf)
        y.bf = y.bf - 1 + min(0, x.bf)

    def instrumented_rightRotate(self, x):
        y = x._get_left()
        x._set_left(y._get_right())
        if y._get_right() is not None:
            y._get_right()._set_parent(x)

        y._set_parent(x._get_parent())
        if x._get_parent() is None:
            self._set_root(y)
        elif x == x._get_parent()._get_right():
            x._get_parent()._set_right(y)
        else:
            x._get_parent()._set_left(y)

        y._set_right(x)
        x._set_parent(y)

        # update the balance factor
        x.bf = x.bf + 1 - min(0, y.bf)
        y.bf = y.bf + 1 + max(0, x.bf)

    def __printHelper(self, currPtr, indent, last):
        # print the tree structure on the screen
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R->")
                indent += "     "
            else:
                sys.stdout.write("L->")
                indent += "|    "

            print(currPtr.data)

            self.__printHelper(currPtr.left, indent, False)
            self.__printHelper(currPtr.right, indent, True)

    def __repr__(self):
        if self.root is None:
            return "EmptyTree"
        assert self.conservative_repok()
        rep = self.to_str3(self.root, set(), "", True)
        return "\n" + rep + "\n"

    def to_str3(self, node, visited, indent, last):
        str_rep = ""
        if node is not None:
            if node in visited:
                str_rep += indent + str(node.data) + "*\n"
            else:
                visited.add(node)
                str_rep += indent
                if last:
                    str_rep += "R->"
                    indent += "     "
                else:
                    str_rep += "L->"
                    indent += "|    "

                str_rep += node.data.__repr__() + "\n"

                str_rep += self.to_str3(node.left, visited, indent, False)
                str_rep += self.to_str3(node.right, visited, indent, True)
        return str_rep

    def __searchTreeHelper(self, node, key):
        if node is None or key == node.data:
            return node

        if key < node.data:
            return self.__searchTreeHelper(node.left, key)
        return self.__searchTreeHelper(node.right, key)

    def __deleteNodeHelper(self, node, key):
        # search the key
        if node is None:
            return node
        elif key < node.data:
            node.left = self.__deleteNodeHelper(node.left, key)
        elif key > node.data:
            node.right = self.__deleteNodeHelper(node.right, key)
        else:
            # the key has been found, now delete it

            # case 1: node is a leaf node
            if node.left is None and node.right is None:
                node = None

            # case 2: node has only one child
            elif node.left is None:
                temp = node
                node = node.right

            elif node.right is None:
                temp = node
                node = node.left

            # case 3: has both children
            else:
                temp = self.minimum(node.right)
                node.data = temp.data
                node.right = self.__deleteNodeHelper(node.right, temp.data)

            # Write the update balance logic here
            # YOUR CODE HERE
        return node

    # update the balance factor the node
    def __updateBalance(self, node):
        if node.bf < -1 or node.bf > 1:
            self.__rebalance(node)
            return

        if node.parent is not None:
            if node == node.parent.left:
                node.parent.bf -= 1

            if node == node.parent.right:
                node.parent.bf += 1

            if node.parent.bf != 0:
                self.__updateBalance(node.parent)

    def __rebalance(self, node):
        if node.bf > 0:
            if node.right.bf < 0:
                self.rightRotate(node.right)
                self.leftRotate(node)
            else:
                self.leftRotate(node)
        elif node.bf < 0:
            if node.left.bf > 0:
                self.leftRotate(node.left)
                self.rightRotate(node)
            else:
                self.rightRotate(node)

    def __preOrderHelper(self, node):
        if node is not None:
            sys.stdout.write(node.data + " ")
            self.__preOrderHelper(node.left)
            self.__preOrderHelper(node.right)

    def __inOrderHelper(self, node):
        if node is not None:
            self.__inOrderHelper(node.left)
            sys.stdout.write(node.data + " ")
            self.__inOrderHelper(node.right)

    def __postOrderHelper(self, node):
        if node is not None:
            self.__postOrderHelper(node.left)
            self.__postOrderHelper(node.right)
            sys.stdout.write(node.data + " ")

    # Pre-Order traversal
    # Node->Left Subtree->Right Subtree
    def preorder(self):
        self.__preOrderHelper(self.root)

    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def inorder(self):
        self.__inOrderHelper(self.root)

    # Post-Order traversal
    # Left Subtree -> Right Subtree -> Node
    def postorder(self):
        self.__postOrderHelper(self.root)

    # search the tree for the key k
    # and return the corresponding node
    def searchTree(self, k):
        return self.__searchTreeHelper(self.root, k)

    # find the node with the minimum key
    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not None,
        # the successor is the leftmost node in the
        # right subtree
        if x.right is not None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self, x):
        # if the left subtree is not None,
        # the predecessor is the rightmost node in the
        # left subtree
        if x.left is not None:
            return self.maximum(x.left)

        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    # rotate left at node x
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        # update the balance factor
        x.bf = x.bf - 1 - max(0, y.bf)
        y.bf = y.bf - 1 + min(0, x.bf)

    # rotate right at node x
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        # update the balance factor
        x.bf = x.bf + 1 - min(0, y.bf)
        y.bf = y.bf + 1 + max(0, x.bf)

    # insert the key to the tree in its appropriate position
    def insert(self, key):
        # PART 1: Ordinary BST insert
        node = Node(key)
        y = None
        x = self.root

        while x:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # PART 2: re-balance the node if necessary
        self.__updateBalance(node)

    def deleteNode(self, data):
        return self.__deleteNodeHelper(self.root, data)

    # print the tree structure on the screen
    def prettyPrint(self):
        self.__printHelper(self.root, "", True)

    def d_is_acyclic(self):
        if not self.root:
            return True
        visited = set()
        visited.add(self.root)
        worklist = []
        worklist.append(self.root)
        while worklist:
            current = worklist.pop(0)
            if current.left:
                if not AVLTree.do_add(visited, current.left):
                    return False
                worklist.append(current.left)
            if current.right:
                if not AVLTree.do_add(visited, current.right):
                    return False
                worklist.append(current.right)
        return True
