from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

#defining direction vectors of planes
l1 = np.array([1,1,0])
l2 = np.array([-3,5,7])

#finding cross product
cp = np.cross(l1,l2)

#plotting lines
plt.plot([0,l1[0]],[0,l1[1]],[0,l1[2]],label="Direction Vector of L1")
plt.plot([0,l2[0]],[0,l2[1]],[0,l2[2]],label="Direction Vector of L2")
plt.plot([0,cp[0]],[0,cp[1]],[0,cp[2]],label="Cross Product Vector")

#printing direction vectors
print("Direction Vector of L1=",l1)
print("Direction Vector of L2=",l2)
print("Cross Product= \n",cp)

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
plt.savefig('../figs/2.1.pdf')
plt.savefig('../figs/2.1.eps')
subprocess.run(shlex.split("termux-open ../figs/2.1.pdf"))
#else
#plt.show()

	

