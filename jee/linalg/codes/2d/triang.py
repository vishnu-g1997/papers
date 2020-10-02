import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
ax = plt.figure().add_subplot(111, aspect='equal')

#defining points
A =  np.array([1.0,2.0])

#Normal vectors
n_1 = np.array([1.0,1.0])
n_2 = np.array([1.0,0])
#Normal matrix
N = np.vstack((n_1,n_2))


#finding centroid O
c = np.array([5,4])
O = np.linalg.inv(N)@c

#finding vertex C
c_1 =  np.array([7,4])
C = np.linalg.inv(N)@c_1

#finding vertex B
B = np.array([11,1]) - C

#Saving vertices to file
np.savetxt('./codes/vert.dat', (A,B,C))
#Area of triangle ABC
tri_mat = np.vstack((A,B,C))
tri_mat = np.hstack(((tri_mat),np.ones((3,1))))
#print(np.transpose(A.T))

#printing points
print("A=\n",A)
print ("O=\n",O)
print ("C=\n",C)
print ("B=\n",B)
print ("Area=\n",0.5*np.linalg.det(tri_mat))

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.05), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

ax.plot()

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('./line/figs/triangle.pdf')
plt.savefig('./line/figs/triangle.eps')
subprocess.run(shlex.split("termux-open ./line/figs/triangle.pdf"))
#else
#plt.show()
