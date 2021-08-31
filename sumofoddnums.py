# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:47:05 2021

@author: Chelsea Sangma
This program finds the sum of the following series:
1+3+5+7+...+N

"""
sum=0
i=1
n=int(input("Enter n: "))
while i <= n:
    sum+=i
    print(i," ",end="")
    i+=2
    
print("\nResult = ",sum)
