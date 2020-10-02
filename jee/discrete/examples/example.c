#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main() //main function begins
{

//Defining the variables
int m,n, len ;//integers
double **a,**P,**Q,**mat,**c,**temp, r, **O, **mat_inv;
double **n_1,**n_2,**n_3,**n_4, **temp1,**theta;
double c_1,c_2,c_3,c_4;
//Generate line points
len = 100;

//Given points
P = loadtxt("./data/P.dat",2,1);
Q = loadtxt("./data/Q.dat",2,1);

//Matrix equation
mat = loadtxt("./data/mat.dat",2,2);
c = loadtxt("./data/c.dat",2,1);

//Circle centre and radius
mat_inv = linalg_inv(mat,2);
O = matmul(mat_inv,c,2,2,1);

//Finding the difference of matrices
temp = linalg_sub(O,P,2,1);

//Finding the norm
r = linalg_norm(temp,2);

free(temp);

//print(O,2,1);//printing the matrix O
//printf("\n %lf\n",r);//printing the radius r

//(i)
n_1 = loadtxt("./data/n_1.dat",2,1);
c_1 =  6;

//(ii)
n_2 = loadtxt("./data/n_2.dat",2,1);
c_2 =  -10;

//(iii)
n_3 = loadtxt("./data/n_3.dat",2,1);
c_3 =  3;

//(iv)
n_4 = loadtxt("./data/n_4.dat",2,1);
c_4 =  -4;

temp = matmul(transpose(n_1,2,1),O,1,2,1);


if ( temp[0][0]== c_1)
	printf("\n (i) is  a diameter\n");
else
	printf("\n(i) is not a diameter\n");

free(temp);

temp = matmul(transpose(n_2,2,1),O,1,2,1);


if ( temp[0][0]== c_2)
	printf("\n (ii) is  a diameter\n");
else
	printf("\n(ii) is not a diameter\n");

free(temp);

temp = matmul(transpose(n_3,2,1),O,1,2,1);


if ( temp[0][0]== c_3)
	printf("\n (iii) is  a diameter\n");
else
	printf("\n(iii) is not a diameter\n");

free(temp);

temp = matmul(transpose(n_4,2,1),O,1,2,1);


if ( temp[0][0]== c_4)
	printf("\n (iv) is  a diameter\n");
else
	printf("\n(iv) is not a diameter\n");

free(temp);

//Generating theta

theta = linspace(0,2*M_PI,len);
//print(theta,len,1);//printing theta
savetxt(theta,"theta.dat",len,1);


free(P);
free(Q);
free(mat);
free(mat_inv);
free(O);
free(c);
return 0;
}


