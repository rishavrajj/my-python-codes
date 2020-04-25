# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:10:39 2020

@author: rishav
"""

ar =list(input().split(' '))
n = int(ar[0])
m = int(ar[1])
arr =list(input().split(' '))
arr1 =list(input().split(' '))
set1 = set(arr1)
arr2 =list(input().split(' '))
set2 = set(arr2)
count = 0
for i in range(0,len(arr)):
    if arr[i] in set1:
        count+=1
    elif arr[i] in set2:
        count-=1
print(count)
        