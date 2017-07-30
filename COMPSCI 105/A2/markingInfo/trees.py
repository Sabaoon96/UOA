""" 
Sabaoon Raza Khan - skha787 | COMPSCI105 A2
"""

#---------------------------------------------------------------------------------
# Stage 1 ->

class RefBinaryTree:

	def __init__(self, data, left = None, right = None):
		self.key = data
		self.left = left
		self.right = right

	def insert_left(self, data):
		self.left = RefBinaryTree(data, left=self.left)  

	def insert_right(self, data):
		self.right = RefBinaryTree(data, right=self.right)

	def get_left_subtree(self):
		return self.left

	def get_right_subtree(self):
		return self.right

	def set_value(self, val):
		self.key = val

	def get_value(self):
		return self.key

	def create_string(self, indent):
		string = str(self.key) + '---+'
		if self.left:
			string += '\n(l)' + indent + self.left.create_string(indent + '    ')
		if self.right:
			string += '\n(r)' + indent + self.right.create_string(indent + '    ')
		return string

	def __str__(self):
		return self.create_string('  ')
	
#---------------------------------------------------------------------------------		
# Stage 1 ->
		
def test_tree(tree):
	t = RefBinaryTree(tree) 
	t.insert_left(31)
	t.insert_right(5)
	t.get_left_subtree().insert_left(27)
	t.get_right_subtree().insert_right(1)
	t.get_right_subtree().get_right_subtree().insert_left(7)
	return t

#---------------------------------------------------------------------------------
# Stage 2 ->	
	
def tree_to_list(tree):
    if tree is None:
        return ['end']
    else:	
        treeList = []
        data = [tree]
        while data:
            duplicate = data[:]
            data = []
            for item in duplicate:
                if item:
                    treeList.append(item.key)
                    data.append(item.left)
                    data.append(item.right)
                else:
                    treeList.append(None)
                    data.append(None)
                    data.append(None)
            if all((value is None for value in data)):
                treeList.append('end')
                break
        return treeList

def list_to_tree_helper(tree, list, index):
    if list[index * 2]:
        tree.insert_left(list[index * 2])
    if list[index]:
        if index * 4 < len(list):
            list_to_tree_helper(tree.get_left_subtree(), list, index * 2)
    if list[(index * 2) + 1]:
        tree.insert_right(list[(index * 2) + 1])
    if list[index]:
        if index * 4 < len(list):
            list_to_tree_helper(tree.get_right_subtree(), list, (index * 2) + 1)
	
def list_to_tree(list):
    if len(list) == 1:
        return None
    if len(list) == 2:
        tree = RefBinaryTree(list[0])
        return tree
    else:		
        tree = RefBinaryTree(list[0])
        list.insert(0, None)
        list.pop()
        list_to_tree_helper(tree, list, 1)
        return tree
		
#---------------------------------------------------------------------------------
# Stage 3 ->

def print_tree(tree):
    list = tree_to_list(tree)
    print("digraph tree2 {")
    if len(list) == 2:
        if list[0]:
            print("    ", list[0], ";", sep="")
    for index in range(0, len(list)//2 - 1):
        parent = list[index]
        left_child = list[index*2+1]
        right_child = list[index*2+2]		
        if (parent and left_child):		
            print("    ", parent, " -> ", left_child, ";", sep="")
        if (parent and right_child):
            print("    ", parent, " -> ", right_child, ";", sep="")
        if right_child:
            print("    ", right_child, "[shape=box];", sep="")
    print("}")	

#---------------------------------------------------------------------------------