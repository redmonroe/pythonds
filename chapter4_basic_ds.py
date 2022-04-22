'''
source: https://runestone.academy/ns/books/published//pythonds/BasicDS/toctree.html

linear data structures: 
    - once at item is added it remains in that position relative to the other elements that come before or after

data types in focus: 
    - deque
    - stack(LIFO): ordered collection, addition & removal of items takes place at same end(top) cf 'base' is bottom4
        - stacks are how you think about browser history and probably UNDO button
    - queue
    - list
    - linked list

pre-fix, infix, postfix notations

when is a stack/queue/deque the appropriate data structure? 
- 


'''

def implement_ADT_queue_deque():
    '''
    Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.

    push(item) adds a new item to the top of the stack. It needs the item and returns nothing.

    pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

    peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

    isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.

    size() returns the number of items on the stack. It needs no parameters and returns an integer.
    '''

    pass

class Stack:

    def __init__(self):
        self.items = []

st = Stack()
breakpoint()