# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:40:25 2020

@author: Shampa
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
n=input().split()
N=input()
earned_money=0
for i in range(int(N)):
    shoe_no, price=input().split()
    if shoe_no in n:
        earned_money+=int(price)
        n.remove(shoe_no)

print(earned_money)