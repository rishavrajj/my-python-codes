# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:42:52 2020

@author: rishav
"""
string = "ABCDEFGHIJKLMNOPQRSTUV"
max_width = 4
l=[]
for i in range(0,len(string),max_width):
    l.append(string[i:i+max_width])
for i in range(0,len(l)):
    print(l[i],sep='\n')
