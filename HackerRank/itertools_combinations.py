# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:54:06 2020

@author: Shampa
"""


from itertools import combinations
s,n=input().split()
a=list(s)
a.sort()
# print(a)
for i in range(1,int(n)+1):
  l1=list(combinations(a, i))
  for item in l1:
    print(''.join(item))