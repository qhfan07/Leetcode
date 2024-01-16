# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:55:00 2024

@author: qhfan
"""

def twoSum(nums, target):
    remain_dict = {}
    for i,num in enumerate(nums):
        remain = target - num
        if num in remain_dict:
            return [remain_dict[num],i]
        else:
            remain_dict[remain] = i
            
nums = [2,7,28,10,3]
target = 9
print(twoSum(nums,target))