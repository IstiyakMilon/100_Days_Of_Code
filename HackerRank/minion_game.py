# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

string="BANANA"
vowel="AEIOU"
kevinScore=0
stuartScore=0
for i in range(len(string)):
    if string[i] in vowel:
        kevinScore+=len(string)-i
    else:
        stuartScore+=len(string)-i
if kevinScore>stuartScore:
    print("Kevin %d" % (kevinScore))
elif stuartScore>kevinScore:
    print(f"Stuart {stuartScore}")
else:
    print("Draw")
    

