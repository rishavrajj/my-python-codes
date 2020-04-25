# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:10:27 2020

@author: rishav
"""
arr =[]
summ = 0
n=int(input())
for i in range(0,n):
    print(i+1)
    p=n
    while(p!=0):
        p=p%8
        summ = summ*10 + p
    print(summ)
    