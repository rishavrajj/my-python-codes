# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:04:52 2020

@author: rishav
"""
class Employee:
    def __init__(self,eid,ename,role,salary):
        self.emp_id = eid
        self.emp_name = ename
        self.emp_role = role
        self.emp_salary = salary
    def increase_salary(self,percent):
        self.emp_salary+=self.emp_salary*percent*0.01
class Organisation:
    def __init__(self,name,elist):
        self.org_name=name
        self.emp_list=elist
if __name__ == '__main__':
    emp_list = []
    count = int(input())
    for i in range(count):
        eid = int(input())
        name = input()
        role=input()
        salary=int(input())
        emp_list.append(Employee(eid,name,role,salary))
    o = Organisation("XYZ Corp",emp_list)
    inp_role=input()
    inp_percent=int(input())
    result=o.calculate_increment(inp_role,inp_percent)
    if len(result)!=0:
        for emp in result:
            print(emp.emp_name,'\t',emp.emp_salary)
    else:
        print('No Employee found with the given role!')