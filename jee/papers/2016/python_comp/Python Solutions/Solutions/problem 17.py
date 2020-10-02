# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 23:20:44 2017

@author: SS
"""

import numpy as np

A = np.array([[-4,-1],[3,1]])
B = np.dot(A,A)
print np.linalg.det(B - 2*A - np.identity(2))