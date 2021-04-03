import numpy as np
import time 
from ch2 import *
start=time.time()

# #Problem1
# #기본 설정
A=np.array([[2,-1,0,0,0],[-1,4,-1,0,0],[0,-1,4,-1,-2],[0,0,-1,2,-1],[0,0,-2,-1,3]])
b=(1/2.5)*np.ones(5)
n=len(b)

x=np.zeros((n,n+1))
r=np.zeros((n,n))
s=np.zeros((n,n))
d=np.zeros(n)
a=np.zeros(n)

#Complex Conjugate 실행
#First Iteration
r[:,0]=b- A@x[:,0]    #Residual
s[:,0]= r[:,0].copy() #탐색방향
a[0]= s[:,0]@r[:,0]/(s[:,0]@A@r[:,0])         #Scailing Factor
#Update x 
x[:,1]= x[:,0]+ a[0]*s[:,0] 
#Iterations
for j in range(1,n):
    r[:,j]=b- A@x[:,j]    #새로운 Residual             
    d[j-1]= -r[:,j]@A@s[:,j-1]/(s[:,j-1]@A@s[:,j-1]) #탐색방향을 찾는 계수2
    s[:,j]= r[:,j]+ d[j-1]*s[:,j-1] #새로운 탐색방향 벡터
    a[j]= s[:,j]@r[:,j]/(s[:,j]@A@r[:,j])
    x[:,j+1]= x[:,j]+ a[j]*s[:,j]
print(x)
print(A@x[:,n])
#x=[0.56,0.72,1.92,2.24,2.16]

#Problem2
n=10
A=4*np.eye(n)-np.eye(n,k=-1)-np.eye(n,k=1)
b=5*np.ones(n)
b[0]=9

x=np.zeros((n,n+1))
r=np.zeros((n,n))
s=np.zeros((n,n))
d=np.zeros(n)
a=np.zeros(n)

#Complex Conjugate 실행
#First Iteration
r[:,0]=b- A@x[:,0]    #Residual
s[:,0]= r[:,0].copy() #탐색방향
a[0]= s[:,0]@r[:,0]/(s[:,0]@A@r[:,0])         #Scailing Factor
#Update x 
x[:,1]= x[:,0]+ a[0]*s[:,0] 
#Iterations
for j in range(1,n):
    r[:,j]=b- A@x[:,j]    #새로운 Residual             
    d[j-1]= -r[:,j]@A@s[:,j-1]/(s[:,j-1]@A@s[:,j-1]) #탐색방향을 찾는 계수2
    s[:,j]= r[:,j]+ d[j-1]*s[:,j-1] #새로운 탐색방향 벡터
    a[j]= s[:,j]@r[:,j]/(s[:,j]@A@r[:,j])
    x[:,j+1]= x[:,j]+ a[j]*s[:,j]
# print(x[:,n])
# print(A@x[:,n])
print(time.time()-start)
# Conjugate Gradient x= [2.90191936 2.60767745 2.52879042 2.50748425 2.50114659 2.4971021 2.48726181 2.45194513 2.3205187  1.83012968]
# Gauss Elimination x= [2.90191936 2.60767745 2.52879042 2.50748425 2.50114659 2.49710212.48726181 2.45194513 2.3205187  1.83012968]
# Conjugate gradient:0.001332 0.0014822 0.00555
# Gauss Elimin 0.0002694 0.000378608 0.003645 

#Problem3
A=np.array([[1,0,1],[0,1,0],[0,0,1]])
b=np.array([0,0,1])
n=len(b)
x_0=np.array([-1,0,0])

# #First Iteration
# r_0=b- A@x_0    #Residual
# s_0= np.array([0,0,1]) #탐색방향
# a_0= s_0@r_0/(s_0@A@r_0)         #Scailing Factor
# print(a_0)
# #Update x 
# x_1= x_0+ a_0*s_0 
# print(x_1)

# #Second Iteration
# r_1=b- A@x_1    #새로운 Residual             
# b_0= -r_1@A@s_0/(s_0@A@s_0) #탐색방향을 찾는 계수2
# print(b_0) 
# print(r_1)# r_1=[0,0,0] ,b_0=0
# s_1= r_1+ b_0*s_0 #새로운 탐색방향 벡터
# print(s_1) # s_1이 0이 되므로 값을 더이상 구할수 업게 됨

x=np.linalg.inv(A)@b
print(x)
