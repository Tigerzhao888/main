# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math


G=6.674*10**-11
M=5.97*10**24
R=6.37*10**6
T=input("Please specify the orbital period of the satellite:")
string1=T

stringList=string1.split(' ')
TP=float(stringList[0])
if stringList[1]=='mintues':
    Tn=TP*60
    if stringList[1]=='hours':
        Tn=TP*3600
    if stringList[1]=='days':
        Tn=TP*24*3600
        
    
r=(G*M*Tn**2/(4*math.pi**2))**(1/3)
h=(r-R)/1000

if h>0:
    print(h)
else:
    print('orbit is not possible')

while True:
    again = input("Run again? (y/n): ")
    T = input("Please specify the orbital period of the satellite:")
    if again != 'y':
        print("Program ended.")
        break
