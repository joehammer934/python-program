# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:43:47 2016

@author: li
"""

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
        
#for n in Fib():
    #if n<1000:
        #print(n)
        
f=Fib()
print(f[20])