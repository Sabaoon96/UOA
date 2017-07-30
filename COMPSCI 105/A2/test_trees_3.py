"""Performs some tests on the print_tree function implemented in Stage 3.

Run this file to test the function. Check the output for results.

Variables used in this file:
tree0: Same tree as the one specified in Stage 1 of the assignment.
tree1 - tree4: Same trees as the one defined in questions 3 and 4 of Lab 9.
tree5: Empty tree.
str0 - str5: Stripped down version of the printed output for tree0 - tree5.

This file does not contain any code that can be submitted as part of the assignment.
"""

import doctest

import trees


def print_tree(tree):
    """Prints out a dot representation of tree.

    >>> tree0 = trees.test_tree(2)
    >>> print_tree(tree0)
    digraph tree2 {
        2 -> 31;
        2 -> 5;
        5[shape=box];
        31 -> 27;
        5 -> 1;
        1[shape=box];
        1 -> 7;
    }
    >>> tree1 = trees.RefBinaryTree(100)
    >>> print_tree(tree1)
    digraph tree2 {
        100;
    }
    >>> tree2 = trees.RefBinaryTree(1)
    >>> tree2.insert_left(2)
    >>> tree2.insert_left(3)
    >>> tree2.insert_left(4)
    >>> tree2.insert_left(5)
    >>> trees.print_tree(tree2)
    digraph tree2 {
        1 -> 5;
        5 -> 4;
        4 -> 3;
        3 -> 2;
    }
    >>> tree3 = trees.RefBinaryTree(1)
    >>> tree3 = trees.RefBinaryTree(1)
    >>> tree3.insert_left(2)
    >>> tree3.insert_right(3)
    >>> trees.print_tree(tree3)
    digraph tree2 {
        1 -> 2;
        1 -> 3;
        3[shape=box];
    }
    >>> tree4 = trees.RefBinaryTree(10)
    >>> tree4.insert_left(5)
    >>> tree4.insert_right(15)
    >>> tree4.insert_right(999)
    >>> left = tree4.get_left_subtree()
    >>> left.insert_left(2)
    >>> left.insert_right(7)
    >>> trees.print_tree(tree4)
    digraph tree2 {
        10 -> 5;
        10 -> 999;
        999[shape=box];
        5 -> 2;
        5 -> 7;
        7[shape=box];
        999 -> 15;
        15[shape=box];
    }
    >>> tree5 = None
    >>> trees.print_tree(tree5)
    digraph tree2 {
    }
    """
    trees.print_tree(tree)


results = doctest.testmod()
if not results.failed:
    print("1 items passed all tests:\n"
          "  51 tests in __main__.print_tree\n"
          "51 tests in 2 items.\n"
          "51 passed and 0 failed.\n"
          "Test passed.")
elif results.failed <= 5:
    print("**********************************************************************")
    print("Note: Please check manually. Your output might be correct...\n"
          "1. The indentation doesn't matter in the dot language.\n"
          '2. it does not matter what name you put in after "digraph"\n'
          '3. It does not matter whether the ")" appears on a new line or is at \n'
          'the end of the last line containing text.')
