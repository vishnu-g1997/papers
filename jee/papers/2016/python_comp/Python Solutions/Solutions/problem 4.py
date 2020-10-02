# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 18:44:52 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

x = 1e3
a = np.linspace(0,2,100)
y = (1 + a/x -4/x**2)**(2*x)
z = ((np.exp(1))**3)*np.ones(100)
plt.plot(a,z, label = 'e^3')
plt.plot(a,y, label = 'Limit value')
plt.grid()
plt.legend()
plt.xlabel('a')
plt.savefig('problem 4.eps', format = 'eps')
plt.show()
