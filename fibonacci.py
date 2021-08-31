# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:18:51 2021

@author: Chelsea Sangma
This programs prints the first 10 terms of fiboacci series.
"""
a=0
b=1
nt=a+b
print("The first 10 FIBONACCI SERIES: ",a,", ",b,", ",nt,end="")
for i in range(3, 10):
    a=b
    b=nt
    nt=a+b
    print(", ",nt,end="")
