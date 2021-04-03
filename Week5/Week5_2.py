import numpy as np
import matplotlib.pyplot as plt

#5주차 QUIZ
# #Problem1
# #1-1
# #x=[0,1,2]
# #b[0]= y[0]
# #b[1]= (y[1]-y[0])/0.1
# #b[2]= (y[2]-y[1])/0.1
# #b[3]= (y[3]-y[2])/0.1

# #1-2
# n=100
# x=np.zeros(n)
# A= 10*np.eye(n)-10*np.eye(n,k=-1)
# b=np.zeros(n)
# for i in range(0,n):
#     b[i]= i * 0.4 
# x=np.zeros(n)
# for i in range(0,n):
#     x[i]= i * 0.1 

# #1-3
# y=np.zeros(n)
# y[0]=10
# for k in range(1,n):
#     y[k]= (b[k]-np.dot(A[k,:],y))/A[k,k]
    
# y_2=2*x*x+10

# plt.plot(x,y)
# plt.plot(x,y_2)
# plt.show()

# #1-4
# B=np.eye(n)
# y=np.zeros((n,n))
# for j in range (0,n):
#     for i in range(0,n):
#         y[i,j]= (B[i,j]-np.dot(A[i,:],y[:,j]))/A[i,i]
# print(y)
# print(A@y)


# #Problem2
# #2-1
# #[y1,y2,y3,y4]=[6,6,1,6]y3

#수업
from ch2 import *
n=5
A= 2*np.eye(n)+np.eye(n, k=-1)+np.eye(n,k=+1)
b=np.zeros(n)
b[0]=1

def Av(v):
    global A
    n=len(v)
    x=np.zeros(n)
    x[0]= A[0,0]*v[0] + A[0,1]*v[1]
    x[n-1]= A[n-1,n-2]*v[n-2] + A[n-1,n-1]*v[n-1]
    for i in range(1,n-1):
        x[i]= A[i,i-1]*v[i-1] +A[i,i]*v[i] +A[i,i+1]*v[i+1]
    return x

x=np.zeros(n)
vsol,inter=conjGrad(Av,x,b)
print(vsol,inter)















