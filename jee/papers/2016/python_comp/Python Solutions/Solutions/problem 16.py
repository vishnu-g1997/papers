# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 23:14:23 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,2,100)
z = 1 + 1j*a
y = imag(z**3)
a_t = np.roots([-1,0,3,0])
ind = np.nonzero(a_t > 0)
a_v = a_t[ind]
plt.plot(a,y)
plt.plot(a_v,0,'o')
plt.ylabel('Im(z)')
plt.xlabel('a')
plt.grid()
plt.savefig('problem 16.eps',format = 'eps')