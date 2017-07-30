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
    treeList = []
    queue = [tree]
    while queue:
        copy = queue[:]
        queue = []
        for item in copy:
            if item is None:
                treeList.append(None)
                queue.append(None)
                queue.append(None)
            else:
                treeList.append(item.key)
                queue.append(item.left)
                queue.append(item.right)
        if all((x is None for x in queue)):
            treeList.append('end')
            break
    return treeList
	
def list_to_tree(list):
    #char a[SIZE] = {A,B,C,D,E,F,G}; 					
    #node* func(int index){								
        #if(index < SIZE){									
            #node *tmp = new node();							
            #tmp->data = a[index];								
            #tmp->left = func(2*index + 1);						
            #tmp->right = func(2*index + 2);					
        #}													
        #return tmp;
    #}
	pass
#---------------------------------------------------------------------------------
# Stage 3 ->

def print_tree(tree):
    if tree is not None:
        print(tree.get_value())
        print_tree(tree.get_left_subtree())
        print_tree(tree.get_right_subtree())

"""
digraph tree2 {
    2 -> 31 ;
    2 -> 5;
    5[shape=box];
    31 -> 27;
    5 -> 1;
    1[shape=box];
    1 -> 7; }
"""


#---------------------------------------------------------------------------------

def main(): 
    a = test_tree(2)
    print(a)
    print()
	
    b = tree_to_list(a)
    print(b)
    print()
	
    c = list_to_tree(b)
    print(c)
    print()
	
    print_tree(a)

main()