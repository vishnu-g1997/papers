#Code by GVV Sharma
#January 28, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Triangle vertices
A,B,C=np.loadtxt('./codes/vert.dat', dtype='double')
print(A,B,C)

#Foots of the altitudes
P = alt_foot(A,B,C)
Q = alt_foot(B,C,A)
R = alt_foot(C,A,B)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AP = line_gen(A,P)
x_BQ = line_gen(B,Q)
x_CR = line_gen(C,R)
x_CP = line_gen(C,P)
x_CQ = line_gen(C,Q)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_BQ[0,:],x_BQ[1,:],label='$BQ$')
plt.plot(x_CR[0,:],x_CR[1,:],label='$CR$')
plt.plot(x_CP[0,:],x_CP[1,:])
plt.plot(x_CQ[0,:],x_CQ[1,:])

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid() # minor

#if using termux
plt.savefig('./line/figs/alt_triangle.pdf')
plt.savefig('./line/figs/alt_triangle.eps')
subprocess.run(shlex.split("termux-open ./line/figs/alt_triangle.pdf"))
#else
#plt.show()







