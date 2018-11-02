#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:23:24 2018
@author: mathemacode

3D Plot of the exact solution 
of the parabolic heat equation problem, just for 
refernce and comparison to estimations.

"""

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def exact():  # 3D plotting of solution for reference
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.arange(0, 1, 0.1)
    t = np.arange(0, 0.1, 0.005)
    t, x = np.meshgrid(t, x)
    z = np.exp((-(np.pi)**2)*t) * np.sin(np.pi*x*0.1)
    
    # Format 3D plot itself
    ax.plot_surface(t, x, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    
    # Additional settings
    ax.set_zlim(0, 0.35)
    plt.title("Exact Solution")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.show()
