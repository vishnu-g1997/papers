# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 15:04:05 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.abs(np.log(2) - np.sin(x))
def g(x):
    return f(f(x))

x = np.linspace(-1,1,100)

plt.plot(x,g(x))
plt.grid()
plt.xlabel('x')
plt.ylabel('g(x)')
plt.savefig('problem 30.eps',format = 'eps')

h = 10**(-10)

#right hand limit
print (g(h) - g(0))/h
     
#left hand limit
print (g(0) - g(-h))/h

print np.cos(np.log(2))