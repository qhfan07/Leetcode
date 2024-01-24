# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:15:59 2024

@author: qhfan
"""

import collections
def groupAnagrams1(strs):
    '''
    Sorted by string. O(nmlogm)
    '''
    str_dict = collections.defaultdict(list)
    for word in strs:
        str_dict[tuple(sorted(list(word)))].append(word)
    
    return str_dict.values()

def groupAnagrams2(strs):
    str_dict = collections.defaultdict(list)
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        str_dict[tuple(count)].append(word)
    
    return str_dict.values()
                

strs = ['eat','tea','show','owsh']
print(groupAnagrams2(strs))


