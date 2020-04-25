# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:11:10 2020

@author: rishav
"""

n = int(input())
l = list(map(int,input().split(' ')))
s = set(l)
count = 0
for k in s:
    for j in range(len(l)):
        if(k == l[j]):
            count+=1
    if(count==1):
        print(k)
        
print(k)