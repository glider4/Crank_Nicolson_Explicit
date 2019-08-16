#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:44:00 2018
@author: mathemacode
Explicit Method, Parabolic Problems

"""

import numpy as np

''' Constants '''
m = 20
n = 10
h = 0.1
k = 0.005

''' Explicit Method '''
def explicit():
    u = np.zeros(n)
    v = np.zeros(n)
     
    u[0] = 0
    v[0] = 0
    u[n-1] = 0
    v[n-1] = 0
    
    for i in range(1, n-1):
        u[i] = np.sin(np.pi*i*h)
    
    for j in range(1, m):
        for i in range(1, n-1):
            v[i] = (u[i-1] + u[i+1]) / 2
            
        t = j*k
        for i in range(1, n-1):
            u[i] = np.exp((-(np.pi)**2)*t) * np.sin(np.pi*i*h) - v[i]
            
        for i in range(1, n-1):
            u[i] = v[i]
            
    return v
