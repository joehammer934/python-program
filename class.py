# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:58:51 2016

@author: li
"""

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=80:
            return 'B'
        elif self.__score>=70:
            return 'C'
        else:
            return 'D'

bert = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bert.print_score()
lisa.print_score()
print(bert.get_grade())
bert.__score=90
print(bert.get_grade())