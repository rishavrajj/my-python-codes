# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:55:43 2020

@author: rishav
"""
for _ in range(int(input())):
    try:
        n,d = map(int,input().split())
        print(n/d)
    except Exception as e:
        print("Error Code:",e)