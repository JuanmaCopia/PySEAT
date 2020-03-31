INT_MAX = 4294967296
INT_MIN = -4294967296


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def repok(self):
        visited = set()
        visited.add(self.root)
        return self.is_BST(self.root, INT_MIN, INT_MAX, visited)

    def is_BST(self, node, min, max, visited):
        if node is None:
            return True
        if (
            node.data <= min
            or node.data >= max
            or (node.left is not None and not do_add(visited, node.left))
            or (node.right is not None and not do_add(visited, node.right))
            or (node is not self.root and node.parent is None)
            or (node.parent is not None and do_add(visited, node.parent))
            or node.right.parent is not node
            or node.left.parent is not node
        ):
            return False

        return self.is_BST(node.left, min, node.data, visited) and self.is_BST(
            node.right, node.data, max, visited
        )

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left is not None:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._find(value, cur_node.right)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        # Protect against deleting a node not found in the tree
        if node is None or self.find(node.value) is None:
            print("Node to be deleted not found in the tree!")
            return None

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
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
            if node_parent is not None:
                # remove reference to the node from the parent
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent is not None:
                # replace the node to be deleted with its child
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        return False
