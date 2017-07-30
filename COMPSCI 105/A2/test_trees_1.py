"""Performs some tests on the test_tree function implemented in Stage 1.

Run this file to test the function. Check the output for results.

Variables used in this file:
tree0: Same tree as the one specified in Stage 1 of the assignment.
tree6: Same as tree0, except that the value of the root is 3.

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


def test_tree(tree):
    """Returns the particular tree.

    >>> tree0 = trees.test_tree(2)
    >>> tree0.get_value()
    2
    >>> tree0.get_left_subtree().get_value()
    31
    >>> tree0.get_right_subtree().get_value()
    5
    >>> tree0.get_left_subtree().get_right_subtree()
    >>> print(tree0)
    2---+
    (l)   31---+
    (l)       27---+
    (r)   5---+
    (r)       1---+
    (l)           7---+
    >>> tree6 = trees.test_tree(3)
    >>> tree6.get_value()
    3
    """
    return trees.test_tree(tree)


results = doctest.testmod()
if not results.failed:
    print("1 items passed all tests:\n"
          "   8 tests in __main__.test_tree\n"
          "8 tests in 4 items.\n"
          "8 passed and 0 failed.\n"
          "Test passed.")
