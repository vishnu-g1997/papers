from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid([-10,10], [-10,10])
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')


#defining direction vectors of planes
A = np.array([2.0,3.0,-1.0])
B = np.array([0.0,1.0,1.0])

#finding cross product
cp = np.cross(A,B)

#plotting points
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.scatter(A[0],A[1],A[2],'o',label="Point A")

#plotting lines
plt.plot([0,A[0]],[0,A[1]],[0,A[2]],label="Vector A")
plt.plot([0,B[0]],[0,B[1]],[0,B[2]],label="Vector B")
plt.plot([0,cp[0]],[0,cp[1]],[0,cp[2]],label="Cross Product Vector")

#printing direction vectors
print("Vector A=",A)
print("Vector B=",B)
print("Cross Product= \n",cp)

#show plot
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
#if using termux
plt.savefig('../figs/4.2.pdf')
plt.savefig('../figs/4.2.eps')
subprocess.run(shlex.split("termux-open ../figs/4.2.pdf"))
#else
#plt.show()
