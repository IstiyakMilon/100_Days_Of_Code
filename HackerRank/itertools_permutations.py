# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:00:58 2020

@author: Shampa
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,n=map(str, input().split())
# n=int(n)
l1=list(permutations(s,int(n)))
outputList=[]
for item in l1:
    item=list(item)
    outputList.append(''.join(item))

outputList.sort()
for i in outputList:
    print(i)