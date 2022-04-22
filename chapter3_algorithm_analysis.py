# source: https://runestone.academy/ns/books/published//pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html
# WHAT IS ALGORITHMN ANALYSIS? 

'''


    an algorithm is a generic, step-by-step list of instructions for solving a problem

    a program is an algorithm that has been encoded into a programming langugage.

    Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each algorithm uses.

    two ways of comparing algorithm efficiency: space resources and time resources(execution time)

    ways around sluggish iteration:
        - a closed equation

    big O notation, another view: source: https://towardsdatascience.com/introduction-to-big-o-notation-820d2e25d3fd
        - deals with the worst-case scenario (ie the thing you are looking for is found last or not at all); algorithm will never perform worse than this


    big O: tells you how much longer it will take to solve a problem as the input gets bigger

    1       constant
    log n   logarithmic log2 8 = 3 bc 2 x 2 x 2 (2 three times) = 8
    n       linear
    n log n log linear
    n2      quadratic
    n3      cubic
    2^n     exponential 
    n!      factorial

    * differences between orders become more pronounced as n gets bigger

    Big O efficiency and Python lists: 
        O(1) = take the same amount of time no matter how large the list becomes
        O(n) = linear search, algo takes an additional step for each additional data element, 1:1 or 2:1, 
            complexity is directly related to size of inputs
        O(log n) = binary search (ie), algo takes an additional step each time the data doubles
            - finding middle of list and eliminating that half of the list
            - sorting list can introduce its own complexity

    python operations and efficiency: (from ch. 3.6 and 3.7)
        further reading: time complexity python: https://wiki.python.org/moin/TimeComplexity
        lists
            - constant time O(1): index, append, index assignment, pop
            - linear O(n): pop(i), insert, del, iteration, del slice, reverse, concate
            - n log n: sort (this is slowest of what I can determine from pythonds chapter)
        dicts
            - o1: get, set, del, contains/in
            - on: iteration, copy



'''
import time
from functools import lru_cache
from timeit import Timer
# @lru_cache
def the_sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i

    end = time.time()
    return the_sum, start-end

# for i in range(5):
    # print('sum is %d required %10.7f seconds'%the_sum_of_n(10000000))

def sum_of_n3(n):
    start = time.time()
    
    answer = (n*(n+1))/2
    end = time.time()
    return answer, start-end

# print(sum_of_n3(10))

# for i in range(5):
    # print(sum_of_n3(100))


def comparing_performance_of_python_lists():
    pass

def test1(): # index
    l = []
    for i in range(1000):
        l = l + [i]

def test2(): # append
    l = []
    for i in range(1000):
        l.append(i)

def test3(): #list comprehension
    l = [i for i in range(1000)]

def test4(): # list range
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
# print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "milliseconds")


def timing_pop_and_python_lists(self):
    pass

import timeit

popzero = timeit.Timer("x.pop(0)",
                    "from __main__ import x")
popend = timeit.Timer("x.pop()",
                    "from __main__ import x")

x = list(range(2000000))
# popzero.timeit(number=1000)

x = list(range(2000000))
# popend.timeit(number=1000)

def three_7_compare_contains_lists_v_dicts():
    pass
    '''claim contains for list is linear, but constant for dicts'''
    '''we would expect that IN dict is not only faster but also takes the same time for a larger dataset'''

import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))

'''result of experiment: lists is way slower, even with as few as 30000 items, dict not slower up to 1m'''