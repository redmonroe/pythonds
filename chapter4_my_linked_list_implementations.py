# https://www.youtube.com/watch?v=Hj_rA0dhr2I : linked lists for technical interviews

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next_item):
        self.next = next_item

    def __str__(self):
        return f'Node(value: {self.value} next: {self.next})'


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, node_value):
        temporary_node_value = Node(node_value) # so we don't add Nodes directly to LL, they just are a constituent, we access functionality o node by putting node_value into a Node object
        temporary_node_value.set_next(self.head) # so this is None if we are adding first item
        self.head = temporary_node_value

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        return f'LinkedList(value of head: {self.head})'

# manual linked list with Node only
n = Node('5')
n2 = Node(10)
n3 = Node(355)
n.set_next(n2)
n2.set_next(n3)

# print manual linked list
# write linked_list funcs from the persepective of current
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next

def recursive_ll(head):
    # print(head.value, ':')
    if head == None:
        return 
    else:
        print(head.value)
        recursive_ll(head.next)

# print_linked_list(n) # 5, 10, 355
# recursive_ll(n) # 5, 10, 355

def make_array_from_ll(head):
    return_list = []
    current = head
    while current is not None:
        return_list.append(current.value)
        current = current.next
    return return_list

def recursive_make_array_from_ll(head):
    return_list = []

    def fill_values(head, return_list):
        if head == None:
            return
        else:
            return_list.append(head.value)
            fill_values(head.next, return_list)
    fill_values(head, return_list)
    return return_list

# print(make_array_from_ll(n))
# print(recursive_make_array_from_ll(n))

def sum_ll(head):
    counter = 0
    current = head
    while current is not None:
        counter += int(current.value)
        current = current.next
    return counter

def rec_sum_ll(count, head):
    if head == None:
        return 0
    else:
        return int(head.value) + rec_sum_ll(count, head.next)
    

# print(sum_ll(n))
# print(rec_sum_ll(0, n))

def find_ll(target, head):
    position = -1
    current = head
    while current is not None:
        position += 1
        if current.value == target:
            return position
        else:
            current = current.next

def rec_find_ll(head, target):
    if head == None:
        return False
    else:
        if head.value == target:
            return True
        else:
            return rec_find_ll(head.next, target)
        

# print(find_ll('5', n))
# print(rec_find_ll(n, 355))

def node_value_at_index(head, index):
    position = 0
    current = head
    while current is not None:
        if position == index:
            return current.value
        else:
            position += 1
            current = current.next

# print(node_value_at_index(n, 2))

def rec_node_value_at_index(head, index):
    try:
        if index == 0:
            return head.value
        else:
            index = index - 1
            return rec_node_value_at_index(head.next, index)
    except AttributeError as e:
        print("list out o' range")

# print(rec_node_value_at_index(n, 2))