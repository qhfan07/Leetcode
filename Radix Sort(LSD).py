# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:41:42 2024

@author: qhfan
"""

from functools import reduce
arr = [845,2913,234,3932,222,140,534]

def radix_sort(arr):
    max_digit = len(str(max(arr))) #get the maxmimum of digits among all numbers in the array

    for digit in range(max_digit):
        count = [[] for _ in range(10)] #counting list to store numbers with the same numebr at the specific digit
        for num in arr:
            num_digit = num // 10 ** digit % 10
            count[num_digit].append(num)
        #arr = [num for lst in count for num in lst] #flatten the counting list
        arr = reduce(lambda x, y: x + y, count) #another way using reduce
    return arr

arr = radix_sort(arr)
print(arr)