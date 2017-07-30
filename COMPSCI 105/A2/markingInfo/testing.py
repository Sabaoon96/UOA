from trees import *
# ====================== code to test assignments ========================= 

def mblist_to_tree(List):
    sz = len(List)
    List = [0] + List
    if List[sz] == 'end':
        List = List[:sz]
    tree_root = RefBinaryTree(List[1])
    queue = [(tree_root, 1, List[1])]
    queue = mbsublist_to_tree(List, queue)
    return tree_root

def mbsublist_to_tree(List, queue):
    if len(queue) > 0:
        parent, p_index, p_value = queue[0][0], queue[0][1], queue[0][2]
        queue = queue[1:]
        l_ndx = 2 * p_index
        r_ndx = l_ndx + 1
        if l_ndx < len(List):
            l_val = List[l_ndx]
        else:
            l_val = None
        if r_ndx < len(List):
            r_val = List[r_ndx]
        else:
            r_val = None
        if l_val:
            parent.insert_left(l_val)
            queue = queue + [(parent.left, l_ndx, l_val)]
        if r_val:
            parent.insert_right(r_val)
            queue = queue + [(parent.right, r_ndx, r_val)]
        queue = mbsublist_to_tree(List, queue)
    return queue


def mbtree_to_list(tree):
    # traverse the tree passing along the appropriate index
    # for the list, will need a help function subtree to list
    List = [0] + [None] * (2 ** (tree.height() + 1) - 1) + ['end']
    mbsubtree_to_list(tree, 1, List)
    return List[1:]

def mbsubtree_to_list(subtree, list_index, List):
    List[list_index] = subtree.get_value()
    if subtree.left:
        mbsubtree_to_list(subtree.left, 2 * list_index, List)
    if subtree.right:
        mbsubtree_to_list(subtree.right, 1 + 2 * list_index, List)
    



def display_tree(tree):
    str_tree = string_tree(tree, "  ")
    print(str_tree)

def string_tree(tree, indent):
    info = str(tree.key) + '---+'

    if not tree.left == None:
        info += '\n(l)' + indent + string_tree(tree.left, indent + '    ')
    if not tree.right == None:
        info += '\n(r)' + indent + string_tree(tree.right, indent +  '    ')
    return info  


# ============================ The assignment solution: a sample implementation ===========

