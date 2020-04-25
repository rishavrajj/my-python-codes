# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:47:00 2020

@author: rishav
"""

string = "AABCAAADA"
k = int(input())
l = []
for i in range(0,len(string),k):
    l.append(string[i:i+k])
print(l)
for i in range(0,len(l)):
    n=l[i]
    s=""
    li=[]
    for j in range(0,len(n)):
        s=""
        if n[j] not in li:
            li.append(n[j])
        s= ''.join(li)
    print(s,sep='\n')

        