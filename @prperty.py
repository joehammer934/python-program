# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:05:26 2016

@author: li
"""

class screen(object):
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self,value):
        self._width=value
        
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self,value):
        self._height=value
        
    @property
    def resolution(self):
        self._resolution=self._width*self._height
        return self._resolution    

s=screen()
s.height=64
s.width=1080
print(s.resolution)