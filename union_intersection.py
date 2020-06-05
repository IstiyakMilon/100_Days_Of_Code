# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 04:18:00 2020

@author: User
"""


A={1,2,3,4,5}
B={5,6,7,8}
aList=list(A)
bList=list(B)
C=set(aList+bList)
print(C)
C=[x for x in aList for j in bList if x not in bList]
print(set(C))