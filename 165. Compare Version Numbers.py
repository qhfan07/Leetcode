# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:10:49 2024

@author: qhfan
"""

def compareVersion(version1, version2):
    n = len(version1)
    m = len(version2)
    
    i, j = 0, 0
    while i < n and j < m:
        curr1 = ""
        curr2 = ""
        while i < n and version1[i] != ".":
            curr1 += version1[i]
            i += 1
        while j < m and version2[j] != ".":
            curr2 += version2[j]
            j += 1
        if int(curr1) < int(curr2):
            return -1
        elif int(curr1) > int(curr2):
            return 1
        else:
            i += 1
            j += 1
    
    while i < n:
        curr1 = ""
        while i < n and version1[i] != ".":
            curr1 += version1[i]
            i += 1
        if int(curr1) > 0:
            return 1
        elif i == n:
            return 0
        else:
            i += 1
    while j < m:
        curr2 = ""
        while j < m and version2[j] != ".":
            curr2 += version2[j]
            j += 1
        if int(curr2) > 0:
            return -1
        elif j == m:
            return 0
        else:
            j += 1
    return 0

class Solution:
    def get_next_chunk(self, version, n, p):
        # If pointer is set to the end of the string, return 0
        if p > n - 1:
            return 0, p
        
        # Find the end of the chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1

        # Retrieve the chunk
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])

        # Find the beginning of the next chunk
        p = p_end + 1
        
        return i, p
        
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        # Compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # The versions are equal
        return 0  


version1 = '1.0.1'
version2 = '1'
print(compareVersion(version1, version2))