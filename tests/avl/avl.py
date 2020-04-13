INT_MAX = 4294967296
INT_MIN = -4294967296


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node():
    """A node in the AVL tree."""

    def __init__(self, parent, k):
        """Creates a node.

        Args:
            parent: The node's parent.
            k: key of the node.
        """
        self.data = k
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0

    def _str(self, visited):
        """Internal method for ASCII art."""
        label = str(self.data)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            if do_add(visited, self.left):
                left_lines, left_pos, left_width = self.left._str(visited)
            else:
                left_lines, left_pos, left_width = [], 0, 0
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            if do_add(visited, self.right):
                right_lines, right_pos, right_width = self.right._str(visited)
            else:
                right_lines, right_pos, right_width = [], 0, 0
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
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

    def __str__(self):
        visited = set()
        visited.add(self)
        return '\n'.join(self._str(visited)[0])

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k.
        """
        if k == self.data:
            return self
        elif k < self.data:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

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
        if node.data < self.data:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

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


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVL():
    """
    AVL binary search tree implementation.
    """

    def __init__(self, root=None):
        """ empty tree """
        self.root = root

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        return str(self.root)

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k or None if the tree is empty.
        """
        return self.root and self.root.find(k)

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
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).

        Args:
            k: The key of the node to be inserted.
        """
        node = Node(None, k)
        if self.root is None:
            # The root's parent is None.
            self.root = node
        else:
            self.root.insert(node)
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
        # node.parent is actually the old parent of the node,
        # which is the first potentially out-of-balance node.
        self.rebalance(deleted.parent)

    def repok(self):
        if not self.root:
            return True
        if not (
            self.is_acyclic() and
            self.is_ordered() and
            self.is_balanced(self.root)
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
                if not do_add(visited, current.left):
                    return False
                worklist.append(current.left)
            if current.right:
                if not do_add(visited, current.right):
                    return False
                worklist.append(current.right)
        return True

    def is_ordered(self):
        return self.is_ordered2(self.root, INT_MIN, INT_MAX)

    def is_ordered2(self, node, min, max):
        if node.data < min or node.data > max:
            return False
        if node.left:
            if not self.is_ordered2(node.left, min, node.data):
                return False
        if node.right:
            if not self.is_ordered2(node.right, node.data, max):
                return False
        return True

    def is_balanced(self, node):
        if node is None:
            return True
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return abs(left_height - right_height) <= 1

    def get_height(self, node):
        if node is None:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1

# def test(args=None):
#     import random, sys
#     if not args:
#         args = sys.argv[1:]
#     if not args:
#         print('usage: %s <number-of-random-items | item item item ...>' % \
#               sys.argv[0])
#         sys.exit()
#     elif len(args) == 1:
#         items = (random.randrange(100) for i in range(int(args[0])))
#     else:
#         items = [int(i) for i in args]

#     tree = AVL()
#     print(tree)
#     for item in items:
#         tree.insert(item)
#         print()
#         print(tree)
#         if tree.repok():
#             print("ok")
#         assert tree.repok()


# if __name__ == '__main__':
#     test()
