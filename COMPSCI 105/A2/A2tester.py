from trees import *

def test_case1():
	tree = 	RefBinaryTree(1)
	tree.insert_left(2)
	tree.insert_right(3)
	print(tree)
	print(tree_to_list(tree))
	print_tree(tree)
	
def test_case2():
	tree = 	RefBinaryTree(1)
	tree.insert_left(2)
	tree.insert_right(3)
	left = tree.get_left_subtree()
	left.insert_left(4)
	left.insert_right(5)	
	print(tree)
	print(tree_to_list(tree))
	print_tree(tree)
	
def test_case3():
	tree = 	RefBinaryTree(1)
	tree.insert_left(2)
	tree.insert_right(3)
	right = tree.get_right_subtree()
	right.insert_left(6)
	right.insert_right(7)	
	print(tree)
	print(tree_to_list(tree))
	print_tree(tree)
	
def test_case4():
	tree = 	RefBinaryTree(1)
	tree.insert_left(2)
	tree.insert_right(3)
	left = tree.get_left_subtree()
	left.insert_left(4)
	right = tree.get_right_subtree()
	right.insert_right(7)	
	print(tree)
	print(tree_to_list(tree))
	print_tree(tree)
	
def test_case5():
	tree = 	RefBinaryTree(1)
	tree.insert_left(2)
	tree.insert_right(3)
	left = tree.get_left_subtree()
	left.insert_right(5)
	right = tree.get_right_subtree()
	right.insert_left(6)	
	print(tree)
	print(tree_to_list(tree))
	print_tree(tree)
	
def test_case6():
	tree = 	RefBinaryTree(1)
	tree.insert_left(2)
	tree.insert_right(3)
	left = tree.get_left_subtree()
	left.insert_right(5)
	left.insert_left(4)
	right = tree.get_right_subtree()
	right.insert_left(6)	
	right.insert_right(7)	
	print(tree)
	print(tree_to_list(tree))
	print_tree(tree)
		
def main():
	test_case1()
	test_case2()
	test_case3()
	test_case4()
	test_case5()
	test_case6()
	
main()