# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:06:37 2024

@author: qhfan
"""

num = 123
def numberToWords(num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
       'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    
    def helper(num):
        if num < 20:
            return to19[num - 1]
        if num < 100:
            return [tens[num//10 - 2]] + helper(num%10)
        if num < 1000:
            return [to19[num//100 - 1]] + ["Hundred"] + helper(num%100)
        
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if num < 1000**(p+1):
                return helper(num//1000**p) + [w] + helper(num%1000**p)
    return ' '.join(helper(num)) or 'Zero'

print(numberToWords(num))