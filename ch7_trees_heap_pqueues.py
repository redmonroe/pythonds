'''trees'''
'''
BINARY TREE HAS AT MOST TWO CHILDREN AND THUS AT MOST TWO POINTERS TO THOSE CHILDREN

don't think of them in terms of generality per level, think of them as a multi-dimensional doubly-linked list, you put stuff in and you can get to it faster because you can cut off large swaths of opportunities if the storage and lookup funcs are written with parallel concern

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

priority queue: a priority queue is similar to queue in that you remove from the front, but the order that items 
are stored in the queue is determined by their priority (highest in front, lowest in back)

binary heaps and priority queue: to avoid the cost sorting and inserting we implement priority queues with binary heaps


'''

'''nodes and references: class-based tree'''
'''extension of Node class that allows pretty printing of trees'''
from binarytree import Node

class BT(Node):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left == None:
            self.left = BT(new_node)
        else:
            t = BT(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right== None:
            self.right= BT(new_node)
        else:
            t = BT(new_node)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left
    
    def set_root_val(self, obj):
        self.value = obj

    def get_root_val(self):
        return self.value

r = BT('a')
r.insert_left('b')
r.insert_left('c')
r.insert_right('10')
# print(r)
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
    expression_tree = BT('center_ph')
    p_stack.push(expression_tree)
    current_tree = expression_tree

    for item in fp_list:
        if item == '(':
            print(f'hit {item}')
            current_tree.insert_left('left_ph')
            p_stack.push(current_tree)
            print('current tree in (:', current_tree)
            current_tree = current_tree.get_left() # descent to left child

        elif item in ['+', '-', '*', '/']:
            print(f'setting {current_tree} root val to {item}')
            current_tree.set_root_val(item)
            current_tree.insert_right('right_ph') # if we have an operator, we know we already have an operand, and also that we need another operand
            print(f'\npushing {item} onto Stack')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right()
        
        elif item == ')':
            print(f'hitting {item}')
            pop_item = p_stack.pop()
            print(f'popping {pop_item} from Stack')
            current_tree = pop_item

        elif item not in ['+', '-', '*', '/', ')']:
            try:
                print('updating operand:', item)
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
    
    left_c = parse_tree.get_left()
    right_c = parse_tree.get_right()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()

# func_exp = '( 3 + 4 )'
# func_exp = '( ( ( 3 * 4 ) * 10 ) + 20 )'
# parse_tree = build_parse_tree(func_exp)
# print('\nfinal tree:', parse_tree)
# print(evaluate(parse_tree))

'''tree traversals'''
'''
there are 3 commonly used patterns to access all the nodes of a tree
- preorder: root first -> recursively traverse throught left subtree -> recursively traverse through right subtree
- inorder: left subtree => root subtree => right subtree
- postorder: left => right => root
'''

'''building from scratch: Node and BinaryTree'''

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
    
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([])) # not empty list, because we are not passing in values
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

main()
    
'''priority queue and binary heap'''


