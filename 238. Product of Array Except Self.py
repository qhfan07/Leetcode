# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:03:28 2024

@author: qhfan
"""

def productExceptSelf(nums):
    ans = []
    total = 1
    have_one_zero = False
    
    for i in range(len(nums)):
        if nums[i] != 0:
            total *= nums[i]
        elif not have_one_zero:
            have_one_zero = True
        else:
            return [0]*len(nums)
    
    for i in range(len(nums)):
        if nums[i] != 0:
            if have_one_zero:
                ans.append(0)
            else:
                ans.append(int(total/nums[i]))
        else:
            ans.append(total)
    
    return ans