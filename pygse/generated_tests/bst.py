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

def find_test1():
    '''
    Self:
      -->None
-->0
      -->None

    Return:
0

    '''
    # Input Generation
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node0.left = None
    node0.parent = None
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Assertions
    assert returnv.data == 0
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    print('Test1: OK')


def find_test2():
    '''
    Self:
      -->None
-->0
            -->None
      -->-1
            -->None

    Return:
-1

    '''
    # Input Generation
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node0.parent = None
    node1 = Node(-1)
    node1.data = -1
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(-1)
    # Assertions
    assert returnv.data == -1
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 0
    assert bst0.root.left.data == -1
    print('Test2: OK')


def find_test6():
    '''
    Self:
      -->None
-->0
            -->None
      -->-1
            -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(0)
    node0.data = 0
    node0.right = None
    node0.parent = None
    node1 = Node(-1)
    node1.data = -1
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.left.data == 1
    assert bst0.root.left.left is None
    print('Test6: OK')


def find_test7():
    '''
    Self:
      -->None
-->1
                  -->None
            -->0
                  -->None
      -->-1
            -->None

    Return:
0

    '''
    # Input Generation
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node0.parent = None
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.parent = node1
    node1.right = node2
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Assertions
    assert returnv.data == 0
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.left.data == -1
    assert bst0.root.left.right.data == 0
    print('Test7: OK')


def find_test8():
    '''
    Self:
      -->None
-->2
                  -->None
            -->1
                  -->None
      -->-1
            -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(2)
    node0.data = 2
    node0.right = None
    node0.parent = None
    node1 = Node(-1)
    node1.data = -1
    node1.left = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node2.left = None
    node2.parent = node1
    node1.right = node2
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.left.data == -1
    assert bst0.root.left.right.data == 1
    assert bst0.root.left.right.left is None
    print('Test8: OK')


def find_test9():
    '''
    Self:
      -->None
-->1
                  -->None
            -->-1
                  -->None
      -->-2
            -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node0.parent = None
    node1 = Node(-2)
    node1.data = -2
    node1.left = None
    node2 = Node(-1)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.parent = node1
    node1.right = node2
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.left.data == -1
    assert bst0.root.left.right.data == -1
    assert bst0.root.left.right.right is None
    print('Test9: OK')


def find_test10():
    '''
    Self:
      -->None
-->1
            -->None
      -->-1
            -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node0.parent = None
    node1 = Node(-1)
    node1.data = -1
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.left = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.left.data == -1
    assert bst0.root.left.right is None
    print('Test10: OK')


def find_test11():
    '''
    Self:
      -->None
-->1
      -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(1)
    node0.data = 1
    node0.right = None
    node0.left = None
    node0.parent = None
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == 1
    assert bst0.root.left is None
    print('Test11: OK')


def find_test12():
    '''
    Self:
            -->None
      -->0
            -->None
-->-1
      -->None

    Return:
0

    '''
    # Input Generation
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node0.parent = None
    node1 = Node(0)
    node1.data = 0
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Assertions
    assert returnv.data == 0
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right.data == 0
    print('Test12: OK')


def find_test13():
    '''
    Self:
            -->None
      -->1
                  -->None
            -->0
                  -->None
-->-1
      -->None

    Return:
0

    '''
    # Input Generation
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node0.parent = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(0)
    node2.data = 0
    node2.right = None
    node2.left = None
    node2.parent = node1
    node1.left = node2
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    returnv = bst0.find(0)
    # Assertions
    assert returnv.data == 0
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right.data == 1
    assert bst0.root.right.left.data == 0
    print('Test13: OK')


def find_test14():
    '''
    Self:
            -->None
      -->2
                  -->None
            -->1
                  -->None
-->-1
      -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node0.parent = None
    node1 = Node(2)
    node1.data = 2
    node1.right = None
    node2 = Node(1)
    node2.data = 1
    node2.right = None
    node2.left = None
    node2.parent = node1
    node1.left = node2
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right.data == 1
    assert bst0.root.right.left.data == 1
    assert bst0.root.right.left.left is None
    print('Test14: OK')


def find_test15():
    '''
    Self:
            -->None
      -->1
                  -->None
            -->-1
                  -->None
-->-2
      -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(-2)
    node0.data = -2
    node0.left = None
    node0.parent = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node2 = Node(-1)
    node2.data = -1
    node2.right = None
    node2.left = None
    node2.parent = node1
    node1.left = node2
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right.data == 1
    assert bst0.root.right.left.data == -1
    assert bst0.root.right.left.right is None
    print('Test15: OK')


def find_test16():
    '''
    Self:
            -->None
      -->1
            -->None
-->-1
      -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(-1)
    node0.data = -1
    node0.left = None
    node0.parent = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right.data == 1
    assert bst0.root.right.left is None
    print('Test16: OK')


def find_test20():
    '''
    Self:
            -->None
      -->1
            -->None
-->0
      -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(0)
    node0.data = 0
    node0.left = None
    node0.parent = None
    node1 = Node(1)
    node1.data = 1
    node1.right = None
    node1.left = None
    node1.parent = node0
    node0.right = node1
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right.data == -1
    assert bst0.root.right.right is None
    print('Test20: OK')


def find_test21():
    '''
    Self:
      -->None
-->-1
      -->None

    Return:
None
    '''
    # Input Generation
    node0 = Node(-1)
    node0.data = -1
    node0.right = None
    node0.left = None
    node0.parent = None
    bst0 = BST(node0)
    bst0.root = node0
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root.data == -1
    assert bst0.root.right is None
    print('Test21: OK')


def find_test22():
    '''
    Self:
Empty
    Return:
None
    '''
    # Input Generation
    bst0 = BST(None)
    bst0.root = None
    # Repok check
    assert bst0.repok()
    # Method call
    bst0.find(0)
    # Assertions
    # Repok check
    assert bst0.repok()
    assert bst0.root is None
    print('Test22: OK')


if __name__ == "__main__":
    find_test1()
    find_test2()
    find_test6()
    find_test7()
    find_test8()
    find_test9()
    find_test10()
    find_test11()
    find_test12()
    find_test13()
    find_test14()
    find_test15()
    find_test16()
    find_test20()
    find_test21()
    find_test22()
#     bst = BST()
#     bst.insert(10)
#     bst.insert(19)
#     bst.insert(15)
#     bst.insert(12)
#     bst.insert(6)
#     bst.insert(1)
#     bst.insert(18)
#     bst.insert(2)
#     bst.insert(7)
#     bst.insert(9)

#     print(bst.__repr__())
#     if bst.repok():
#         print("ES BST")
#     else:
#         print("NO ES BST")

#     node = bst.find(2)

#     toadd = Node(5)
#     toadd.parent = None
#     node.right = toadd

#     # node.parent = Node(29)

#     if bst.repok():
#         print("ES BST")
#     else:
#         print("NO ES BST")

#     print(bst.__repr__())

#     bst = BST()
#     bst.insert(1)
#     bst.insert(2)
#     bst.insert(3)
#     bst.insert(4)
#     bst.insert(5)
#     bst.insert(6)
#     bst.insert(7)
#     bst.insert(8)
#     bst.insert(9)
#     bst.insert(10)
#     print(bst.__repr__())
#     if bst.repok():
#         print("ES BST")
#     else:
#         print("NO ES BST")
