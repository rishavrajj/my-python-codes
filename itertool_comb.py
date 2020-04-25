# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:17:05 2020

@author: rishav
"""

from itertools import combinations as cn
s = input().split()
[ print(''.join(i)) for i in sorted(list(cn(s[0],int(s[1])))) ]