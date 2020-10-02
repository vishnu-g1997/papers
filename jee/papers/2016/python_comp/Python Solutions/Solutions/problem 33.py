# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 15:44:53 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(0,4,100)

y1 = np.sqrt(2*x)
y2 = np.sqrt(4*x - x**2)
z = np.maximum(y1,y2)
fill_between(x,z)
fill_between(x,y1)
plt.grid()
plt.savefig('problem 33.eps',format = 'eps')