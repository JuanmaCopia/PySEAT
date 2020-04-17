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
        self.s_data = data
        self.s_right = None
        self.s_left = None

        self._data_is_initialized = False
        self._right_is_initialized = False
        self._left_is_initialized = False

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    @property
    def data(self):
        return self._engine.lazy_initialization(self, "data")

    @data.setter
    def data(self, value):
        return self._engine.lazy_set_attr(self, "data", value)

    @property
    def right(self):
        return self._engine.lazy_initialization(self, "right")

    @right.setter
    def right(self, value):
        return self._engine.lazy_set_attr(self, "right", value)

    @property
    def left(self):
        return self._engine.lazy_initialization(self, "left")

    @left.setter
    def left(self, value):
        return self._engine.lazy_set_attr(self, "left", value)

    def repok(self):
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
    def __init__(self):
        self.s_root = None

        self._root_is_initialized = False

        self._identifier = self.__class__.__name__.lower() + str(self._id)
        self.__class__._id += 1
        self._recursion_depth = 0

    @property
    def root(self):
        return self._engine.lazy_initialization(self, "root")

    @root.setter
    def root(self, value):
        return self._engine.lazy_set_attr(self, "root", value)

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

    def insert(self, data: int):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("data already in tree!")

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
