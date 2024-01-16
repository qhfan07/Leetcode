# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:57:17 2024

@author: qhfan
"""

import collections
def topKFrequent(nums, k):
    n = len(nums)
    if n == k:
        return nums
    
    count = collections.Counter(nums)
    ids = list(count.keys())
    
    def partition(left,right):
        pivot_val = count[ids[right]]
        i = left
        j = right - 1
        while i < j:
            while count[ids[i]] < pivot_val and i < right:
                i += 1
            while count[ids[j]] >= pivot_val and j > left:
                j -= 1
            if i < j:
                ids[i],ids[j] = ids[j],ids[i]
        
        if count[ids[i]] > pivot_val:
            ids[i],ids[right] = ids[right],ids[i]
        return i
    
    def quickselect(left,right):
        pivot_idx = partition(left,right)
        if pivot_idx == len(ids) - k:
            return
        elif pivot_idx > len(ids) - k:
            quickselect(left, pivot_idx - 1)
        else:
            quickselect(pivot_idx + 1, right)
    
    quickselect(0, len(ids)-1)
    return ids[len(ids)-k:]

nums = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,7]
k = 3
print(topKFrequent(nums,k))