# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:32:38 2024

@author: qhfan
"""

arr = [2,5,7,3,8,9,0,-1,-2,10,23,-213]

def quick_sort(arr,left,right):
    if left < right:
        pivot_idx = get_pivot(arr,left,right)
        quick_sort(arr,left,pivot_idx-1)
        quick_sort(arr,pivot_idx+1,right)

def get_pivot(arr,left,right):
    pivot = arr[right]
    i = left
    j = right - 1
    while i < j:
        while arr[i] < pivot and i < right:
            i += 1
        while arr[j] >= pivot and j > left:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    
    if arr[i] > pivot:
        arr[right],arr[i] = arr[i],arr[right]
    return i
        
quick_sort(arr,0,len(arr)-1)
print(arr)