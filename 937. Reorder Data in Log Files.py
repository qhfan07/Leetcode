# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:40:00 2024

@author: qhfan
"""

def reorderLogFiles(logs):
    right = len(logs) - 1
    for i in range(len(logs) - 1, -1, -1):
        if logs[i][-1].isdigit():
            logs[i], logs[right] = logs[right], logs[i]
            right -= 1
    
    logs[:right + 1] = sorted(logs[:right + 1], key = lambda x:(x.split()[1:],x.split()[0]))
    return logs

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))