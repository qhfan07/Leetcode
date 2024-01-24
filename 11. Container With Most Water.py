# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:49:59 2024

@author: qhfan
"""

def maxArea(height):
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        max_area = max(max_area, min(height[right], height[left])*(right - left))
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    
    return max_area

height = [1,8,4,6,10,4,1,5]
print(maxArea(height))