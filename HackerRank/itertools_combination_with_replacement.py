# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:42:35 2020

@author: Shampa
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,n=input().split()
a=list(s)
a.sort()
list1=list(combinations_with_replacement(a, int(n)))
for item in list1:
  print(''.join(item))