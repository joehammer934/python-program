# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:08:56 2016

@author: li
"""

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 7 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    
for name, member in Weekday.__members__.items():
    print(name, '=>', member.value)