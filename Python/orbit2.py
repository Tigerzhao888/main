# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

import numpy as np

G=6.674*10**-11
M=5.97*10**24
R=6.37*10**6
T=int(input("Please specify the orbital period of the satellite:"))

r=(G*M*T**2/(4*math.pi**2))**(1/3)
h=(r-R)/1000


print (f"The altitude is:{h} km")
