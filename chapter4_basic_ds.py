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
    ''' we are treating the bottom of the stack as the 'last in' point so that we can use constant time operations append and pop()'''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        fo = self.items.pop()
        return fo

    def peek(self):
        try:
            return self.items[len(self.items)-1]
        except IndexError as e:
            print(e, 'peek method does not work on empty stack')

    def is_empty(self):
        if len(self.items):
            return False
        else:
            return True

    def size(self):
        return len(self.items)

    def revstring(self, mystr):
        for l in mystr:
            self.push(l)

        for i in range(len(self.items)):
            it = self.items.pop()
            self.items.append(it)


    # def __str__(self):
    #     return self.items

    def erase_this_line(self):
        ''' just get rid of indent to run'''
        st = Stack()
        st.push('5')
        fo = st.pop()
        print('pop', fo)
        st.push(10)
        fo = st.peek()
        print('peek', fo)
        bool1 = st.is_empty()
        print('is_empty', bool1)
        fo = st.pop()
        print('pop another one off the top')
        bool1 = st.is_empty()
        print('is_empty', bool1)
        print('size', st.size())

        st2 = Stack()
        st2.revstring('fuckyou')
        print(''.join(st2.items))

def balanced_parens_simple():
    '''using stack with maths'''
    pass

empty_test = ''
first_test = '()'
fail_test = '(()'
fail2_test = '(()()()()()()'
hard_test = '(()(())())'

def paren_checker(test=None):
    s = Stack()
    balanced = True
    index = 0
    while index < len(test) and balanced:
        symbol = test[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1


    if balanced and s.is_empty():
        return True
    else:
        return False

answer = paren_checker(test=hard_test)
assert answer == True
answer = paren_checker(test=first_test)
assert answer == True
answer = paren_checker(test=fail_test)
assert answer == False
# print(paren_checker(test=fail2_test))
# print(paren_checker(test=empty_test))

def stack_converting_decimal_to_binary():
    pass

def decimal_to_binary(dec_number=None):
    # keep dividing by two until we get to 0
    s = Stack()
    while dec_number > 0:
        check = dec_number % 2
        s.push(check)
        dec_number = dec_number // 2
        # print(f'dividing {dec_number}: check=', check)

    binary_string = []
    for i in range(len(s.items)):
        item = s.items.pop()
        binary_string.append(str(item))

    # print(binary_string)

    return ''.join(binary_string)

for dec in range(500):
    bin_str = decimal_to_binary(dec)
    print(f'the binary value of {dec} = {bin_str}')
    
assert decimal_to_binary(233) == '11101001'
assert decimal_to_binary(100) == '1100100'
# breakpoint()
# breakpoint()