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

    # Init params should be annotated also
    def __init__(self, data: int):
        self.data = data
        self.right = None
        self.left = None

        self._data_is_initialized = True
        self._right_is_initialized = False
        self._left_is_initialized = False

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

    def repok(self):
        return True

    def conservative_repok(self):
        return True

    def instrumented_repok(self):
        return True

    def __repr__(self):
        return self._identifier + ": " + str(self.data)


class BST:

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

    def repok(self):
        if not self.root:
            return True
        if not (self.is_acyclic() and self.is_ordered()):
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
        if node.data <= min or node.data >= max:
            return False
        if node.left:
            if not self.is_ordered2(node.left, min, node.data):
                return False
        if node.right:
            if not self.is_ordered2(node.right, node.data, max):
                return False
        return True

    def conservative_repok(self):
        if not self._root_is_initialized:
            return True
        if not self.root:
            return True
        if not (self.cons_is_acyclic() and self.cons_is_ordered()):
            return False
        return True

    def cons_is_acyclic(self):
        visited = set()
        visited.add(self.root)
        worklist = []
        worklist.append(self.root)
        while worklist:
            current = worklist.pop(0)
            if not current._left_is_initialized:
                return True
            if current.left:
                if not do_add(visited, current.left):
                    return False
                worklist.append(current.left)
            if not current._right_is_initialized:
                return True
            if current.right:
                if not do_add(visited, current.right):
                    return False
                worklist.append(current.right)
        return True

    def cons_is_ordered(self):
        return self.cons_is_ordered2(self.root, INT_MIN, INT_MAX)

    def cons_is_ordered2(self, node, min, max):
        if not node._data_is_initialized:
            return True
        if node.data <= min or node.data >= max:
            return False

        if not node._left_is_initialized:
            return True
        if node.left:
            if not self.cons_is_ordered2(node.left, min, node.data):
                return False

        if not node._right_is_initialized:
            return True
        if node.right:
            if not self.cons_is_ordered2(node.right, node.data, max):
                return False
        return True

    def instrumented_repok(self):
        if not self._get_root():
            return True
        if not (self.ins_is_acyclic() and self.ins_is_ordered()):
            return False
        return True

    def ins_is_acyclic(self):
        visited = set()
        visited.add(self._get_root())
        worklist = []
        worklist.append(self._get_root())
        while worklist:
            current = worklist.pop(0)
            if current._get_left():
                if not do_add(visited, current._get_left()):
                    return False
                worklist.append(current._get_left())
            if current._get_right():
                if not do_add(visited, current._get_right()):
                    return False
                worklist.append(current._get_right())
        return True

    def ins_is_ordered(self):
        return self.ins_is_ordered2(self._get_root(), INT_MIN, INT_MAX)

    def ins_is_ordered2(self, node, min, max):
        if node._get_data() <= min or node._get_data() >= max:
            return False
        if node._get_left():
            if not self.ins_is_ordered2(node._get_left(), min, node._get_data()):
                return False
        if node._get_right():
            if not self.ins_is_ordered2(node._get_right(), node._get_data(), max):
                return False
        return True

    def insert(self, data: int):
        if self._get_root() is None:
            self._set_root(Node(data))
        else:
            self._insert(data, self._get_root())

    def _insert(self, data, cur_node):
        if data < cur_node._get_data():
            if cur_node._get_left() is None:
                cur_node._get_left()._set_left(Node(data))
            else:
                self._insert(data, cur_node._get_left())
        elif data > cur_node._get_data():
            if cur_node._get_right() is None:
                cur_node._get_right()._set_right(Node(data))
            else:
                self._insert(data, cur_node._get_right())
        else:
            print("data already in tree!")

    def find(self, data: int):
        if self._get_root() is not None:
            return self._find(data, self._get_root())
        else:
            return None

    def _find(self, data, cur_node):
        if data == cur_node._get_data():
            return cur_node
        elif data < cur_node._get_data() and cur_node._get_left() is not None:
            return self._find(data, cur_node._get_left())
        elif data > cur_node._get_data() and cur_node._get_right() is not None:
            return self._find(data, cur_node._get_right())

    def to_str(self, node, visited):
        """Returns list of strings, width, height, and horizontal coord of root."""
        # No child.

        if node is None:
            line = "%s" % node.data + "N"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if not do_add(visited, node):
            line = "%s" % node.data + "*"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None and node.left is None:
            line = "%s" % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.to_str(node.left, visited)
            s = "%s" % node.data
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.to_str(node.right, visited)
            s = "%s" % node.data
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.to_str(node.left, visited)
        right, m, q, y = self.to_str(node.right, visited)
        s = "%s" % node.data
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

    def __repr__(self):
        if self.root is None:
            return "<empty tree>"
        visited = set()
        lines, _, _, _ = self.to_str(self.root, visited)
        result = ""
        for line in lines:
            result += "        " + line + "\n"
        return "\n" + result
