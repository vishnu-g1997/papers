#This program calculates the circumcentre of Triangle ABC
import numpy as np
from coeffs import *


#Triangle vertices
A,B,C=np.loadtxt('./codes/vert.dat', dtype='double')

print(ccircle(A,B,C))



