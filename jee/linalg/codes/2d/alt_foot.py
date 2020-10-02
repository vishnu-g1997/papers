#This program calculates the foot of the altitude of Triangle ABC
import numpy as np
from coeffs import *

#Triangle vertices
A,B,C=np.loadtxt('./codes/vert.dat', dtype='double')

m = dir_vec(B,C)
n = norm_vec(B,C)
p = np.zeros(2)
p[0] = m@A
p[1] = n@B

#Intersection
N=np.vstack((m,n))
P=np.linalg.inv(N)@p
print(P)



