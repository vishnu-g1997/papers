# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 23:02:02 2017

@author: SS
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.sqrt(3),3*np.sqrt(3),1000)
y = np.sqrt(3*(1-(x**2)/27))
z = -np.sqrt(3*(1-(x**2)/27))
plt.plot(x,y)
plt.plot(x,z)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('problem 13.eps',format = 'eps')
