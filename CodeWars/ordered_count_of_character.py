# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:21:42 2020

@author: User
"""


ss="abracadabra"

def ordered_count(inp):
    sdict={}
    for s in inp:
        if s not in sdict:
            sdict[s]=1
        else:
            sdict[s]+=1
            
    slist=[(key,value) for key, value in sdict.items()]
    # slist=slist.sort()
    # return sorted(slist)
    return slist


print(ordered_count(ss))