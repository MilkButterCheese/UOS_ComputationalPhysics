import numpy as np
from ch2 import *
#역행렬 복습
#반복 반습 Iterative Method
#공액경사법 Conjugate gradient Method

#A@X=B 문제에서 B가 Identity mtr면 X는 Inverse mtr 이다.
# A= np.array([[0.6,-0.4,1],[-0.3,0.2,0.5],[0.6,-1.0,0.5]])
# B= np.eye(3)

# Aori=A.copy()
# LU, seq= LUdecompp(Aori)
# x0=LUsolvee(LU,B[0,:],seq)
# x1=LUsolvee(LU,B[1,:],seq)
# x2=LUsolvee(LU,B[2,:],seq)

# # print(LU)
# # print(seq) #피봇값들 모아둔거
# # X=np.array([x0,x1,x2]).T
# # print(X)
# # print(A@X)

# n= len(Aori)
# X=np.zeros((n,n))

# for i in range(0,n):
#     X[:,i]= LUsolvee(LU,B[:,i],seq)
    
# print(X)
# print(A@X)
    
# #함수 형태로 만들기
# def inverse(A):
#     for i in range(0,n):
#         X[:,i]= LUsolvee(LU,B[:,i],seq)
#     return X 

# print(inverse(A))
    
#sparse matrix > 삼중대각행렬일땐?
# n=6
# A= 2*np.eye(n)-1*np.eye(n,k=-1)-1*np.eye(n,k=1) 
# A[n-1,n-1]=5
# B=np.eye(n)
# X=np.zeros((n,n))

# c= -1*np.ones(n-1)
# d=  2*np.ones(n)
# e= -1*np.ones(n-1)

# c, d, e =LUdecomp3(c,d,e)

# for i in range(0,n):
#     X[:,i]= LUsolve3(c,d,e,B[:,i])

# print(X)
# print(A@X)

#Iterative Method
#A@x=b에서 x의 어림값 x_0를 알때 
#min(f(x_0)) -> Optimization 
#A@x_0=b'
#A(x-x_0)=b-b' : 이떄 b-b'을 residual이라 부른다.
#Sparse Matrix의 경우 큰 크기의 행렬을 굳이 저장하지 않고 풀어 경제적
#x_0 ->x_1 ->x_2 ->x_3 -> ... ->x_n으로 수렴하면 답이된다.
# A_ij *x_j = A_ii * x_i + A_ij * x_j(i !=j로 sum)=b_i
#x_i=(b_i- A_ij * x_j(i !=j로 sum))/A_ii

# A=np.array([[4.,-1,1],[-1,4,-2],[1,-2,4]])
# b=np.array([12.,-1,5])
# x=np.zeros(3)
# w=1 

# x[0]= (1/A[0,0]) *(b[0]-(A[0,1]*x[1]+A[0,2]*x[2]))
# x[1]= (1/A[1,1]) *(b[1]-(A[1,0]*x[0]+A[1,2]*x[2]))
# x[2]= (1/A[2,2]) *(b[2]-(A[2,0]*x[0]+A[2,1]*x[1]))
#이 x값이 저장되도록 할려면 어떻게 해야하지?
#값이 발산하는 문제 발생

# A=np.array([[3.,-3,3],[-3,5,1],[3,1,5]])
# b=np.array([9.,-7,12])
# x=np.zeros(3)
# w=1 
# x=np.linalg.solve(A,b)                 
# for i in range(0,3):
#     x[0]= (1/A[0,0]) *(b[0]-(A[0,1]*x[1]+A[0,2]*x[2]))
#     x[1]= (1/A[1,1]) *(b[1]-(A[1,0]*x[0]+A[1,2]*x[2]))
#     x[2]= (1/A[2,2]) *(b[2]-(A[2,0]*x[0]+A[2,1]*x[1]))


# print(x)
# print(A@x)

#Conjugate Gradient Method

# A=np.array([[4.,-1,1],[-1,4,-2],[1,-2,4]])
# b=np.array([12.,-1,5])
# x_0=np.zeros(3)
# #일단 3,1,1이 답임

# #First Iteration
# r_0=b- A@x_0    #Residual
# s_0= r_0.copy() #탐색방향
# a_0= s_0@r_0/(s_0@A@r_0)         #Scailing Factor

# #Update x 
# x_1= x_0+ a_0*s_0 
# print(x_1)

# #Second Iteration
# r_1=b- A@x_1    #새로운 Residual             
# b_0= -r_1@A@s_0/(s_0@A@s_0) #탐색방향을 찾는 계수2
# s_1= r_1+ b_0*s_0 #새로운 탐색방향 벡터
# a_1= s_1@r_1/(s_1@A@r_1)
# x_2= x_1+ a_1*s_1
# print(x_2)

# #Second Iteration
# r_2=b- A@x_2    #새로운 Residual             
# b_1= -r_2@A@s_1/(s_1@A@s_1) #탐색방향을 찾는 계수2
# s_2= r_2+ b_1*s_1 #새로운 탐색방향 벡터
# a_2= s_2@r_2/(s_2@A@r_2)
# x_3= x_2+ a_2*s_2
# print(x_3)

#위에 발산한 예시를 Conjugate Gradient Method로 풀기
A=np.array([[3.,-3,3],[-3,5,1],[3,1,5]])
b=np.array([9.,-7,12])
x_0=np.zeros(3)


#First Iteration
r_0=b- A@x_0    #Residual
s_0= r_0.copy() #탐색방향
a_0= s_0@r_0/(s_0@A@r_0)         #Scailing Factor

#Update x 
x_1= x_0+ a_0*s_0 
print(x_1)

#Second Iteration
r_1=b- A@x_1    #새로운 Residual             
b_0= -r_1@A@s_0/(s_0@A@s_0) #탐색방향을 찾는 계수2
s_1= r_1+ b_0*s_0 #새로운 탐색방향 벡터
a_1= s_1@r_1/(s_1@A@r_1)
x_2= x_1+ a_1*s_1
print(x_2)

#Third Iteration
r_2=b- A@x_2    #새로운 Residual             
b_1= -r_2@A@s_1/(s_1@A@s_1) #탐색방향을 찾는 계수2
s_2= r_2+ b_1*s_1 #새로운 탐색방향 벡터
a_2= s_2@r_2/(s_2@A@r_2)
x_3= x_2+ a_2*s_2
print(x_3)
print(A@x_3)

# def Av(v):
#     return A@v 

# x0=np.zeros(3)
# print(conjGrad(Av,x0,b))










