# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 18:22:01 2017

@author: SS
"""

import numpy as np
import mpmath as mp

P = np.array([[np.sqrt(3)/2,0.5],[-0.5,np.sqrt(3)/2]]) 

A = np.array([[1,1],[0,1]])

B = np.matrix.transpose(P)

Q = np.dot(np.dot(P,A),B)
X = np.linalg.matrix_power(Q,2015)

print np.dot(np.dot(B,X),P)