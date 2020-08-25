# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 08:49:39 2020

@author: User
"""


def getMaxScore(jewels):
    # Write your code here
    counter=0
    jwLen=len(jewels)
    for i in range(jwLen//2):
        if 'aa' in jewels:
            n1=jewels.count('aa')
            counter+=n1
            jewels=jewels.replace('aa', '')
        elif 'bb' in jewels:
            n1=jewels.count('bb')
            counter+=n1
            jewels=jewels.replace('bb', '')
        elif 'cc' in jewels:
            n1=jewels.count('cc')
            counter+=n1
            jewels=jewels.replace('cc', '')
        elif 'dd' in jewels:
            n1=jewels.count('dd')
            counter+=n1
            jewels=jewels.replace('dd', '')
            
        elif 'ee' in jewels:
            n1=jewels.count('ee')
            counter+=n1
            jewels=jewels.replace('ee', '')
    
        elif 'ff' in jewels:
            n1=jewels.count('ff')
            counter+=n1
            jewels=jewels.replace('ff', '')
        elif 'gg' in jewels:
            n1=jewels.count('gg')
            counter+=n1
            jewels=jewels.replace('gg', '')
        elif 'hh' in jewels:
            n1=jewels.count('hh')
            counter+=n1
            jewels=jewels.replace('hh', '')
        elif 'ii' in jewels:
            n1=jewels.count('ii')
            counter+=n1
            jewels=jewels.replace('ii', '')
        elif 'jj' in jewels:
            n1=jewels.count('jj')
            counter+=n1
            jewels=jewels.replace('jj', '')
        elif 'kk' in jewels:
            n1=jewels.count('kk')
            counter+=n1
            jewels=jewels.replace('kk', '')
        elif 'll' in jewels:
            n1=jewels.count('ll')
            counter+=n1
            jewels=jewels.replace('ll', '')
        elif 'mm' in jewels:
            n1=jewels.count('mm')
            counter+=n1
            jewels=jewels.replace('mm', '')
        elif 'nn' in jewels:
            n1=jewels.count('nn')
            counter+=n1
            jewels=jewels.replace('nn', '')
        elif 'oo' in jewels:
            n1=jewels.count('oo')
            counter+=n1
            jewels=jewels.replace('oo', '')
        elif 'pp' in jewels:
            n1=jewels.count('pp')
            counter+=n1
            jewels=jewels.replace('pp', '')
        elif 'qq' in jewels:
            n1=jewels.count('qq')
            counter+=n1
            jewels=jewels.replace('qq', '')
        elif 'rr' in jewels:
            n1=jewels.count('rr')
            counter+=n1
            jewels=jewels.replace('rr', '')
        elif 'ss' in jewels:
            n1=jewels.count('ss')
            counter+=n1
            jewels=jewels.replace('ss', '')
        elif 'tt' in jewels:
            n1=jewels.count('tt')
            counter+=n1
            jewels=jewels.replace('tt', '')
        elif 'uu' in jewels:
            n1=jewels.count('uu')
            counter+=n1
            jewels=jewels.replace('uu', '')
        elif 'vv' in jewels:
            n1=jewels.count('vv')
            counter+=n1
            jewels=jewels.replace('vv', '')
        elif 'ww' in jewels:
            n1=jewels.count('ww')
            counter+=n1
            jewels=jewels.replace('ww', '')
        elif 'xx' in jewels:
            n1=jewels.count('xx')
            counter+=n1
            jewels=jewels.replace('xx', '')
        elif 'yy' in jewels:
            n1=jewels.count('yy')
            counter+=n1
            jewels=jewels.replace('yy', '')
        elif 'zz' in jewels:
            n1=jewels.count('zz')
            counter+=n1
            jewels=jewels.replace('zz', '')
        
                
    return counter
    
    
    
    
print(getMaxScore('abxcddcxbyyd'))
print(getMaxScore('abcd'))

# Python3 code to demonstrate  
# occurrence frequency using  
# count() 
  
# initializing string  
test_str = "GeeksforGeeks"
  
# using count() to get count  
# counting e  
counter = test_str.count('eee') 
  
# printing result  
print ("Count of e in GeeksforGeeks is : "
                           +  str(counter)) 