# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:22:20 2020

@author: rishav
"""
p = input()
n1 = list(p.split(' '))
n = n1[0]
m = n1[1]

print(n)
print(m)
c='.|.'
for i in range(0,3):
    print ((c*(2*i+1)).center(21,'-'))
print("WELCOME".center(21,'-'))
for i in range(4,7):
    print ((c*(2*(7-i)-1)).center(21,'-'))

    
    