#This program calculates the incentre of Triangle ABC
import numpy as np
from coeffs import *

#Triangle vertices
A,B,C=np.loadtxt('./codes/vert.dat', dtype='double')
k1 = 1
k2 = 1
I,r = icentre(A,B,C,k1,k2)
print(I,r)




