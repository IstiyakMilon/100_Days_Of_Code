# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:01:02 2020

@author: Shampa
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
l1=input().split()
l2=input().split(' ')
l3=set(input().split(' '))
l4=set(input().split(' '))
happynessCount=0
for item in l2:
    if item in l3:
        happynessCount+=1
    if item in l4:
        happynessCount-=1
print(happynessCount)