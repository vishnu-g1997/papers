#Program to plot  a ellipse
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
theta = np.linspace(0,2*np.pi,len)

#Given ellipse parameters
#Eqn : x.T@V@x + 2u.T@x+F=0
V = np.array(([5,-3],[-3,5]))
u = np.array([11,-13])
F = 29

eigval,eigvec = LA.eig(V)
#
D = np.diag(eigval)
P = eigvec
print("D=\n",D)
print("P=\n",P)
#Generating points on the ellipse at origin
y = np.zeros((2,len))
y[0,:] = 1/eigval[0]*np.cos(theta)
y[1,:] = 1/eigval[1]*np.sin(theta)

#Plotting standard ellipse
plt.plot(y[0,:],y[1,:],label='Ellipse at origin')

#Affine Transformation
c = (-1 * LA.inv(V) @ u).reshape((2,1))
print("c=\n",c)
x = P@y + c
#
#Plotting required ellipse
plt.plot(x[0,:],x[1,:],label='Affine Ellipse')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

#if using termux
plt.savefig('./conics/figs/ellipse.pdf')
plt.savefig('./conics/figs/ellipse.eps')
subprocess.run(shlex.split("termux-open ./conics/figs/ellipse.pdf"))
#else

#plt.show()
