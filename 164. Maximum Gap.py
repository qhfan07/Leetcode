# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:04:03 2024

@author: qhfan
"""

nums = [1,3,56,12,3,5,12,4,6,234,6,36]

def maximumGap(self, nums):
    if len(nums) < 2:
        return 0
    
    min_val = min(nums)
    max_val = max(nums)
    
    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
    num_buckets = (max_val - min_val) // bucket_size + 1
    
    buckets = [[] for _ in range(num_buckets)]
    
    for num in nums:
        bucket_number = (num - min_val) // bucket_size
        if not buckets[bucket_number]:
            buckets[bucket_number] = {'min':num,'max':num}
        else:
            buckets[bucket_number]['min'] = min(buckets[bucket_number]['min'],num)
            buckets[bucket_number]['max'] = max(buckets[bucket_number]['max'],num)
            
    max_diff = 0
    pre_max = buckets[0]['max']
    for i in range(1,len(buckets)):
        if buckets[i]:
            temp_diff = buckets[i]['min'] - pre_max
            max_diff = max(max_diff,temp_diff)
            pre_max = buckets[i]['max']
    return max_diff