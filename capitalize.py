# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:50:13 2020

@author: rishav
"""
s = input()
l = s.split(' ')
for i in range(0,len(l)):
    l[i]=l[i].capitalize()
s = " ".join(l)
print(s)
