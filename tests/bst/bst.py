import sys


def do_add(s, x):  # pragma: no cover
    length = len(s)
    s.add(x)
    return len(s) != length


class node:
    # Instance attributes annotations (will be treated as symbolic)
    value: int
    right_child: "node"
    left_child: "node"
    parent: "node"

    def __init__(self, value: int = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree

    def __repr__(self):
        return "node: " + str(self.value)


class BST:
    # Instance attributes annotations (will be treated as symbolic)
    root: "node"

    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    # def print_tree(self):
    #     if self.root != None:
    #         self._print_tree(self.root)

    # def _print_tree(self, cur_node):
    #     if cur_node != None:
    #         self._print_tree(cur_node.left_child)
    #         print(str(cur_node.value))
    #         self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value: int):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value: int):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        ## -----
        # Improvements since prior lesson

        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            print("Node to be deleted not found in the tree!")
            return None
        ## -----

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

    def repok(self):  # pragma: no cover
        if not self.root:
            return True
        if not (self.is_acyclic() and self.is_ordered() and self.parents_ok(self.root)):
            return False
        if self.root.parent is not None:
            return False
        return True

    def is_acyclic(self):  # pragma: no cover
        visited = set()
        visited.add(self.root)
        worklist = []
        worklist.append(self.root)
        while worklist:
            current = worklist.pop(0)
            if current.left_child:
                if not do_add(visited, current.left_child):
                    return False
                worklist.append(current.left_child)
            if current.right_child:
                if not do_add(visited, current.right_child):
                    return False
                worklist.append(current.right_child)
        return True

    def is_ordered(self):  # pragma: no cover
        return self.is_ordered2(self.root, -sys.maxsize, sys.maxsize)

    def is_ordered2(self, node, min, max):  # pragma: no cover
        if node.value <= min or node.value >= max:
            return False
        if node.left_child:
            if not self.is_ordered2(node.left_child, min, node.value):
                return False
        if node.right_child:
            if not self.is_ordered2(node.right_child, node.value, max):
                return False
        return True

    def parents_ok(self, node):  # pragma: no cover
        if node is None:
            return True

        if node.left_child is not None:
            if node.left_child.parent is not node:
                return False

        if node.right_child is not None:
            if node.right_child.parent is not node:
                return False

        return self.parents_ok(node.left_child) and self.parents_ok(node.right_child)

    def to_str(self, node):  # pragma: no cover
        """Returns list of strings, width, height, and horizontal coord of root."""
        # No child.

        if node.right_child is None and node.left_child is None:
            line = "%s" % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right_child is None:
            lines, n, p, x = self.to_str(node.left_child)
            s = "%s" % node.value
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left_child is None:
            lines, n, p, x = self.to_str(node.right_child)
            s = "%s" % node.value
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.to_str(node.left_child)
        right, m, q, y = self.to_str(node.right_child)
        s = "%s" % node.value
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __repr__(self):  # pragma: no cover
        if self.root is None:
            return "<empty tree>"
        lines, _, _, _ = self.to_str(self.root)
        result = ""
        for line in lines:
            result += "        " + line + "\n"
        return "\n" + result
