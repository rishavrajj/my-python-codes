# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:21:28 2020

@author: rishav
"""
n=int(input())
l=[]
for i in range(0,n):
    l.append(input())
li=[]
for i in range(0,n):
    if((l[i][0:].lower()) == l[i][::-1].lower()):
        li.append(l[i])
print(li)