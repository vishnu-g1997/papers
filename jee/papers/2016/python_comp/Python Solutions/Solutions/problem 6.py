# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 19:43:22 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,1.2,100)
x = 4*t**2 + 3
y = 8*t**3 - 1
z = 3*(x-7) + 7
plt.plot(x,y,label = 'curve')
plt.plot(x,z,label = 'tangent')
plt.plot(7,7,'o')
plt.plot(4,-2,'o')
plt.grid()
plt.text(7,8,'P')
plt.text(4,-4,'Q')
plt.legend()
plt.savefig('problem 6.eps', format = 'eps')