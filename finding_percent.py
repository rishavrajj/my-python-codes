# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 08:45:54 2020

@author: rishav
"""
minPer = 100
dict = {'Krishna':[67,68,69]
        ,'Arjun':[45,98,63]
        ,'Malika':[52,56,60]}
for i in dict:
    x=sum(dict[i])/3
    if(x<minPer):
        minPer=x
        index = i
print(index)