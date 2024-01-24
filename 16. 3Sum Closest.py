# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:54:44 2024

@author: qhfan
"""

import math
def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    min_res = float('inf')
    
    for i in range(n-2):
        if min_res < float('inf') and nums[i] > math.ceil(target/3):
            break
        if i == 0 or nums[i-1] != nums[i]:
            left = i + 1
            right = n - 1
            temp = float('inf')
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                temp = threeSum if abs(threeSum-target) < abs(temp-target) else temp
                if threeSum < target:
                    left += 1
                elif threeSum > target:
                    right -= 1
                else:
                    return target
            if abs(target-temp) < abs(target-min_res):
                min_res = temp
    
    return min_res

nums = [2,3,8,9,10]
target = 16
print(threeSumClosest(nums, target))