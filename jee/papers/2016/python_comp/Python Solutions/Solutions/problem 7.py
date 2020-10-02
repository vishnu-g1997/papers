# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 20:12:38 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(-5,5,100)
d = np.sqrt(k**2 + k + 4)

dist = np.min(d)*np.ones(100)

plt.figure(1)
plt.plot(k,d,label = 'd')
plt.plot(k,dist,label = 'min d')
plt.grid()
plt.legend()
plt.savefig('problem 7_1.eps', format = 'eps')

x = np.linspace(-2.5,2.5,100)
y = x**2 - 4

plt.figure(2)
plt.plot(x,y)
plt.ylim(-6,1)
plt.xlim(-2.5,2.5)
plt.plot(np.sqrt(3.5),-0.5,'o')
plt.plot(-np.sqrt(3.5),-0.5,'o')
plt.plot(0,0,'o')
plt.text(-np.sqrt(3.5)+0.1,-0.5,'P')
plt.text(np.sqrt(3.5)+0.1,-0.5,'Q')
plt.text(0.1,0,'O')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('problem 7_2.eps', format = 'eps')