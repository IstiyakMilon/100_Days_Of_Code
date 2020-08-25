# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:38:42 2020

@author: Shampa
"""


import numpy
N,M,P=map(int, input().split())
NXP=numpy.array([input().split() for _ in range(N)], int)
MXP=numpy.array([input().split() for _ in range(M)], int)
NMP=numpy.concatenate((NXP,MXP), axis=0)
print(NMP)