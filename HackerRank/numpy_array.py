# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:37:25 2020

@author: Shampa
"""


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    positiveArr=[]
    negativeArr=[]
    for item in arr:
        if float(item)<0:
            negativeArr.append(float(item))
        else:
            positiveArr.append(float(item))
    positiveArr.sort(reverse=True)
    negativeArr.sort()
    sortedArr=negativeArr+positiveArr
    return numpy.array(sortedArr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)