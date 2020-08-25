# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:38:30 2020

@author: Shampa
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
N=input()
product_price=dict()
for _ in range(int(N)):
    *item, price=input().split()
    item_name=' '.join(item)
    if item_name not in product_price:
        product_price[item_name]=int(price)
    else:
        product_price[item_name]+=int(price)

for key,value in product_price.items():
    print(f"{key} {value}")