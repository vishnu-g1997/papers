import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA

A=np.matrix('1 0; 1 1; 1 2')
b=np.matrix('6; 0; 0')

x1=np.linspace(-10, 10, 50)
x2=np.linspace(-10, 10, 50)
w, h = 50, 50;
#f = np.matrix([[1 for x in range(w)] for y in range(h)]) 
f = np.zeros((w,h))
xx, yy=np.meshgrid(x1, x2)
print(f)

for i in range (1, 50):
	for j in range (1, 50):
		f[j][i]=LA.norm(b-np.dot(A, np.array([[xx[j]], [yy[j]]])))**2
M=np.amin(f)
print (M)
