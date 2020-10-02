# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 23:54:59 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.linspace(0,0.25*np.pi,100)
z = np.linspace(0.25*np.pi,0.5*np.pi,100)
t = np.linspace(0.5*np.pi,0.75*np.pi,100)
s = np.linspace(0.75*np.pi,np.pi,100)

y = np.sin(x)**4 + np.cos(x)**4
u = np.sin(z)**4 + np.cos(z)**4 
v = np.sin(t)**4 + np.cos(t)**4
w = np.sin(s)**4 + np.cos(s)**4       

plt.plot(x,y)
fill_between(z,u,facecolor='orange')
plt.plot(t,v)
fill_between(s,w,facecolor='orange')
plt.grid()
plt.xlabel('0 < x < pi')
plt.ylabel('Sin(x)^4 + Cos(x)^4')
plt.savefig('problem 20.eps', format = 'eps')


