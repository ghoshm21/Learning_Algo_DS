%matplotlib inline
import matplotlib.pyplot as plt
from time import time
from random import random, randint
sizes = [100000*i for i in range(1,1001)]
def bubble_sort(input):
    i = 1
    while i <= len(input):
        for num in range(len(input)-1):
            if (input[num] > input[num+1]):
                input[num],input[num+1] = input[num+1], input[num]
        i=i+1

def bubble_sort_optimized(input):
    swap = True
    while swap:
        swap = False
        for num in range(len(input)-1):
            if (input[num] > input[num+1]):
                input[num],input[num+1] = input[num+1], input[num]
                swap = True
        
        
# to_sort_1 = [10,9,8,7,6,5,-2,4,3,2,1,0]
# print(to_sort_1)
# bubble_sort(to_sort_1)
# print(to_sort_1)

# to_sort_2 = [10,9,8,7,6,5,-2,4,3,2,1,0]
# print(to_sort_2)
# bubble_sort_optimized(to_sort_2)
# print(to_sort_2)
time_sort = []
time_optimize = []

to_sort_3 = list(random.randint(1,10000000000) for x in range(1000000))
to_sort_4 = to_sort_3.copy()
start_time = time()
bubble_sort(to_sort_3)
print(time() - start_time)
# print(to_sort_3)
start_time = time()
bubble_sort_optimized(to_sort_4)
print(time() - start_time)
# print(to_sort_3)
