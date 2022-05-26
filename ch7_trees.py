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

'''nodes and references: class-based tree'''
class BinaryTree:

    def __init__(self, key):
        self.key = key 
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child== None:
            self.right_child= BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

# r = BinaryTree('a')
# print(r.get_root_val())
# print('initial_get_left_call:', r.get_left_child())
# r.insert_left('b')
# print(r.get_left_child().get_root_val())
# print(r.insert_right('c'))
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# print(r.get_right_child().set_root_val('heelo'))
# print(r.get_right_child().get_root_val())

'''parse trees'''
'''
parse trees can be used to represent real-world constructions like sentences or mathematical expressions

building a parse tree:
1) break up expression string into list of tokens
2) for math: 4 kinds of tokens:
    1) left paren
    2) right paren
    3) operators
    4) operands
3) always true:
    - we know that when we read a left paren we are starting a new expression (and we should start a new tree)
    - thus, we know if we use right paren, we have finished the expression
    - we know that operands are going to be leaf nodes and children of operators
    - we know that every operators is going to have both a left and right child
'''
from chapter4_basic_ds import Stack

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack()
    expression_tree = BinaryTree('')
    p_stack.push(expression_tree)
    current_tree = expression_tree

    for item in fp_list:
        if item == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif item in ['+', '-', '*', '/']:
            current_tree.set_root_val(item)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        
        elif item == ')':
            current_tree = p_stack.pop()

        elif item not in ['+', '-', '*', '/', ')']:
            try:
                current_tree.set_root_val(int(item))
                parent = p_stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError('token "{}" is not a valid integer'.format(item))

    return expression_tree

'''evaluating the parse tree we have built'''
'''
the following recursive function allows us to evaluate a parse tree and return a numerical result
'''
import operator

def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()

func_exp = '( 3 + 4 )'
# func_exp = '( ( 3 * 4 ) * 10 )'
parse_tree = build_parse_tree(func_exp)
print(evaluate(parse_tree))

'''tree traversals'''
'''
there are 3 commonly used patterns to access all the nodes of a tree
- preorder: root first -> recursively traverse throught left subtree -> recursively traverse through right subtree
- inorder: left subtree => root subtree => right subtree
- postorder: left => right => root
'''

from binarytree import Node

func_exp = '( 3 + 4 )'


