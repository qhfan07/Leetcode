# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:50:12 2024

@author: qhfan
"""

def strStr(haystack, needle):
    '''
    Sliding window. Time complexity is O(nm).
    '''
    m = len(needle)
    n = len(haystack)

    for window_start in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window_start + i]:
                break
            if i == m - 1:
                return window_start

    return -1

haystack = 'mississipi'
needle = 'issip'
print(strStr(haystack,needle))