'''
source: https://runestone.academy/ns/books/published//pythonds/BasicDS/toctree.html

linear data structures: 
    - once at item is added it remains in that position relative to the other elements that come before or after

data types in focus: 
    - deque: double-ended queue, new items can be added or removed at either end, removal and addition is not enforced by this datastructure but through consistent use of addition and removal operators
    - stack(LIFO): ordered collection, addition & removal of items takes place at same end(top) cf 'base' is bottom4
        - stacks are how you think about browser history and probably UNDO button
    - queue(FIFO): ordered collection (based on a list), addition happens at one end (the rear), removal at the other end (the front), items added wait their turn to be removedq
    - list: an unordered collection of item
    - linked list: each item contains information about the NEXT item, information about the items relative positions is not located OUTSIDE of the list items, contained in NODEs

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

class Node:
    '''None: plays a special role; a reference to None indicates that there is no next node'''
    '''constructor usually shown as self.next = None'''
    '''called grounding the node'''

    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_previous(self, new_prev):
        self.prev = new_prev

    def __gt__(self, comparison):
        return self.get_data() > comparison.get_data()

    def __lt__(self, comparison):
        return self.get_data() < comparison.get_data()

    def __str__(self):
        return f'Node: {self.get_data()}'

class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        '''each item must reside in a node'''
        temp = Node(item)
        '''now, we set the "next" reference of the new Node to refer to the old first node of the list'''
        temp.set_next(self.head)
        self.head = temp

    def add2(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_data()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def is_empty(self):
        '''returns True if self.head is a reference to None'''
        '''will only be True if there are no nodes in the linked list'''
        return self.head == None

    '''linked list traversal'''
    '''traversal means systematically visiting each node'''
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
            
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def see(self):
        print_list = []
        current = self.head
        while current != None:
            print_list.append(current.get_data())
            # print(current.get_data())
            current = current.get_next() 
        print(print_list)

def test_ordered():
    ol = OrderedList()
    ol.add(1)
    ol.add(3)
    ol.add2(2)
    print('ol version 1')
    ol.see()
    print('ol2 version 2')
    ol2 = OrderedList()
    ol2.add2(1)
    ol2.add2(3)
    ol2.add2(2)
    ol2.see()



test_ordered()



class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        '''each item must reside in a node'''
        temp = Node(item)
        '''now, we set the "next" reference of the new Node to refer to the old first node of the list'''
        temp.set_next(self.head)
        self.head = temp
        self.head.set_previous(temp)

    def is_empty(self):
        '''returns True if self.head is a reference to None'''
        '''will only be True if there are no nodes in the linked list'''
        return self.head == None

    '''linked list traversal'''
    '''traversal means systematically visiting each node'''
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        found = False
        previous = None
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
            
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def see(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()            

def list_runner():
    mynode = Node('mein_nodt')
    mylist = UnorderedList()
    print('head:', mylist.head)
    mylist.add('min_list1')
    print('head:', mylist.head)
    mylist.add('min_list2')
    print('head:', mylist.head)
    mylist.add('min_list3')
    print('head:', mylist.head)
    mylist.add('min_list4')
    print('head:', mylist.head)
    print('see = >')
    mylist.see()
    print('size:', mylist.size())
    print('search:', mylist.search(100))

    print('search:', mylist.search('min_list2'))
    mylist.remove('min_list3')
    print('see ==> min_list3 removed')
    mylist.see()

# list_runner()

def building_up_ll():
    ul = UnorderedList()
    ''' ul = []'''
    assert ul.head == None
    ul.add('fucksticks')
    '''ul = [fucksticks]'''
    next1 = ul.head.get_next()
    assert next1 == None #.get_data() doesn't work here because next1 == None, ie 'end of list'
    prev1 = ul.head.get_previous()
    assert prev1 == None
    ul.add('egg_crates')
    '''ul = [fucksticks, egg_crates]'''
    assert ul.head.get_data() == 'egg_crates'
    assert ul.head.get_next().get_data() == 'fucksticks'

class Dequeue: 
    """
    Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.

    addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.

    addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.

    removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

    removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

    isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

    size() returns the number of items in the deque. It needs no parameters and returns an integer.
    """

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def add_rear(self, item):
        '''rear has lower time complexity'''
        self.items.append(item)
    
    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'{self.items}'

def dequeue_work():
    dq = Dequeue()
    dq.add_front(1)
    dq.add_front(2)
    print(dq.remove_front())
    print(dq.remove_front())

    dq.add_front('cat')
    dq.add_front('koko minkie')
    dq.add_rear('steve')
    print(dq.remove_rear())

    print(dq.is_empty())
    print(dq.size())

    str1 = 'racecar'

def palindrome_checker(str1=None):
    is_palindrome = Dequeue()
    for item in str1:
        is_palindrome.add_rear(item)

    while is_palindrome.size() > 1:
        if is_palindrome.remove_front() == is_palindrome.remove_rear():
            print('ok')

    if is_palindrome.size() >= 1:
        print('this is a palindrome')
    else:
        print('this is not a palindrome')

# palindrome_checker(str1=str1)

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
    # print(f'{name_list[0]} has the hot potato. Let us play the game')

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