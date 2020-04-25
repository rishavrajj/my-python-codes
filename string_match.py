# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:15:14 2020

@author: rishav
"""

string = "ABCDCDC"
sub_str = "CDC"
count = 0
i=0
while(string[i] is None):
    c=0
    for j in range(0,len(sub_str)):
        if(sub_str[j]==string[c]):
            c+=1
        if(c==len(sub_str)):
            count+=1
    i+=1
print(count)

            
    