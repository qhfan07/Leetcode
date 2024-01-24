# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:01:05 2024

@author: qhfan
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists_iteration(list1, list2):
    dummy = ListNode()
    prev = dummy
    
    while list1 and list2:
        v1 = list1.val
        v2 = list2.val
        if v1 < v2:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next
    
    prev.next = list1 if list1 else list2
    
    return dummy.next

def mergeTwoLists_recursion(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val <= list2.val:
        list1.next = mergeTwoLists_recursion(list1.next,list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursion(list1,list2.next)
        return list2