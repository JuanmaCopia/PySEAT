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

    @staticmethod  # pragma: no mutate
    def calc_height(node):  # pragma: no cover
        if node is None:  # pragma: no mutate
            return 0  # pragma: no mutate
        return 1 + max(  # pragma: no mutate
            AVLTree.calc_height(node.left_child),  # pragma: no mutate
            AVLTree.calc_height(node.right_child),  # pragma: no mutate
        )  # pragma: no mutate

    @staticmethod  # pragma: no mutate
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
