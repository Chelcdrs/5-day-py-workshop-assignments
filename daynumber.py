# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 01:47:10 2021

@author: Chelsea Sangma
This program prints the days of the week using nested if.
"""
print("7 days of the week!!\n\n")
day=int(input("Enter any day number: "))
if day==0 or day>7:
    print("Do you know that there are only 7 days in a week??\n")
    import sys
    sys.exit()
if day==1:
    print("You entered 1 so it is MONDAY!!")
elif day==2:
    print("You entered 2 so it is TUESDAY!!")
elif day==3:
    print("You entered 3 so it is WEDNESDAY!!")  
elif day==4:
    print("You entered 4 so it is THURSDAY!!")
elif day==5:
    print("You entered 5 so it is FRIDAY!!")
elif day==6:
    print("You entered 6 so it is SATURDAY!!")
else:
    print("You entered 7 so it is SUNDAY!!")