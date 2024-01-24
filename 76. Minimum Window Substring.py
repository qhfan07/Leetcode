# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:58:57 2024

@author: qhfan
"""

import collections
def minWindow(s, t):
    if not s or not t:
        return  ""
    
    m = len(s)
    count = collections.Counter(t)
    n = len(count.keys())
    seen = {}
    included = 0
    left, right = 0, 0
    res = (float('inf'), None, None)
    
    while right < m:
        if s[right] not in t:
            right += 1
        else:
            seen[s[right]] = seen.get(s[right],0) + 1
            if seen[s[right]] == count[s[right]]:
                included += 1
            while left <= right and included == n:
                while s[left] not in t:
                    left += 1
                seen[s[left]] -= 1
                if seen[s[left]] < count[s[left]]:
                    included -= 1
                if res[0] > right - left:
                    res = (right - left + 1, left, right)
                left += 1
            right += 1

    return "" if res[0] == float('inf') else s[res[1]:res[2] + 1]

s = "aa"
t = "aa"
print(minWindow(s,t))