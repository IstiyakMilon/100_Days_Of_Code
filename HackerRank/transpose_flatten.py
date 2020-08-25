# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:46:46 2020

@author: User
"""


import numpy
N,M=input().split()
list=[]
for _ in range(int(N)):
  n=input().split()
  x=[int(i) for i in n]
  list.append(x)

list1=numpy.array(list)
print(numpy.transpose(list1))
print(list1.flatten())