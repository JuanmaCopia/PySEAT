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

    # We need to add type annotations, there is no need to annotate self
    def  __init__(self, data: int):
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
        self._identifier = ""
        self._generated = False
        self._marked = False

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
        self._identifier = ""
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

    def conservative_repok(self):
        if not self._root_is_initialized:
            return True
        if not self.root:
            return True
        if not (self.is_acyclic() and self.is_ordered() and self.is_balanced()):
            return False
        return True


    def repok(self):
        if not self.root:
            return True
        if not (self.is_acyclic() and self.is_ordered() and self.is_balanced()):
            return False
        return True


    @staticmethod
    def do_add(s, x):
        l = len(s)
        s.add(x)
        return len(s) != l

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
        return self.is_ordered2(self.root, -1, -1);

    def is_ordered2(self, node, min, max):
        if (min != -1 and node.elem <= min) or (max != -1 and node.elem >= max):
            return False
        if node.left:
            if not self.is_ordered2(node.left, min, node.elem):
                return False
        if node.right:
            if not self.is_ordered2(node.right, node.elem, max):
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
                queue.add(current.left)
            if current.right:
                queue.add(current.right)
        return True 


    # private boolean isBalanced(){
	# 	LinkedList<AvlNode> queue = new LinkedList<AvlNode>();
	# 	queue.add(root);
    #     while (!queue.isEmpty()) {
    #         AvlNode current = (AvlNode) queue.removeFirst();
    #         int l_Height = current.left == null ? 0 : current.left.height;
	# 		int r_Height = current.right == null ? 0 : current.right.height;
	# 		int difference = l_Height - r_Height;
	# 		if (difference < -1 || difference > 1)
	# 			return false; // Not balanced.
	# 		int max = l_Height > r_Height ? l_Height : r_Height;
	# 		if (current.height != 1 + max)
	# 			return false; // Wrong height.
    #         if (current.left != null) {
    #         	queue.add(current.left);
    #         }
    #         if (current.right != null) {
    #         	queue.add(current.right);
    #         }
    #     }
    #     return true;
		
	}

    # private boolean isOrdered(AvlNode n) {
    #      return isOrdered(n, -1, -1);
    #  }

    #  private boolean isOrdered(AvlNode n, int min, int max) {
    #      // if (n.info == null)
    #      // return false;
    #      if (n.data == -1)
    #          return false;
    #      // if ((min != null && n.info.compareTo(min) <= 0)
    #      // || (max != null && n.info.compareTo(max) >= 0))
    #      if ((min != -1 && n.data <= (min)) || (max != -1 && n.data >= (max)))

    #          return false;
    #      if (n.left != null)
    #          if (!isOrdered(n.left, min, n.data))
    #              return false;
    #      if (n.right != null)
    #          if (!isOrdered(n.right, n.data, max))
    #              return false;
    #      return true;
    #  }

    # private boolean isAcyclic() {
    #       Set<AvlNode> visited = new HashSet<AvlNode>();
    #       visited.add(root);
    #       LinkedList<AvlNode> workList = new LinkedList<AvlNode>();
    #       workList.add(root);
    #       while (!workList.isEmpty()) {
    #           AvlNode current = (AvlNode) workList.removeFirst();
    #           if (current.left != null) {
    #               // checks that the tree has no cycle
    #               if (!visited.add(current.left))
    #                   return false;
    #               workList.add(current.left);
    #           }
    #           if (current.right != null) {
    #               // checks that the tree has no cycle
    #               if (!visited.add(current.right))
    #                   return false;
    #               workList.add(current.right);
    #           }
    #       }
    #       return true;
    #   }

    # The instrumented method should have replaced accesses to fields by the above getters
    # and setters, and types annotated.
    def instrumented_insert(self, key: int):
        # PART 1: Ordinary BST insert
        node =  Node(key)
        y = None
        x = self._get_root()

        while x != None:
            y = x
            if node.data < x.data:
                x = x._get_left()
            else:
                x = x._get_right()

        # y is parent of x
        node._set_parent(y)
        if y == None:
            self._set_root(node)
        elif node.data < y.data:
            y._set_left(node)
        else:
            y._set_right(node)

        # PART 2: re-balance the node if necessary
        self.__ins_updateBalance(node)

    # any method called inside the method under test should be also instrumented.
    def __ins_updateBalance(self, node):
        if node.bf < -1 or node.bf > 1:
            self.__ins_rebalance(node)
            return

        if node._get_parent() != None:
            if node == node._get_parent()._get_left():
                node._get_parent().bf -= 1

            if node == node._get_parent()._get_right():
                node._get_parent().bf += 1

            if node._get_parent().bf != 0:
                self.__ins_updateBalance(node._get_parent())


    def __ins_rebalance(self, node):
        if node.bf > 0:
            if node._get_right().bf < 0:
                self.ins_rightRotate(node._get_right())
                self.ins_leftRotate(node)
            else:
                self.ins_leftRotate(node)
        elif node.bf < 0:
            if node._get_left().bf > 0:
                self.ins_leftRotate(node._get_left())
                self.ins_rightRotate(node)
            else:
                self.ins_rightRotate(node)


    def ins_leftRotate(self, x):
        y = x._get_right()
        x._set_right(y._get_left())
        if y._get_left() != None:
            y._set_parent(x)

        y._set_parent(x._get_parent()) 
        if x._get_parent() == None:
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


    def ins_rightRotate(self, x):
        y = x._get_left()
        x._set_left(y._get_right())
        if y._get_right() != None:
            y._get_right()._set_parent(x)
        
        y._set_parent(x._get_parent())
        if x._get_parent() == None:
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
        if currPtr != None:
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

    def to_str(self, currPtr, indent, last):
        # print the tree structure on the screen
        str_rep = ""
        if currPtr != None:
            str_rep += indent
            if last:
                str_rep += "R->"
                indent += "     "
            else:
                str_rep += "L->"
                indent += "|    "

            str_rep += currPtr.data.__repr__() + "\n"

            str_rep += self.to_str(currPtr.left, indent, False)
            str_rep += self.to_str(currPtr.right, indent, True)
            return str_rep
        return "None"
    
    def __searchTreeHelper(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.__searchTreeHelper(node.left, key)
        return self.__searchTreeHelper(node.right, key)

    def __deleteNodeHelper(self, node, key):
        # search the key
        if node == None: 
            return node
        elif key < node.data:
            node.left = self.__deleteNodeHelper(node.left, key)
        elif key > node.data: 
            node.right = self.__deleteNodeHelper(node.right, key)
        else:
            # the key has been found, now delete it

            # case 1: node is a leaf node
            if node.left == None and node.right == None:
                node = None

            # case 2: node has only one child
            elif node.left == None:
                temp = node
                node = node.right

            elif node.right == None:
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

        if node.parent != None:
            if node == node.parent.left:
                node.parent.bf -= 1

            if node == node.parent.right:
                node.parent.bf += 1

            if node.parent.bf != 0:
                self.__updateBalance(node.parent)

     # rebalance the tree
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
        if node != None:
            sys.stdout.write(node.data + " ")
            self.__preOrderHelper(node.left)
            self.__preOrderHelper(node.right)

    def __inOrderHelper(self, node):
        if node != None:
            self.__inOrderHelper(node.left)
            sys.stdout.write(node.data + " ")
            self.__inOrderHelper(node.right)

    def __postOrderHelper(self, node):
        if node != None:
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
        while node.left != None:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not None,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self, x):
        # if the left subtree is not None,
        # the predecessor is the rightmost node in the 
        # left subtree
        if x.left != None:
            return self.maximum(x.left)

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    # rotate left at node x
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
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
        if y.right != None:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent == None:
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
        node =  Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # PART 2: re-balance the node if necessary
        self.__updateBalance(node)


    # delete the node from the tree
    def deleteNode(self, data):
        return self.__deleteNodeHelper(self.root, data)

    # print the tree structure on the screen
    def prettyPrint(self):
        self.__printHelper(self.root, "", True)

    def __repr__(self):
        return "\n" + self.to_str(self.root, "", True) + "\n"