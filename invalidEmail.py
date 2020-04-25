# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:17:58 2020

@author: rishav
"""

import string
def fun(s):
    # return True if s is a valid email, else return False
    if ('@' not in s) or ('.' not in s) or (' ' in s):

            return False

    if s.count('@')>1:

            return False
    
    alpha = list(string.ascii_letters)
    dig = list(string.digits)
    symbol = ['-','_','.']

    uname,domain = s.split('@')
    ws,ext,d_ext = domain.split('.')
    if(len(uname)==0):
        return False
    else:
        for i in range(len(uname)):
            if uname[i] not in (alpha + dig + symbol):
                return False
    if(len(ws)==0):
        return False
    else:
        for i in range(len(ws)):
            if ws[i] not in (alpha + dig):
                return False
    if(len(d_ext)>3 or len(ext)>3):
        return False
    elif(d_ext not in ['com','in','org','uk','usa','pk','eu','sin']):
        return False
    return True

    
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)