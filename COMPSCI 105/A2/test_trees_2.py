"""Performs some tests on some functions implemented in Stage 2.

Run this file to test the functions. Check the output for results.

Variables used in this file:
tree0: Same tree as the one specified in Stage 1 of the assignment.
tree1 - tree4: Same trees as the one defined in questions 3 and 4 of Lab 9.
tree5: Empty tree.
list0 - list5: List representations of tree0 - tree5.

This file does not contain any code that can be submitted as part of the assignment.
"""

import doctest

import trees


def create_string(self, indent):
    info = str(self.key) + "---+"
    if self.left:
        info += "\n(l)" + indent + self.left.create_string(indent + "    ")
    if self.right:
        info += "\n(r)" + indent + self.right.create_string(indent + "    ")
    return info


def __str__(self):
    representation = self.create_string("   ")
    return representation


trees.RefBinaryTree.create_string = create_string
trees.RefBinaryTree.__str__ = __str__


def tree_to_list(tree):
    """Returns a list of the tree node values.

    >>> tree0 = trees.test_tree(2)
    >>> tree_to_list(tree0)
    [2, 31, 5, 27, None, None, 1, None, None, None, None, None, None, 7, None, 'end']
    >>> tree1 = trees.RefBinaryTree(100)
    >>> tree_to_list(tree1)
    [100, 'end']
    >>> tree2 = trees.RefBinaryTree(1)
    >>> tree2.insert_left(2)
    >>> tree2.insert_left(3)
    >>> tree2.insert_left(4)
    >>> tree2.insert_left(5)
    >>> tree_to_list(tree2)
    [1, 5, None, 4, None, None, None, 3, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'end']
    >>> tree3 = trees.RefBinaryTree(1)
    >>> tree3 = trees.RefBinaryTree(1)
    >>> tree3.insert_left(2)
    >>> tree3.insert_right(3)
    >>> tree_to_list(tree3)
    [1, 2, 3, 'end']
    >>> tree4 = trees.RefBinaryTree(10)
    >>> tree4.insert_left(5)
    >>> tree4.insert_right(15)
    >>> tree4.insert_right(999)
    >>> left = tree4.get_left_subtree()
    >>> left.insert_left(2)
    >>> left.insert_right(7)
    >>> tree_to_list(tree4)
    [10, 5, 999, 2, 7, None, 15, 'end']
    >>> tree5 = None
    >>> tree_to_list(tree5)
    ['end']
    """
    return trees.tree_to_list(tree)


def list_to_tree(list):
    """Returns a tree with the list values laid out in level order.

    >>> list0 = [2, 31, 5, 27, None, None, 1, None, None, None, None, None, None, 7, None, 'end']
    >>> print(list_to_tree(list0))
    2---+
    (l)   31---+
    (l)       27---+
    (r)   5---+
    (r)       1---+
    (l)           7---+
    >>> list1 = [100, 'end']
    >>> print(list_to_tree(list1))
    100---+
    >>> list2 = [1, 5, None, 4, None, None, None, 3, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'end']
    >>> print(list_to_tree(list2))
    1---+
    (l)   5---+
    (l)       4---+
    (l)           3---+
    (l)               2---+
    >>> list3 = [1, 2, 3, 'end']
    >>> print(list_to_tree(list3))
    1---+
    (l)   2---+
    (r)   3---+
    >>> list4 = [10, 5, 999, 2, 7, None, 15, 'end']
    >>> print(list_to_tree(list4))
    10---+
    (l)   5---+
    (l)       2---+
    (r)       7---+
    (r)   999---+
    (r)       15---+
    >>> list5 = ['end']
    >>> print(list_to_tree(list5))
    None
    """
    return trees.list_to_tree(list)


results = doctest.testmod()
if not results.failed:
    print("2 items passed all tests:\n"
          "  12 tests in __main__.list_to_tree\n"
          "  25 tests in __main__.tree_to_list\n"
          "37 tests in 5 items.\n"
          "37 passed and 0 failed.\n"
          "Test passed.")
