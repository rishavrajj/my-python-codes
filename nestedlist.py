# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:20:34 2020

@author: rishav
"""
#to find the 2nd lowest score of students.
markSheet = []
scorelist = []
namelist=[]
n = int(input("total input : "))
for i in range(n):
    name = input("enter name: ")
    score = float(input("enter score: "))
    markSheet += [[name,score]]
    scorelist += [score]
key = sorted(list(set(scorelist)))[1]#convert scorelist to "set" datatype to avoid repetition.
for i,j in sorted(markSheet):
    if(j==key):
        print(i)

