#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:46:35 2018
@author: mathemacode
Crank-Nicolson Method, Parabolic Problem

"""

import numpy as np
from TRI import TRI

''' Constants '''
m = 20
n = 10
h = 0.1
k = 0.005

''' Crank Nicolson Method '''
def crank():
    c = np.zeros(n)
    d = np.zeros(n)
    u = np.zeros(n)
    v = np.zeros(n)
    
    s = (h**2)/k
    r = 2 + s
    
    for i in range(1, n-1):
        d[i] = r
        c[i] = -1
        u[i] = np.sin(np.pi*i*h)
        
    for j in range(1, m):
        for i in range(1, n-1):
            d[i] = r
            v[i] = s*u[i]
            
        TRI(n-1, c, d, c, v, v)
        
        t = j*k
        for i in range(1, n-1):
            u[i] = np.exp((-(np.pi)**2)*t) * np.sin(np.pi*i*h) - v[i]
            
        for i in range(1, n-1):
            u[i] = v[i]
        
    return v
