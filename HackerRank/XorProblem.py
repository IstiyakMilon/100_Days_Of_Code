# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:22:38 2020

@author: User
"""


def maxXorValue(x, k):
    # Write your code here
    X=list(x)
    y=[]
    for i in range(k):
      if X[i]=='0':
        y.append('1')
      elif X[i]=='1':
        y.append('0')
    
    if k<len(X):
      for i in range(len(X)-k):
        y.append('0')
    y=''.join(y)
    return y



print(maxXorValue('10010', 5))
print(maxXorValue('11010', 1))