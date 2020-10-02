# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 23:10:34 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5,5,100)
y = np.sqrt(2*x + 1) - np.sqrt(2*x - 1) - 1
plt.plot(x,y)
plt.plot(5.0/8,0,'o')
plt.grid()
plt.text(5.0/8 + 0.1,0,'P')
plt.savefig('problem 15.eps',format = 'eps')