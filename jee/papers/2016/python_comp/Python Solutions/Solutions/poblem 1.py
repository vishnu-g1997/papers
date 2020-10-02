# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 19:46:05 2017

@author: SS
"""

import numpy as np

def fn(n,x):
    if n % 3 == 1:
        return 1/(1-x)
    elif n % 3 == 2:
        return fn(1,fn(1,x))
a = fn(1,fn(100,3))
b = fn(1,fn(1,2.0/3))
c = fn(1,fn(2,3.0/2))

print a+b+c