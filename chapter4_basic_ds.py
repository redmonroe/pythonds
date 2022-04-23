'''
source: https://runestone.academy/ns/books/published//pythonds/BasicDS/toctree.html

linear data structures: 
    - once at item is added it remains in that position relative to the other elements that come before or after

data types in focus: 
    - deque
    - stack(LIFO): ordered collection, addition & removal of items takes place at same end(top) cf 'base' is bottom4
        - stacks are how you think about browser history and probably UNDO button
    - queue(FIFO): ordered collection (based on a list), addition happens at one end (the rear), removal at the other end (the front), items added wait their turn to be removedq
    - list
    - linked list

pre-fix, infix, postfix notations
    - infix notation: when the operator appears between the operands: B x C, 10 * 12, 1 + 2
    - prefix: operator before operands: x BC, * 10 12, + 1 2
    - postfix: operator after: BC x, 10 12 *, 1 2 +
    - neither post or pre needs parentheses to determine which operation goes first

    A + B * C, would be pre => + A * B C  or post => A B C * +

    more examples (a = 2, b=5, c=10, d=11) 63 is the answer
    in                      pre                      post
    A + B * C + D           + + A * B C D            A B C * + D +

order of operations PEMDAS is one way to address ambiguity of which operations goes first
fully parenthesized expressions are another; post and prefix yet another


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

class Queue:
    '''what constant time efficiencies can I find?'''
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        try:
            return self.items.pop()
        except IndexError as e:
            print(f'{self} is empty with error {e}')

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

qq = Queue()
qq.enqueue('4')
assert qq.items == ['4']
assert qq.size() == 1
assert qq.is_empty() == False
r = qq.dequeue()
assert r == '4'

name_list = ['fred', 'tori', 'monica', 'aj', 'daniella', 'hole', 'seaperson', 'alexandria', 'tes', 'billmon', 'artemis', 'arlemustus', 'frangelico', 'dean', 'hard', 'jelson', 'ask', 'prentices', 'larman', 'alejendron', 'fellt', 'crg', 'carg', 'larg', 'brenno', 'able', 'john', 'pila', 'baxter', 'frienddzz']

def hot_potato(name_list, num):
    print(f'{name_list[0]} has the hot potato. Let us play the game')

    reset_num = num
    qq = Queue()
    for name in name_list:
        qq.enqueue(name)

    # print('size:', qq.size())
    
    while qq.size() > 1:
        # print('size:', qq.size())
        popped_name = qq.dequeue()
        qq.enqueue(popped_name)
        num = num - 1
        # print('num:', num)
        # breakpoint()
        if num == 0:
            popped_name = qq.dequeue()
            num = reset_num
    # print(qq.items)
    return qq.items


final_boy = hot_potato(name_list, 6)
assert final_boy == ['carg']
# breakpoint()
assert hot_potato(name_list, 10)[0] == 'pila'



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
    s = Stack()
    while dec_number > 0:
        check = dec_number % 2
        s.push(check)
        dec_number = dec_number // 2

    binary_string = []
    for i in range(len(s.items)):
        item = s.items.pop()
        binary_string.append(str(item))

    return ''.join(binary_string)

# for dec in range(500):
#     bin_str = decimal_to_binary(dec)
#     print(f'the binary value of {dec} = {bin_str}')

assert decimal_to_binary(233) == '11101001'
assert decimal_to_binary(100) == '1100100'

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while dec_number > 0:
        check = dec_number % base
        s.push(check)
        dec_number = dec_number // base

    newString = ""
    while not s.is_empty():
        newString = newString + digits[s.pop()]

    return newString

# print(base_converter(26,26))
# print(base_converter(256,16))

def notation_algos():
    pass

sample_infix = '( A + B )'
sample_infix = "A * B + C * D"
sample_infix = '( A + B ) * ( C + D )'
sample_infix = "( A + B ) * C" # = A B + C *
sample_infix = "A + B * C" # = A B C * +

sample_infix = '9 + 3 * 5 / ( 1 - 4 )' # = 9 3 5 1 4 - * / +

def convert_to_postfix(infix=None):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    rator = Stack() # opstack
    post_fix_notation = []
    infix = infix.split()

    for l in infix:
        if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or l in "0123456789":
            post_fix_notation.append(l)
        elif l == '(':
            rator.push(l)
        elif l == ')':
            top_token = rator.pop() # this pops the + in A + B, the ) is the signal
            while top_token != '(': #
                post_fix_notation.append(top_token)
                top_token = rator.pop()
        else:
            while (not rator.is_empty()) and (prec[rator.peek()] >= prec[l]):
                post_fix_notation.append(rator.pop())
            rator.push(l)

    while not rator.is_empty():
        post_fix_notation.append(rator.pop())
    return ' '.join(post_fix_notation)

# print(convert_to_postfix(infix=sample_infix))

sample_postfix = '4 5 6 * +'
def evaluate_postfix(postfix=None):
    # single digit integer values only

    def do_math(operator, first_rand, second_rand):
        if operator == '*':
            return first_rand * second_rand
        elif operator == '/':
            return first_rand / second_rand
        elif operator == '+':
            return first_rand + second_rand
        else:
            return first_rand - second_rand

    # what are we attempting to do here?  target value is: 34
    operand_stack = Stack()
    for l in postfix.split(' '):
        if l in "0123456789":
            # place 4, 5, 6 on the stack
            operand_stack.push(l)
        elif l in '*/+-':
            # preserve order carefully in case of division
            second_token = int(operand_stack.pop())
            first_token = int(operand_stack.pop())
            result = do_math(l, first_token, second_token)
            # print(f'{first_token} {l} {second_token} = {result}')
            operand_stack.push(result)

    return operand_stack.pop()



answer = evaluate_postfix(postfix=sample_postfix)
assert answer == 34
assert evaluate_postfix(postfix='7 8 + 3 2 + /') == 3
answer = convert_to_postfix(infix='5 * 3 ** ( 4 - 2 )')