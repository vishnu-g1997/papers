import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA

#Creating matrices
A=np.matrix('1 0; 1 1; 1 2')
b=np.matrix('6; 0; 0')
#Eigenvalue decompostion of A'A
Dv, Pv=LA.eig(A.T.dot(A))
#Eigenvalue decompostion of AA'
Du, Pu=LA.eig(A.dot(A.T))
#Singular values of A
Stemp=np.sqrt(Dv)
#QR Decomposition to get U and V
V, Rv=LA.qr(Pv)
U, Ru=LA.qr(Pu)
#SVD, A=USV
U_1, s, V_1=LA.svd(A)
print(V)
print(V_1)
print(U)
print(U_1)
print(s)
print(Stemp)

