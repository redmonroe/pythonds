'''trees'''
'''
CS trees unlike reg trees: root at top, leaves at bottom
tree terms:
    - node: fundamental part of tree, referred to by its 'key', value of node is 'payload'
    - edge: an edge connects two nodes to show there is a relationship between them
    - root: only node with NO incoming edges : (
    - path: ordered list of nodes connected by edges
    - children: set of nodes c that have incoming edges from the same node are said to be children of that node
    - parent: a node is parent to all nodes it is connected to by outgoing edges
    - sibling: nodes in a tree that are children of same parent
    - subtree: a set of edges and nodes comprised of an arbitrary parent and all of its children
    - level: the level of node n is the number of edges on the path from root node to n. level of root node is 0
    - height: equal to maximum level of any node in the tree, the lowest node (lol, this is not named right)

2 definitions of a tree:
    - definition 1: 
        - a tree is a set of nodes and a set of edges that connect pairs of nodes with the following properties:    
            - one node of tree is a root node
            - every node, except root, has a parent
            - a unique path traverses from root to node
        - if each node in the tree has a max of 2 children, this is a BINARY TREE
    - definition 2: recursive definition
        - a tree is either empty or consists of a root and zero or more subtrees
'''

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
''' binary tree: first'''
def BinaryTree(r):
    return [r, [], []] # constructs a list with root node r, and two empty sublists for the children

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t)  > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch], [], [])
    return root