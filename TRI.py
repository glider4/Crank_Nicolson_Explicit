#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:47:23 2018
@author: mathemacode
TRI function (book pseudocode adaptation)

"""

''' TRI Function '''
def TRI(n, a, d, c, b, y):
    
    for i in range (2, n):
        xmult = a[i-1] / d[i-1]
        d[i] = d[i] - ( (xmult)*c[i-1] )
        b[i] = b[i] - ( (xmult)*b[i-1] )
        
    y[n-1] = ( b[n-1] / d[n-1] )
    
    for i in  range(n-2,0,-1):
        y[i] = ( (b[i] - ((c[i])*y[i+1])) ) / d[i]