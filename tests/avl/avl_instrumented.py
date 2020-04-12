INT_MAX = 4294967296
INT_MIN = -4294967296


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:

    _vector = []
    _engine = None
    _id = 0

    # Instance attributes annotations (will be treated as symbolic)
    data: int
    right: "Node"
    left: "Node"
    parent: "Node"

    # Init params should be annotated also
    def __init__(self, parent: "Node", data: int):
        self.data = data
        self.right = None
        self.left = None
        self.parent = parent
        self.height = 0

        self._data_is_initialized = True
        self._right_is_initialized = False
        self._left_is_initialized = False
        self._parent_is_initialized = False
        self._height_is_initialized = True

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_data(self):
        if not self._data_is_initialized:
            self._key_is_initialized = True
            self.data = self._engine.sym_int()
        return self.data

    def _set_data(self, value):
        self.data = value
        self._data_is_initialized = True

    def _get_right(self):
        if not self._right_is_initialized and self._engine.is_tracked(self):
            self._right_is_initialized = True
            self.right = self._engine.get_next_lazy_step(Node, Node._vector)
            self._engine.save_lazy_step(Node)
            self._engine.ignore_if(not self.conservative_repok(), self)
        else:
            self._engine.check_recursion_limit(self.right)
        return self.right

    def _set_right(self, value):
        self.right = value
        self._right_is_initialized = True

    def _get_left(self):
        if not self._left_is_initialized and self._engine.is_tracked(self):
            self._left_is_initialized = True
            self.left = self._engine.get_next_lazy_step(Node, Node._vector)
            self._engine.save_lazy_step(Node)
            self._engine.ignore_if(not self.conservative_repok(), self)
        else:
            self._engine.check_recursion_limit(self.left)
        return self.left

    def _set_left(self, value):
        self.left = value
        self._left_is_initialized = True

    def _get_parent(self):
        if not self._parent_is_initialized and self._engine.is_tracked(self):
            self._parent_is_initialized = True
            self.parent = self._engine.get_next_lazy_step(Node, Node._vector)
            self._engine.save_lazy_step(Node)
            self._engine.ignore_if(not self.conservative_repok(), self)
        else:
            self._engine.check_recursion_limit(self.parent)
        return self.parent

    def _set_parent(self, value):
        self.parent = value
        self._parent_is_initialized = True

    def is_balanced(self, node):
        return self.is_balanced_helper(node) > -1

    def con_is_balanced(self, node):
        return self.con_is_balanced_helper(node) > -1

    def is_balanced_helper(self, node):
        if node is None:
            return 0
        left_height = self.is_balanced_helper(node.left)
        if left_height == -1:
            return -1
        right_height = self.is_balanced_helper(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def con_is_balanced_helper(self, node):
        if node is None:
            return 0
        if not node._left_is_initialized:
            return 0
        left_height = self.con_is_balanced_helper(node.left)
        if left_height == -1:
            return -1
        if not node._right_is_initialized:
            return 0
        right_height = self.con_is_balanced_helper(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def repok(self):
        visited = set()
        visited.add(self)
        if self.left is not None:
            if not do_add(visited, self.left) or self.left.data > self.data:
                return False
            if self.left.parent is None or self.left.parent is not self:
                return False
        if self.right is not None:
            if not do_add(visited, self.right) or self.right.data < self.data:
                return False
            if self.right.parent is None or self.right.parent is not self:
                return False

        if self.parent is not None:
            if not do_add(visited, self.parent):
                return False
            if self.parent.left is None:
                if self.parent.right is None or self.parent.right is not self:
                    return False

            if self.parent.right is None:
                if self.parent.left is None or self.parent.left is not self:
                    return False

            if self.parent.left is not None and self.parent.right is not None:
                if not (self.parent.left is self or self.parent.right is self):
                    return False

            if self.parent.left is self and self.data > self.parent.data:
                return False
            if self.parent.right is self and self.data < self.parent.data:
                return False

            # return self.is_balanced(self.parent)
        return True

    def conservative_repok(self):
        visited = set()
        visited.add(self)
        if not self._left_is_initialized:
            return True
        if self.left is not None:
            if not self.left._data_is_initialized or not self._data_is_initialized:
                return True
            if not do_add(visited, self.left) or self.left.data > self.data:
                return False

            if not self.left._parent_is_initialized:
                return True
            if self.left.parent is None or self.left.parent is not self:
                return False

        if not self._right_is_initialized:
            return True
        if self.right is not None:
            if not self.right._data_is_initialized or not self._data_is_initialized:
                return True
            if not do_add(visited, self.right) or self.right.data < self.data:
                return False

            if not self.right._parent_is_initialized:
                return True
            if self.right.parent is None or self.right.parent is not self:
                return False

        if not self._parent_is_initialized:
            return True
        if self.parent is not None:
            if not do_add(visited, self.parent):
                return False
            if not self.parent._left_is_initialized:
                return True
            if self.parent.left is None:
                if not self.parent._right_is_initialized:
                    return True
                if self.parent.right is None or self.parent.right is not self:
                    return False

            if not self.parent._right_is_initialized:
                return True
            if self.parent.right is None:
                if not self.parent._left_is_initialized:
                    return True
                if self.parent.left is None or self.parent.left is not self:
                    return False

            if self.parent.left is not None and self.parent.right is not None:
                if not (self.parent.left is self or self.parent.right is self):
                    return False

            if not self._data_is_initialized or not self.parent._data_is_initialized:
                return True
            if self.parent.left is self and self.data > self.parent.data:
                return False

            if self.parent.right is self and self.data < self.parent.data:
                return False

            # return self.con_is_balanced(self.parent)
        return True

    # def repok(self):
    #     return True

    # def conservative_repok(self):
    #     return True

    def instrumented_repok(self):
        return True

    def __repr__(self):
        if self.parent is not None:
            return self.parent._identifier + " <- " + self._identifier + ": " + str(self.data)
        if self._parent_is_initialized:
            return "None" + " <- " + self._identifier + ": " + str(self.data)
        return "CLOUD" + " <- " + self._identifier + ": " + str(self.data)

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k.
        """
        if k == self._get_data():
            return self
        elif k < self._get_data():
            if self._get_left() is None:
                return None
            else:
                return self._get_left().find(k)
        else:
            if self._get_right() is None:
                return None
            else:
                return self._get_right().find(k)

    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this
        node.

        Returns:
            The node with the minimum key.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def next_larger(self):
        """Returns the node with the next larger key (the successor) in the BST.
        """
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node._get_data() < self._get_data():
            if self._get_left() is None:
                node._set_parent(self)
                self._set_left(node)
            else:
                self._get_left().insert(node)
        else:
            if self._get_right() is None:
                node._set_parent(self)
                self._set_right(node)
            else:
                self._get_right().insert(node)

    def delete(self):
        """Deletes and returns this node from the tree."""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.data, s.data = s.data, self.data
            return s.delete()

    def update_height(self):
        self.height = max(height(self._get_left()), height(self._get_right())) + 1


def height(node):
    if node is None:
        return -1
    else:
        return node.height


class AVL():

    _vector = []
    _engine = None
    _id = 0

    # Instance attributes annotations (will be treated as symbolic)
    root: "Node"

    # Init params should be annotated also
    def __init__(self, root: "Node" = None):
        self.root = root

        self._root_is_initialized = False

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    def _get_root(self):
        if not self._root_is_initialized and self._engine.is_tracked(self):
            self._root_is_initialized = True
            self.root = self._engine.get_next_lazy_step(Node, Node._vector)
            self._engine.save_lazy_step(Node)
            self._engine.ignore_if(not self.conservative_repok(), self)
        else:
            self._engine.check_recursion_limit(self.root)
        return self.root

    def _set_root(self, value):
        self.root = value
        self._root_is_initialized = True

    def to_str(self, node, visited):
        """Internal method for ASCII art."""
        label = node.__repr__()
        if node.left is None:
            if node._right_is_initialized:
                left_lines, left_pos, left_width = ["None"], 0, 0
            else:
                left_lines, left_pos, left_width = [], 0, 0
        else:
            if do_add(visited, node.left):
                left_lines, left_pos, left_width = self.to_str(node.left, visited)
            else:
                left_lines, left_pos, left_width = [str(node.left.data) + "*"], 0, 0
        if node.right is None:
            if node._right_is_initialized:
                right_lines, right_pos, right_width = ["None"], 0, 0
            else:
                right_lines, right_pos, right_width = [], 0, 0
        else:
            if do_add(visited, node.right):
                right_lines, right_pos, right_width = self.to_str(node.right, visited)
            else:
                right_lines, right_pos, right_width = [str(node.right.data) + "*"], 0, 0
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and node.parent is not None and \
           node is node.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) + right_line for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __repr__(self):
        if self.root is None:
            return '<empty tree>'
        visited = set()
        visited.add(self.root)
        s = '\n'.join(self.to_str(self.root, visited)[0])
        result = ""
        for line in s.splitlines():
            result += "        " + line + "\n"
        return "\n" + result

    def find(self, k: int):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k or None if the tree is empty.
        """
        return self._get_root() and self._get_root().find(k)

    def find_min(self):
        """Returns the minimum node of this BST."""

        return self.root and self.root.find_min()

    def next_larger(self, k):
        """Returns the node that contains the next larger (the successor) key in
        the BST in relation to the node with key k.

        Args:
            k: The key of the node of which the successor is to be found.

        Returns:
            The successor node.
        """
        node = self.find(k)
        return node and node.next_larger()

    def left_rotate(self, x):
        y = x._get_right()
        y._set_parent(x._get_parent())
        if y._get_parent() is None:
            self._set_root(y)
        else:
            if y._get_parent()._get_left() is x:
                y._get_parent()._set_left(y)
            elif y._get_parent()._get_right() is x:
                y._get_parent()._set_right(y)
        x._set_right(y._get_left())
        if x._get_right() is not None:
            x._get_right()._set_parent(x)
        y._set_left(x)
        x._set_parent(y)
        x.update_height()
        y.update_height()

    def right_rotate(self, x):
        y = x._get_left()
        y._set_parent(x._get_parent())
        if y._get_parent() is None:
            self._set_root(y)
        else:
            if y._get_parent()._get_left() is x:
                y._get_parent()._set_left(y)
            elif y._get_parent()._get_right() is x:
                y._get_parent()._set_right(y)
        x._set_left(y._get_right())
        if x._get_left() is not None:
            x._get_left()._set_parent(x)
        y._set_right(x)
        x._set_parent(y)
        x.update_height()
        y.update_height()

    def rebalance(self, node):
        while node is not None:
            node.update_height()
            if height(node._get_left()) >= 2 + height(node._get_right()):
                if height(node._get_left()._get_left()) >= height(node._get_left()._get_right()):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node._get_left())
                    self.right_rotate(node)
            elif height(node._get_right()) >= 2 + height(node._get_left()):
                if height(node._get_right()._get_right()) >= height(node._get_right()._get_left()):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node._get_right())
                    self.left_rotate(node)
            node = node._get_parent()

    def insert(self, k: int):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node to be inserted.
        """
        node = Node(None, k)
        if self._get_root() is None:
            # The root's parent is None.
            self._set_root(node)
        else:
            self._get_root().insert(node)
        self.rebalance(node)

    def insert2(self, node: "Node"):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node to be inserted.
        """
        if self._get_root() is None:
            # The root's parent is None.
            self._set_root(node)
        else:
            self._get_root().insert(node)
        self.rebalance(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node that we want to delete.

        Returns:
            The deleted node with key k.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = Node(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
        else:
            deleted = node.delete()
        self.rebalance(deleted.parent)

    def repok(self):
        if self.root is None:
            return True
        if self.root.parent is not None:
            return False
        visited = set()
        visited.add(self.root)
        isbst = self.is_BST(self.root, INT_MIN, INT_MAX, visited)
        return isbst and self.is_balanced()

    def is_balanced_helper(self, node):
        if node is None:
            return 0
        left_height = self.is_balanced_helper(node.left)
        if left_height == -1:
            return -1
        right_height = self.is_balanced_helper(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def is_balanced(self):
        return self.is_balanced_helper(self.root) > -1

    def ins_is_balanced_helper(self, node):
        if node is None:
            return 0
        left_height = self.ins_is_balanced_helper(node._get_left())
        if left_height == -1:
            return -1
        right_height = self.ins_is_balanced_helper(node._get_right())
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def ins_is_balanced(self):
        return self.ins_is_balanced_helper(self._get_root()) > -1

    def con_is_balanced_helper(self, node):
        if node is None:
            return 0
        if not node._left_is_initialized:
            return 0
        left_height = self.con_is_balanced_helper(node.left)
        if left_height == -1:
            return -1
        if not node._right_is_initialized:
            return 0
        right_height = self.con_is_balanced_helper(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def con_is_balanced(self):
        if not self._root_is_initialized:
            return True
        return self.con_is_balanced_helper(self.root) > -1

    def conservative_repok(self):

        if not self._root_is_initialized:
            return True

        if self.root is None:
            return True

        if not self.root._parent_is_initialized:
            return True

        if self.root.parent is not None:
            return False

        visited = set()
        visited.add(self.root)
        isbst = self.conservative_is_BST(self.root, INT_MIN, INT_MAX, visited)
        return isbst and self.con_is_balanced()

    def instrumented_repok(self):
        if self._get_root() is None:
            return True
        if self._get_root()._get_parent() is not None:
            return False
        visited = set()
        visited.add(self._get_root())
        isbst = self.instrumented_is_BST(self._get_root(), INT_MIN, INT_MAX, visited)
        return isbst and self.ins_is_balanced()

    def is_BST(self, node, min, max, visited):
        if node is None:
            return True
        if node is not self.root:
            if node.parent is None:
                return False
            if node.parent.right is not node and node.parent.left is not node:
                return False

        if node.left is not None:
            if not do_add(visited, node.left) or node.left.parent is not node:
                return False

        if node.right is not None:
            if not do_add(visited, node.right) or node.right.parent is not node:
                return False

        if node.data < min or node.data > max:
            return False

        return self.is_BST(node.left, min, node.data, visited) and self.is_BST(
            node.right, node.data, max, visited
        )

    def conservative_is_BST(self, node, min, max, visited):
        if node is None:
            return True

        if node is not self.root:
            if not node._parent_is_initialized:
                return

            if node.parent is None:
                return False

            if not node.parent._right_is_initialized or not node.parent._left_is_initialized:
                return True

            if node.parent.right is not node and node.parent.left is not node:
                return False

        if not node._left_is_initialized:
            return True

        if node.left is not None:
            if not node.left._parent_is_initialized:
                return True
            if not do_add(visited, node.left) or node.left.parent is not node:
                return False

        if not node._right_is_initialized:
            return True

        if node.right is not None:

            if not node.right._parent_is_initialized:
                return True

            if not do_add(visited, node.right) or node.right.parent is not node:
                return False

        if not node._data_is_initialized:
            return True

        if node.data < min or node.data > max:
            return False

        return self.conservative_is_BST(node.left, min, node.data, visited) and self.conservative_is_BST(
            node.right, node.data, max, visited
        )

    def instrumented_is_BST(self, node, min, max, visited):
        if node is None:
            return True

        if node is not self._get_root():
            if node._get_parent() is None:
                return False
            if node._get_parent()._get_right() is not node and node._get_parent()._get_left() is not node:
                return False

        if node._get_left() is not None:
            if not do_add(visited, node._get_left()) or node._get_left()._get_parent() is not node:
                return False

        if node._get_right() is not None:
            if not do_add(visited, node._get_right()) or node._get_right()._get_parent() is not node:
                return False

        if node._get_data() < min or node._get_data() > max:
            return False

        return self.instrumented_is_BST(node._get_left(), min, node._get_data(), visited) and self.instrumented_is_BST(
            node._get_right(), node._get_data(), max, visited
        )
