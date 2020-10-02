# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 19:18:54 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt
x1 = 1
x2 = np.linspace(-1,1,1000)
x3 = np.linspace(1,2,1000)
b = -x1
a = -x1-np.arccos(b+x1)
y = -x2
z = a + np.arccos(b+(x3))
plt.plot(x3,z, label = 'f(x) = -x')
plt.plot(x2,y, label = 'f(x) = a + acos(x+b)')
plt.grid()
plt.legend()
plt.savefig('problem5.eps',format = 'eps')
