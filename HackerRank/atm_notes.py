# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:31:17 2020

@author: Shampa
Code Wars problems

"""

def atm_note(n):
  noteCount=0
  temp=n//500
  if temp>0:
    n=n%500
    noteCount+=temp
  temp=n//200
  if temp>0:
    n=n%200
    noteCount+=temp
  temp=n//100
  if temp>0:
    n=n%100
    noteCount+=temp
  temp=n//50
  if temp>0:
    n=n%50
    noteCount+=temp
  temp=n//20
  if temp>0:
    n=n%20
    noteCount+=temp
  temp=n//10
  if temp>0:
    n=n%10
    noteCount+=temp
  if n>0 and n<10:
    return -1
  else:
    return noteCount


print(atm_note(750))

