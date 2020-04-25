# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:08:32 2020

@author: rishav

s = "banana"
l = len(s)
di = {}
for i in range(0,l):
    for j in range(1,l):
        if s[i:i+j] not in di:
            value = 1 
            di[s[i:i+j]] = value
        elif :
            value += 1
            di[s[i:i+j]] = value
print(di)
print(len(di))"""
s=input()
v='AEIOU'
stuart, kevin, ln = 0, 0, len(s)
for i in range(ln):
    if s[i] in v:
        kevin += ln - i
    else:
        stuart += ln - i
if stuart > kevin:
    print('Stuart', stuart)
elif stuart == kevin:
    print('Draw')
else:
    print('Kevin', kevin)