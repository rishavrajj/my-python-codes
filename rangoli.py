# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:49:46 2020

@author: rishav
"""

n = int(input())
alpha = list("abcdefghijklmnopqrstuvwxyz")
l=[]
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append(s[::-1]+s[1:])
width = len(l[0])
for i in range(n-1,0,-1):
    print (l[i].center(width,"-"))
for i in range(n):
    print (l[i].center(width,"-"))