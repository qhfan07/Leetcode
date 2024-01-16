# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:29:55 2024

@author: qhfan
"""


def myAtoi(s):
    n = len(s)
    i = 0
    negative = False
    
    while i < n and s[i] == ' ':
        i += 1
    
    if i < n and s[i] == '-':
        negative = True
        i += 1
    elif i < n and s[i] == '+':
        i += 1
    
    res = ''
    for k in range(i,len(s)):
        if not s[k].isdigit():
            break
        res += s[k]
    
    if not res:
        return 0
    
    res = int(res)
    
    return max(-2**31,-res) if negative else min(2**31-1,res)

s = '+'
print(myAtoi(s))