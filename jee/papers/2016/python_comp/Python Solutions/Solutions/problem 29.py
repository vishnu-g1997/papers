# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 16:38:43 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = (1/(2*x))*(np.log(1 + (np.tan(np.sqrt(x)))**2))
plt.plot(x,y)
plt.grid()
plt.xlabel('x')
plt.ylabel('log(p)')
plt.plot(0,0.5,'o')
plt.savefig('problem 29.eps',format = 'eps')

