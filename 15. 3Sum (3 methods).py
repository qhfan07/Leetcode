# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:59:15 2024

@author: qhfan
"""

'''
There are three methods for 3Sum. Fisrt two method need sorting, the last one does not need sorting.
'''

def threeSum1(nums):
    '''
    This method use two pointers, but need to sort the list first.
    Time complexity is O(n^2).
    '''
    nums.sort()
    res = set()
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        remain = -nums[i]
        
        while left < right:
            sum_two = nums[left] + nums[right]
            if sum_two > remain:
                right -= 1
                continue
            if sum_two < remain:
                left += 1
                continue
            if sum_two == remain:
                res.add((nums[i],nums[left],nums[right]))
                left += 1
                right -= 1
                
    return res

def threeSum2(nums):
    '''
    This method use hashtable, but need to sort the list first.
    Time complexity is O(n^2).
    '''
    res = set()
    nums.sort()
    
    def twoSum(i,remain):
        seen = set()
        for j in range(i+1,len(nums)):
            if (remain - nums[j]) not in seen:
                seen.add(nums[j])
            else:
                res.add((nums[i],nums[j],remain-nums[j]))
                
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i == 0 or nums[i-1] != nums[i]:
            twoSum(i,-nums[i])
    
    return res

def threeSum3(nums):
    '''
    This method use hashtable, but need extra space.
    Time complexity is O(n^2), space complexity is O(n).
    '''
    res = set()
    n = len(nums)
    dup = set()
    seen = {}
    
    for i in range(n-2):
        if nums[i] not in dup:
            dup.add(nums[i])
            for j in range(i+1,n):
                remain = -nums[i] - nums[j]
                if remain in seen and seen[remain] == i:
                    res.add(tuple(sorted([nums[i],nums[j],remain])))
                else:
                    seen[nums[j]] = i
    
    return res