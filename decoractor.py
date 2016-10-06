# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 00:13:49 2016

@author: li
"""

import functools

def log(text1,text2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text1, func.__name__))
            func()
            print('%s %s():' % (text2, func.__name__))
            return 0
        return wrapper
    return decorator
    
@log('call','end')
def now():
    print('2016')
    
f=now
f()
