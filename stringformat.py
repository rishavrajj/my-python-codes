# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:32:40 2020

@author: rishav
"""
n = 3
w=len(bin(n)[2:])
for i in range(1,n):
    n1 = str(oct(i))
    n2 = str(hex(i)).upper()
    n3 = str(bin(i))
    n1 = n1[2:]
    n2 = n2[2:]
    n3 = n3[2:]
    print(str(i).rjust(w,' ') + n1.rjust(w,' ') + n2.rjust(w,' ') + n3.rjust(w,' '))