#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:17:37 2018
@author: mathemacode

Plots both the explicit and Crank-Nicolson
Methods for Parabolic problems, pseudocodes taken 
from book.  3D exact solution plot is also included.

Use a=1 for plots on same graphic, a=2 for dual plots
lined up side-by-side for analysis.  Also, I made a function
to compare to the exact solution for the heat equation.  
It will plot secondary to the methods.

"""
import matplotlib.pyplot as plt

from Explicit import explicit
from Crank import crank
from Heat3Dplot import exact

n = 10

def main():  
    methods_plot(1)  # a = 1 for both on same plot, 2 for side-by-side
    exact()
    
    
def methods_plot(a):

    if a == 1:  # Single plot, two lines
        plt.plot(explicit(), 'b-o')
        plt.plot(crank(), 'r--')
        plt.title("Heat Equation Parabolic Methods Results")
        plt.xlim(0, n)
        plt.ylim(0,0.35)
        plt.xlabel("n")
        plt.ylabel("Value")
        plt.legend(['Explicit', 'Crank-Nicolson'], loc='upper left')
        plt.show()
    
    elif a == 2:  # Double plot, individual lines
        ''' Plot Results of Explicit '''
        plt.subplot(121)
        plt.plot(explicit(), 'b-o')
        plt.xlim(0, n)
        plt.ylim(0, 0.35)
        plt.title("Explicit Method Result")
        plt.xlabel("n")
        plt.ylabel("Value")
            
        ''' Plot Results of Crank-Nicolson Method '''
        plt.subplot(122)
        plt.plot(crank(), 'r-o')
        plt.xlim(0, n)
        plt.ylim(0,0.35)
        plt.xlabel("n")
        plt.title("Crank-Nicolson Method Result")
        
        plt.show()

main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
