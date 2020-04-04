INT_MAX = 4294967296
INT_MIN = -4294967296


def do_add(s, x):
    length = len(s)
    s.add(x)
    return len(s) != length


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data) + "\n"


class BST:
    def __init__(self, root=None):
        self.root = None

    def repok(self):
        if self.root is None:
            return True
        if self.root.parent is not None:
            return False
        visited = set()
        visited.add(self.root)
        return self.is_BST(self.root, INT_MIN, INT_MAX, visited)

    def is_BST(self, node, min, max, visited):
        if node is None:
            return True
        if (
            node.data <= min
            or node.data >= max
            or (node is not self.root and node.parent is None)
            or (node.parent is not None and do_add(visited, node.parent))
            or (
                node.left is not None
                and (not do_add(visited, node.left) or node.left.parent is not node)
            )
            or (
                node.right is not None
                and (not do_add(visited, node.right) or node.right.parent is not node)
            )
        ):
            return False

        return self.is_BST(node.left, min, node.data, visited) and self.is_BST(
            node.right, node.data, max, visited
        )

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node  # set parent
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node  # set parent
            else:
                self._insert(data, cur_node.right)
        else:
            print("data already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.data))
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

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, cur_node):
        if data == cur_node.data:
            return cur_node
        elif data < cur_node.data and cur_node.left is not None:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right is not None:
            return self._find(data, cur_node.right)

    def delete_data(self, data):
        return self.delete_node(self.find(data))

    def delete_node(self, node):
        # Protect against deleting a node not found in the tree
        if node is None or self.find(node.data) is None:
            print("Node to be deleted not found in the tree!")
            return None

        # returns the node with min data in tree rooted at input node
        def min_data_node(n):
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
            successor = min_data_node(node.right)

            # copy the inorder successor's data to the node formerly
            # holding the data we wished to delete
            node.data = successor.data

            # delete the inorder successor now that it's data was
            # copied into the other node
            self.delete_node(successor)

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left is not None:
            return self._search(data, cur_node.left)
        elif data > cur_node.data and cur_node.right is not None:
            return self._search(data, cur_node.right)
        return False

    def __repr__(self):
        if not self.root:
            return "Empty"
        visited = set()
        visited.add(self.root)
        return self.to_str(self.root, visited, "")

    def to_str(self, node, visited, indent):
        str_rep = ""
        indent2 = "      "

        if node is None:
            return indent + "-->" + "None\n"

        str_rep += self.to_str(node.right, visited, indent + indent2)
        str_rep += indent + "-->" + node.__repr__()
        str_rep += self.to_str(node.left, visited, indent + indent2)
        return str_rep
