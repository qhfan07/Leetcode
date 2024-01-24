# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:16:32 2024

@author: qhfan
"""

def mostCommonWord(paragraph, banned):
    seen = {}
    res = None
    max_count = 0
    curr = ''
    
    for i, ch in enumerate(paragraph):
        if ch not in " !?',;."  and i < len(paragraph) - 1:
            curr += ch
        elif ch in " !?',;.":
            curr = curr.lower()
            if curr and curr not in banned:
                seen[curr] = seen.get(curr, 0) + 1
                if seen[curr] > max_count:
                    res = curr
                    max_count = seen[curr]
            curr = ''
        else:
            curr += ch
            curr = curr.lower()
            if curr not in banned:
                seen[curr] = seen.get(curr, 0) + 1
                if seen[curr] > max_count:
                    res = curr
                    max_count = seen[curr]
    return res

paragraph = "Bob"
banned = []
print(mostCommonWord(paragraph, banned))