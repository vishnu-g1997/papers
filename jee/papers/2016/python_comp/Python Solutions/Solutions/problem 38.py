# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 19:12:20 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_point(Q,t,O1,O2):
    plt.plot(Q[0],Q[1],'o')
    plt.text(Q[0]+O1,Q[1]+O2,t)

a = 1.5
b = np.sqrt(3)/2
e = np.sqrt(1 + (b/a)**2)
print e
x = np.linspace(-4,4,1000)
y1 = b*np.sqrt((x/a)**2 - 1)
y2 = -y1

plt.plot(x,y1)
plt.plot(x,y2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')

F1 = [a*e,0]
F2 = [-a*e,0]
plot_point(F1,'F1',0.15,-0.1)
plot_point(F2,'F2',-0.45,-0.1)
plt.savefig('problem 38.eps',format = 'eps') 