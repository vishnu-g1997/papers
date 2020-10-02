# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 15:24:46 2017

@author: SS
"""

import numpy as np
import matplotlib.pyplot as plt

maxlen = 20
p = []
x = np.linspace(1,maxlen,maxlen)
for n in range(1,maxlen+1):
    l = n
    product = []
    for k in range(1,2*n + 1):
        l = l + 1
        product.append(double(l))
    p.append((np.prod(product)/(n**(2*n)))**(1.0/n)) 
    
plt.stem(x,p)

sol = np.array([18.0/np.exp(4),27.0/np.exp(2),9.0/np.exp(2),3*np.log(3) - 2])
y = np.ones(maxlen)
plt.plot(x,y*sol[0],label = '18/e^4')
plt.plot(x,y*sol[1],label = '27/e^2')
plt.plot(x,y*sol[2],label = '9/e^2')
plt.plot(x,y*sol[3],label = '3log(3) - 2')
plt.grid()
plt.legend()
plt.xlabel('n')
plt.ylabel('p_n')
plt.savefig('problem 32.eps', format = 'eps')
