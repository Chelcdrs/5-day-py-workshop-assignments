# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:33:03 2021

@author: Chelsea Sangma
"""
print("This program checks whether the enetered number is a prime number or not\n")
n=int(input("Type a number: "))
if n>1:
    for i in range(2, n):
        if(n%i)==0:
            print(n," is not prime")
            break
    else:
        print(n," is prime")          
else:
    print(n," is not prime")
