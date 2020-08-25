# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 06:27:29 2020

@author: Shampa
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())
s=input()
Student = namedtuple('Student',s)
markTotal=0
for i in range(N):
    n1,n2,n3,n4=input().split()
    xyz = Student(n1,n2,n3,n4)
    markTotal+=int(xyz.MARKS)

print(markTotal/N)
