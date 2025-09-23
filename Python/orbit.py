#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 01:04:52 2025

@author: zhaozhihao
"""
import math
import numpy as np
    
G=6.674*10**-11
M=5.97*10**24
R=6.37*10**6
T=np.array([94*60,4*3600, 6*3600, 24*3600])

r=(G*M*T**2/(4*math.pi**2))**(1/3)
h=(r-R)/1000


print (h)