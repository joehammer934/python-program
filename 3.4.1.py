# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:18:50 2016

@author: li
"""

def count(s,r,b):
    return (1-(1-s**r)**b)
    
A=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for i in A:
    print(count(i,3,10))
print('---分割线---')
    
for i in A:
    print(count(i,6,20))
print('---分割线---')
   
for i in A:
    print(count(i,5,50))