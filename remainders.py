'''chapter 7'''

def trees_as_list_of_lists():
    my_tree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]
    print(my_tree)

# trees_as_list_of_lists()

''' binary tree: with lists of lists'''
def BinaryTree(r):
    return [r, [], []] # constructs a list with root node r, and two empty sublists for the children

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t)  > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t)  > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch], [], [])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, root_value):
    root[0] = root_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

# r = BinaryTree(3)
# insert_left(r, 4)
# insert_left(r, 5)
# insert_left(r, 6)
# insert_left(r, 7)
# left = get_left_child(r)
# print(left)
# set_root_val(left, 9)
# print(r)
# insert_left(left, 11)
# print(r)
# print(get_right_child(r))