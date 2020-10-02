# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 21:05:40 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(1,4,100)

y1 = 1-x
y2 = x**2 - 5*x + 4
X = np.concatenate([x,x[::-1]])
Y = np.concatenate([y1,y2[::-1]])
fill(x,y2)
fill(X,Y)
plt.grid()
plt.savefig('problem 8.eps',format = 'eps')