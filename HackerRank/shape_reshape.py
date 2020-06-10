# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:18:41 2020

@author: User
"""

import numpy
List=input().split()
List1=[int(x) for x in List]
arr=numpy.array(List1)
change_arr=numpy.reshape(arr,(3,3))
print(change_arr)