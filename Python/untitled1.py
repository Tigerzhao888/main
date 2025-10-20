#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 03:03:25 2025

@author: zhaozhihao
"""

import math
import numpy as np
import matplotlib.pyplot as mp
from fun import falling1D, rising1D

g=9.8 

def projectile(v0, angle_deg, h0):

    theta=math.radians(angle_deg)
    v0x=v0*math.cos(theta)          # V horizontal 
    v0y=v0*math.sin(theta)          # V vertical
    
    h_up, t_up=rising1D(v0y)         
    hmax=h0+h_up                   

    t_down, vfy=falling1D(hmax, v0=0)   # fall from hmax to ground
    T=t_up+t_down

    R=v0x*T                         # Range
    vf=math.hypot(v0x, vfy)         # final velocity 

    return [round(vf, 2), round(R, 2), round(T, 2), round(hmax, 2)]


def projgraph(v0, angle_deg, h0):
    vf, R, T, hmax=projectile(v0, angle_deg, h0)
    theta=math.radians(angle_deg)
    v0x=v0*math.cos(theta)
    
    x=np.linspace(0, R, 500)
    y=h0+x*math.tan(theta)-(g*x**2)/(2*v0x**2)
    
    mp.figure()
    mp.plot(x, y, label="Trajectory")
    mp.axhline(0, color='k', linewidth=1)
    mp.xlabel("x (m)")
    mp.ylabel("y (m)")
    mp.title(f"Projectile Motion (v0={v0} m/s, angle={angle_deg}degree, initial height={h0} m)")
    mp.grid(True)
    
    return (round(R, 2), round(hmax, 2))


if __name__== "__main__":
    v0, ang, h0=62.0, 35.0, 26.5

    result=projectile(v0, ang, h0)
    print("[vf, R, T, hmax] =", result)  

    R, hmax=projgraph(v0, ang, h0)
    print("Range and max height from graph:", round(R, 2), round(hmax, 2))