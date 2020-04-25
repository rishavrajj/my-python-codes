# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:21:27 2020

@author: rishav


string = "ABCDCDCDC"
sub_str = "CDC"
p = string.find(sub_str)
print(p)
"""
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
#Middle Belt
for i in range((thickness+1)//2):
    print((c*(5*thickness)).center(thickness*6))
    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))