# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 20:26:25 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

#Point of intersection
A = np.array([[1.0/3,1.0/4] , [1.0/4,1.0/3]])
B = np.array([1,1])
U = np.dot(np.linalg.inv(A),np.transpose(B))
print U

#Sketching tThe curve
h = np.linspace(0.5,5.9/7,50)
h2 = np.linspace(6.1/7,1.2,50)
k = 1/(7.0/6 - 1/h)
k2 = 1/(7.0/6 - 1/h2)
plt.stem(h,k)
plt.stem(h2,k2)
plt.xlabel('h')
plt.ylabel('k')
plt.grid()
plt.savefig('problem 9.eps',format = 'eps')