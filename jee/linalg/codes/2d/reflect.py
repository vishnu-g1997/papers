import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
ax = plt.figure().add_subplot(111, aspect='equal')

#defining points
P = np.array([4.0,1.0])

#defining lines
n = np.array([1,-1])
c = 0
m = omat@n

n=n.reshape((2,1))
m=m.reshape((2,1))

R1 = ((m@m.T-n@n.T)/(m.T@m+n.T@n))@P
R2 = c*n/np.linalg.norm(n)
R2=R2.reshape((1,2))
R = 2*(R1+R2)
R = np.array(R)[0]
#Translation
t = np.array([2,0])
S = R+t

#Rotation
theta = np.pi/4
rot_mat = np.array(([np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]))
T = rot_mat@S

#printing points
print("P=\n",P)
print("R=\n",R)
print("S=\n",S)
print("T=\n",T)

A = np.array((c,0))
m = np.array(m.T)[0]

#Generating the line
x_AB = line_gen(A,(P+R)/2)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$L$')

#Plotting all points
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 - 0.05), R[1] * (1) , 'R')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 - 0.05), S[1] * (1) , 'S')
plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 - 0.05), T[1] * (1) , 'T')
ax.plot()

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('../figs/reflection.pdf')
plt.savefig('../figs/reflection.eps')
subprocess.run(shlex.split("termux-open ../figs/reflection.pdf"))
#else
#plt.show()
