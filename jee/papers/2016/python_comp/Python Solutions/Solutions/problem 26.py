# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 00:16:29 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.5*np.pi,0.5*np.pi,100)
im_z = (2 - 6*np.sin(t)**2)/(1 + 4*np.sin(t)**2)
plt.plot(t,im_z)
plt.plot(-np.arcsin(1/np.sqrt(3)),0,'o')
plt.plot(np.arcsin(1/np.sqrt(3)),0,'o')
plt.grid()
plt.xlabel(r"$\dot{\Theta}$ (Radians)")
plt.ylabel('Imaginary part')
plt.savefig('problem 26.eps',format = 'eps')
