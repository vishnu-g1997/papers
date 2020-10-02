#This program calculates the orthocentre of Triangle ABC
import numpy as np
from coeffs import *

#Triangle vertices
A,B,C=np.loadtxt('./codes/vert.dat', dtype='double')

p = np.zeros(2)

#AP
n1 = dir_vec(B,C)
p[0] = n1@A
#BQ
n2 = dir_vec(C,A)
p[1] = n2@B

#Intersection
N=np.vstack((n1,n2))
H=np.linalg.inv(N)@p
print(H)



