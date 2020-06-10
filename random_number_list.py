# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 04:30:05 2020

@author: User
"""
import random
rand_list=[]
n=int(input())
for i in range(n):
  x=random.randrange(1,101)
  if x not in rand_list:
    rand_list.append(x)
    
    
print(rand_list)