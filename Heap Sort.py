# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:38:37 2024

@author: qhfan
"""

arr = [2,4,7,3,-5,2,8,9,3]

def max_heapify(size,idx):
    '''
    Heapify the array. No output.
    '''
    left_child = idx*2 + 1
    right_child = idx*2 + 2
    largest = idx
    if left_child < size and arr[largest] < arr[left_child]:
        largest = left_child
    
    if right_child < size and arr[largest] < arr[right_child]:
        largest = right_child
        
    if largest != idx:
        arr[largest],arr[idx] = arr[idx],arr[largest]
        max_heapify(size, largest)
    

def heap_sort(arr):
    '''
    Heap sort the array.
    '''
    
    #Heapify all the array
    for i in range(len(arr)//2-1,-1,-1): #note: begins with len(arr)//2-1. Why?
        max_heapify(len(arr), i)
    
    #exchange the largest num with the last entry and re-heapify the rest array
    for i in range(len(arr)-1,0,-1): #ends at 1 because index 0 has only one number
        arr[0],arr[i] = arr[i],arr[0] #put the largest in the end
        max_heapify(i,0)

heap_sort(arr)
        