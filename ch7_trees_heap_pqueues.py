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

PRIORITY QS AND BINARY HEAPS
    -priority queue: a priority queue is similar to queue in that you remove from the front, but the order that items 
    are stored in the queue is determined by their priority (highest in front, lowest in back)

    -binary heaps and priority queue: to avoid the cost sorting and inserting we implement priority queues with binary heaps

    -complete binary tree: an otherwise binary tree that has all of its levels filled out with the possible
    exception of the bottom level

    -heap order property: parent key is always smaller or equal to the key of the children

BINARY SEARCH TREES:
    - bst property: keys less than parent are left child, greater than are right child
    - 

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

'''building from scratch: Node and BinarySearchTree'''

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

# main()
    
'''priority queue and binary heap'''

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        '''it is easy enough to add next to the proper place in the tree and maintain
        completeness, however, this will often disrupt the heap order rule, so we will
        need to perform a swap operation on most inserts when they violate heap order
       the swapping will be done in another function that will percolate up the mis-
       placed item''' 

        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)
    
    def percolate_up(self, i): # i: index is self.current_size + 1s
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2 ] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            minchild = self.minchild(i)
            if self.heap_list[i] > self.heap_list[minchild]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[minchild]
                self.heap_list[minchild] = tmp
            i = minchild

    def minchild(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 * 1

    def del_min(self):
        return_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return return_val

    def build_heap(self, list1):
        i = len(list1) // 2
        self.current_size = len(list1)
        self.heap_list = [0] + list1[:]
        while (i > 0):
            self.percolate_down(i)
            i = i - 1

def heap_main():
    bh = BinaryHeap()
    bh.build_heap([9,5,6,2,3])
    bh.insert(1)
    bh.insert(4)
    bh.insert(99)
    bh.insert(100)

    index = 1
    init_len = len(bh.heap_list)
    while index < init_len:
        print(index, bh.del_min())
        index += 1

# heap_main()

'''Binary Search Tree'''
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        '''use of optional parameters: we can either pass in only key/val or we can additionally send
        in references to parents and children'''

        self.key = key
        self.payload = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self): # this returns a bool
        return self.parent and self.parent.left == self

    def is_right(self): # this returns a bool
        return self.parent and self.parent.right == self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.left or self.right)
    
    def has_any_children(self):
        return self.left or self.right
    
    def has_both_children(self):
        return self.left and self.right
    
    def replace_node_data(self, key, value, left, right):
        self.key = key
        self.payload = value
        self.left = lc
        self.right = rc
        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self

    def put(self, key, val):
        '''let's us build out our bst'''
        '''if bst doesn't have a root it will create one, if it root node is already in place
        then put calls subput() to search tree in following way:
            - starting at root, search the binary tree comparing new key to the key in the current node.
            if new key is less than the current node, search left, if new key is greater, search right
            - when there is no left (or right) child, we have found the position in the tree where the new
            node should be installed
            - then, to add a node to the tree, create a new TreeNode object and insert the object at the point
            discovered in the previous step

        '''
        if self.root:
            self.subput(key, val, self.root) # makes call to subput
        else:
            self.root = TreeNode(key, val)
        
        self.size = self.size + 1
    
    def subput(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left:
                '''traverse left'''
                self.subput(key, val, current_node.left)
            else:
                '''create new node once we are finished traversing'''
                current_node.left = TreeNode(key, val, parent=current_node)
        else:
            '''traverse right'''
            if current_node.has_right():
                self.subput(key, val, current_node.right)
            else:
                current_node.right = TreeNode(key, val, parent=current_node)
    
    def __setitem__(self, key, val):
        '''we can use put() like myZipTree['Plymouth'] = 55446'''
        self.put(key, val) 

    def get(self, key): # key is what we are looking for
        '''retrieval'''
        ''' 
        
        '''
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
    
    def _get(self, key, current_node): # at first step, current_node is self.root
        if not current_node:
            return None
        elif current_node.key == key: # does current_node.key match?
            return current_node
        elif key < current_node: # is key less than current_node? speed comes from here. traverse down until we get match
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        '''most baroque functionality of bst'''
        ''' 
        steps:
        1 - find the node to delete with key
             - if more then one node, then can search using self._get() to find TreeNode that needs to be
            removed
        2 - once we find the node, we must deal with three cases:
            1: the node has no children
            2: the node has one children
            3: the node has two children

        '''
        if self.size > 1:
            node_to_remove = self._get(key, self.root) # make sure that the node we are trying to get rid of actually exists
            if node_to_remove: 
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
    
    def __delitem__(self, key):
        self.delete(key)

    def remove(self,currentNode):
        '''case A: no children'''
        if currentNode.is_leaf(): #leaf
            if current_node == current_node.parent.left:
               current_node.parent.left = None
            else:
               current_node.parent.right = None
        # case B: has both children
        elif current_node.has_both_children(): #interior
           succ = current_node.find_successor()
           succ.splice_out()
           current_node.key = succ.key
           current_node.payload = succ.payload

        else: # this node has one child
            if current_node.has_left():
                if current_node.is_left():
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right():
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:
                    current_node.replace_node_data(current_node.left.key,
                                    current_node.left.payload,
                                    current_node.left.left,
                                    current_node.left.right)
            else:
                if current_node.is_left():
                  current_node.right.parent = current_node.parent
                  current_node.parent.left = current_node.right
                elif current_node.is_right():
                   current_node.right.parent = current_node.parent
                   current_node.parent.right = currentnode.right
                else:
                   current_node.replace_node_data(current_node.right.key,
                                    current_node.right.payload,
                                    current_node.right.left,
                                    current_node.right.right)
    
    def find_successor(self):
        succ = None
        if self.has_right():
            succ = self.right.find_min()
        else:
            if self.parent:
                if self.is_left():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.find_successor()
                    self.parent.right = self
        return succ

    def find_min(self):
        current = self
        while current.has_left():
            current = current.left
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_children():
            if self.has_left():
                if self.is_left():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.left:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left():
                for item in self.left():
                    yield item
            yield self.key
            if self.has_left():
                for item in self.right():
                    yield item
        
def bst_main():
    tree = BinarySearchTree()
    tree[3] = 'red'
    tree[4] = 'blue'
    tree[6] = 'yellow'

    print(tree[3])

bst_main()