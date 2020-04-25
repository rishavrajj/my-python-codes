# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:31:56 2020

@author: rishav
"""

arr =  [3,5,7,6,9,2,4,1,8.9,3,8,7,10,20,2,18,20,16]
maxi = 0
secMax = 0
n = len(arr)
for i in range(0,n):
    if(arr[i]==maxi):
        maxi = arr[i]
    else:
        if(arr[i]>maxi):
            secMax=maxi
            maxi=arr[i]
        elif(arr[i]>secMax):
            secMax=arr[i]
print(secMax)
