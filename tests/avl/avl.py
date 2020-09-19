import sys


def do_add(s, x):  # pragma: no cover
    length = len(s)  # pragma: no mutate
    s.add(x)  # pragma: no mutate
    return len(s) != length  # pragma: no mutate


class node:
    # Instance attributes annotations (will be treated as symbolic)
    value: int
    height: int
    right_child: "node"
    left_child: "node"
    parent: "node"

    def __init__(self, value: int = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree
        self.height = 1  # height of node in tree (max dist. to leaf) NEW FOR AVL


class AVLTree:
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
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")  # pragma: no mutate

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
            print("Node to be deleted not found in the tree!")  # pragma: no mutate
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

            # exit function so we don't call the _inspect_deletion twice
            return

        if node_parent != None:
            # fix the height of the parent of current node
            node_parent.height = 1 + max(
                self.get_height(node_parent.left_child),
                self.get_height(node_parent.right_child),
            )

            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)

    # Functions added for AVL...

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent == None:
            return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left_child)
        right_height = self.get_height(cur_node.parent.right_child)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):
        if cur_node == None:
            return

        left_height = self.get_height(cur_node.left_child)
        right_height = self.get_height(cur_node.right_child)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)
        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)
        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception("_rebalance_node: z,y,x node configuration not recognized!")

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3 != None:
            t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(
            self.get_height(z.left_child), self.get_height(z.right_child)
        )
        y.height = 1 + max(
            self.get_height(y.left_child), self.get_height(y.right_child)
        )

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2
        if t2 != None:
            t2.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(
            self.get_height(z.left_child), self.get_height(z.right_child)
        )
        y.height = 1 + max(
            self.get_height(y.left_child), self.get_height(y.right_child)
        )

    def get_height(self, cur_node):
        if cur_node == None:
            return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left_child)
        right = self.get_height(cur_node.right_child)
        return cur_node.left_child if left >= right else cur_node.right_child

    def repok(self):  # pragma: no cover
        if not self.root:  # pragma: no mutate
            return True  # pragma: no mutate
        if not (  # pragma: no mutate
            self.is_acyclic()  # pragma: no mutate
            and self.is_ordered()  # pragma: no mutate
            and self.is_balanced()  # pragma: no mutate
            and self.parents_ok(self.root)  # pragma: no mutate
            and self.heights_ok(self.root)  # pragma: no mutate
        ):  # pragma: no mutate
            return False  # pragma: no mutate
        if self.root.parent is not None:  # pragma: no mutate
            return False  # pragma: no mutate
        return True  # pragma: no mutate

    def is_acyclic(self):  # pragma: no cover
        visited = set()  # pragma: no mutate
        visited.add(self.root)  # pragma: no mutate
        worklist = []  # pragma: no mutate
        worklist.append(self.root)  # pragma: no mutate
        while worklist:  # pragma: no mutate
            current = worklist.pop(0)  # pragma: no mutate
            if current.left_child:  # pragma: no mutate
                if not do_add(visited, current.left_child):  # pragma: no mutate
                    return False  # pragma: no mutate
                worklist.append(current.left_child)  # pragma: no mutate
            if current.right_child:  # pragma: no mutate
                if not do_add(visited, current.right_child):  # pragma: no mutate
                    return False  # pragma: no mutate
                worklist.append(current.right_child)  # pragma: no mutate
        return True  # pragma: no mutate

    def is_ordered(self):  # pragma: no cover
        return self.is_ordered2(  # pragma: no mutate
            self.root, -sys.maxsize, sys.maxsize  # pragma: no mutate
        )  # pragma: no mutate

    def is_ordered2(self, node, min, max):  # pragma: no cover
        if node.value <= min or node.value >= max:  # pragma: no mutate
            return False  # pragma: no mutate
        if node.left_child:  # pragma: no mutate
            if not self.is_ordered2(  # pragma: no mutate
                node.left_child, min, node.value  # pragma: no mutate
            ):  # pragma: no mutate
                return False  # pragma: no mutate
        if node.right_child:  # pragma: no mutate
            if not self.is_ordered2(  # pragma: no mutate
                node.right_child, node.value, max  # pragma: no mutate
            ):  # pragma: no mutate
                return False  # pragma: no mutate
        return True  # pragma: no mutate

    def parents_ok(self, node):  # pragma: no cover
        if node is None:  # pragma: no mutate
            return True  # pragma: no mutate

        if node.left_child is not None:  # pragma: no mutate
            if node.left_child.parent is not node:  # pragma: no mutate
                return False  # pragma: no mutate

        if node.right_child is not None:  # pragma: no mutate
            if node.right_child.parent is not node:  # pragma: no mutate
                return False  # pragma: no mutate

        return self.parents_ok(  # pragma: no mutate
            node.left_child  # pragma: no mutate
        ) and self.parents_ok(  # pragma: no mutate
            node.right_child  # pragma: no mutate
        )  # pragma: no mutate

    def is_balanced_helper(self, root):  # pragma: no cover
        if root is None:  # pragma: no mutate
            return 0  # pragma: no mutate
        left_height = self.is_balanced_helper(root.left_child)  # pragma: no mutate
        if left_height == -1:  # pragma: no mutate
            return -1  # pragma: no mutate
        right_height = self.is_balanced_helper(root.right_child)  # pragma: no mutate
        if right_height == -1:  # pragma: no mutate
            return -1  # pragma: no mutate
        if abs(left_height - right_height) > 1:  # pragma: no mutate
            return -1  # pragma: no mutate
        return max(left_height, right_height) + 1  # pragma: no mutate

    def is_balanced(self):  # pragma: no cover
        return self.is_balanced_helper(self.root) > -1  # pragma: no mutate

    @staticmethod
    def calc_height(node):  # pragma: no cover
        if node is None:  # pragma: no mutate
            return 0  # pragma: no mutate
        return 1 + max(  # pragma: no mutate
            AVLTree.calc_height(node.left_child),  # pragma: no mutate
            AVLTree.calc_height(node.right_child),  # pragma: no mutate
        )  # pragma: no mutate

    @staticmethod
    def heights_ok(node):  # pragma: no cover
        if node is None:  # pragma: no mutate
            return True  # pragma: no mutate
        if AVLTree.calc_height(node) != node.height:  # pragma: no mutate
            return False  # pragma: no mutate
        return AVLTree.heights_ok(  # pragma: no mutate
            node.left_child  # pragma: no mutate
        ) and AVLTree.heights_ok(  # pragma: no mutate
            node.right_child  # pragma: no mutate
        )  # pragma: no mutate
