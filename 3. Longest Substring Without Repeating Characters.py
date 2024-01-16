# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:57:10 2024

@author: qhfan
"""

def lengthOfLongestSubstring(s):
    ch_hash = {}
    max_len = 0
    temp = 0
    prev_idx = 0
    
    for i,ch in enumerate(s):
        if ch not in ch_hash or ch_hash[ch] < prev_idx:
            ch_hash[ch] = i
            temp += 1
        else:
            max_len = max(max_len,temp)
            prev_idx = ch_hash[ch] + 1
            temp = i - ch_hash[ch]
            ch_hash[ch] = i
        
        
    return max(temp,max_len)

s = 'abba'
print(lengthOfLongestSubstring(s))