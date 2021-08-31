# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:25:39 2021

@author: Chelsea Sangma
A python program to find the largest of three numbers
"""

n1=int(input("Type the first number: "))
n2=int(input("Type the second number: "))
n3=int(input("Type the third number: "))

if n1>n2 and n1>n3:
    largest=n1
elif n2>n1 and n2>n3: 
    largest=n2
else:
    largest=n3

print("\nThe largest number out of the three input numbers are: ", largest)