# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 00:07:47 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.linspace(0,(np.pi)/6,100)
B = (np.pi)/6 - A

y = np.tan(A) + np.tan(B)

min_y = np.min(y)
min_x = (np.pi)/12
        
plt.plot(A,y)
plt.plot(min_x,min_y,'o')
plt.grid()
plt.ylabel('tan(A) + tan(B)')
plt.xlabel('A (Radians)')
plt.savefig('problem 25.eps',format = 'eps')