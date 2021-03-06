'''searching and sorting'''
'''
searching is process of finding a particular item in a collection of items; usually bool result
in other words, MEMBERSHIP

efficiency of search algorithmns:
- binary in python with slice: O log n but slicing is O(k) in python
- hash table: constant time minus time for collisions
- WHAT IS EFF OF SEQ?
- 

hashing:
- hashing means building a datastructure which we will get us close to being able to search in constant time O(1)
    - hash tables: made up of slots with names
    - naming
        - remainder method: name is integer item divided by table size.  so for table size 11, first item would be named item%11
        - folding method: divide item into equal-size pieces (except for last)
        - mid-square method: 

- collision resolution in hash tables
    - open addressing: alg tries to find next available slot
        - linear probing
    - quadratic probing
    - chaining: (think {key: [value1, value2, value3]})

-efficiency of hash tables
    - can vary due to frequency of collisions and variability of time needed to handle them
    - load factor: basically, either/and: how full is table? how likely is there to be collisions in the inputs?
    - open addressing efficiency depends on whether search is successful or unsuccessfull: 
        - successful = 1/2(1+(1/1-load factor))
        - unsucessful = 1/2(1 + (1/(1-load_factor))^2)
        - if successful and using chaining: 1 + load_f/2
        - if unsuc and chaining: load_factor
- sorting
    -placing elements in a list in some kind of order (alphabeticaly or by len)

- sorting methods:
    - bubble sort: 
        - places adjacent items in a pair, largest of those items is target and will be moved along until it is in its proper place, starts with largest value in collection
        - most inefficient sort bc of wasted moves, but can be designed to stop if items are in proper order
    - selection sort:
        - selection sort: makes only one exchange per pass through, finds largest value in set not in proper place in each pass, and moves it to proper location
    - insertion sort:
        - maintains a growing sorted sublist 
    - shell sort:
    - merge sort:
        - uses divide and conquer strategy 
        - recursive alg that continually splits a list in half
        - if list is empty or has one item it is sorted by definition, 
    - quick sort:
        - uses divide and conquer strategy 
        - does not use additional storage a la mergesort
        - pivot value: can be midpoint, first item, 
        - split point: the actual place in the final list that the pivot value belongs
'''


'''sequential search: divide and conquer strategy'''
test_list0 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
def seq_search(test_list, target):
    position = 0
    found = False
    stop = False
    while position < len(test_list) and not found and not stop:
        if test_list[position] == target:
            found = True
        else:
            if test_list[position] > target:
                stop = True
            else:
                position = position + 1

    return found

# print(seq_search(test_list0,10))

'''binary search implementation: recursion'''
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
def binary_search(test_list, target):
    if len(test_list) == 0:
        return False
    else:
        midpoint = len(test_list)//2

        if test_list[midpoint] == target:
            return True
        else:
            if target < test_list[midpoint]:
                # breakpoint()
                return binary_search(test_list[:midpoint], target) # slice is slow in python, workarounds are available
            else:
                return binary_search(test_list[midpoint+1:], target)

# print(0 in test_list)
# print(binary_search(test_list, 42))

'''hash tables and Map abstract data type'''

"""
    Map() Create a new, empty map. It returns an empty map collection.

    put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.

    get(key) Given a key, return the value stored in the map or None otherwise.

    del Delete the key-value pair from the map using a statement of the form del map[key].

    len() Return the number of key-value pairs stored in the map.

    in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
""" 

class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.value = [None] * self.size

    def put(self, key, value):
        # uses simple remainder method for generating hash
        # uses linear probing with plus +1 rehashing; assumes there will eventually be an empty slot
        # cannot handle case where there are no empty slots left
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None: # if no collision
            self.slots[hash_value] = key
            self.value[hash_value] = value 
        else:
            if self.slots[hash_value] == key: # 
                self.value[hash_value] = value  # replace value
            else:
                # 
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.value[next_slot] = value
                else:
                    self.data[next_slot] = value # replace

    def hash_function(self, key, size):
        # returns the remainder of division
        if isinstance(key, str):
            key = len(key)
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash+1)%size

    def get(self, key):
        # compute initial hash_value based on len of table, given key, and hash_function algorithm
        # if 
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.value[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)
'''
hasht = HashTable()
hasht.put('a', 15)
hasht.put('j0', 15)
hasht.put('jim', 10)
hasht.put('paul', 9)
hasht.put('mike', 12)
hasht.put('beauchamp', 12)
hasht.put('beauchamp-depuis-de-ulm', 12)
print(hasht.get('a'))
print(hasht.slots)
print(hasht.value)
'''
list1 = [54,26,93,17,77,31,44,55,20]
def bubble_sort(list1):
    for pass_num in range((len(list1)-1), 0, -1):
        for i in range(pass_num):
            if list1[i] > list1[i+1]:
                placeh = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = placeh
# bubble_sort(list1)
# print(list1)

def short_bubble(list1):
    exchanges = True
    p_num = len(list1) - 1
    while p_num > 0 and exchanges:
        exchanges = False
        for i in range(p_num):
            if list1[i] > list1[i + 1]:
                exchanges = True
                placeh = list1[i]
                list1[i] = list1[i + 1]
                list1[i + 1] = placeh

list1 = [54,26,93,17,77,31,44,55,20]
# short_bubble(list1)
# print(list1)

'''selection sort'''
list1 = [54,26,93,17,77,31,44,55,20]
def selection_sort(list1):
    for item in range((len(list1))-1, 0, -1):
        position_of_max = 0
        for location in range(1, item+1):
            if list1[location] > list1[position_of_max]:
                position_of_max = location

        placeh = list1[item]
        list1[item] = list1[position_of_max]
        list1[position_of_max] = placeh

# selection_sort(list1)
# print(list1)
'''insertion sort'''
def insertion_sort(list1):
    for index in range(1, len(list1)):
        current_value = list1[index]
        position = index
        position1 = index

        while position > 0 and list1[position - 1] > current_value:
            list1[position] = list1[position-1]
            position = position - 1
        
        list1[position] = current_value
        breakpoint()

# insertion_sort(list1)
# print(list1)
'''shell sort'''
# print(list1)
def gap_insert_sort(list1, start, gap):
    for i in range(start + gap, len(list1), gap): # 5-9
        # print(f'gap_inserting withn range start:{start+gap}, stop:{len(list1)}, step:{gap})')

        current_value = list1[i]
        position = i 

        while position >= gap and list1[position - gap] > current_value:
            # print(f'gap while loop: {position}: inserting {list1[position - gap]} into {list1[position]}')
            list1[position] = list1[position - gap]
            position = position - gap
            print(list1)

        list1[position] = current_value

def shell_sort(list1):
    sublist_count = len(list1)//2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insert_sort(list1, start_position, sublist_count)
            print('after increment of size', sublist_count, 'the list is', list1)

        sublist_count = sublist_count//2

# shell_sort(list1)
# print(list1)

'''merge sort'''
def merge_sort(list1):
    print('splitting', list1)
    if len(list1) > 1:
        mid = len(list1)//2
        lefthalf = list1[:mid]
        righthalf = list1[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        k = 0
        j = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                list1[k] = lefthalf[i]
                i += 1
            else:
                list1[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            list1[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            list1[k] = righthalf[j]
            j += 1
            k += 1
        print('merging:', list1)

# merge_sort(list1)
# print(list1, 'FINALE')
'''quick sort'''
def quick_sort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

quick_sort(list1)
print(list1)