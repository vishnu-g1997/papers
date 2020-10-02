# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 18:36:19 2017

@author: SS
"""

import numpy as np
import math as mp

#numerical
def nCr(n,r):
    return mp.factorial(n)/(mp.factorial(r)*mp.factorial(n-r))
s = 0
for r in range (1,16):
        s += nCr(15,r)*r**2/nCr(15,r-1)
print s

#theoretical
r = 15
print (-2*r**3 +45*r**2 + 47*r)/6
