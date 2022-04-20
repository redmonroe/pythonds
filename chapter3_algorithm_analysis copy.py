# source: https://runestone.academy/ns/books/published//pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html
# WHAT IS ALGORITHMN ANALYSIS? 

'''
    an algorithm is a generic, step-by-step list of instructions for solving a problem

    a program is an algorithm that has been encoded into a programming langugage.

    Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each algorithm uses.

    two ways of comparing algorithm efficiency: space resources and time resources(execution time)

    ways around sluggish iteration:
        - a closed equation

    big O

    1       constant
    log n   logarithmic
    n       linear
    n log n log linear
    n2      quadratic
    n3      cubic
    2^n     exponential 

    * differences between orders become more pronounced as n gets bigger

'''
import time
from functools import lru_cache

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



