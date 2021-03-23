import numpy as np
import scipy as sp
from scipy.linalg import lu_factor, lu_solve
from ch2 import *

# A= np.array([[3,-3,3],[-3,5,1],[3,1,5]])
# b= np.array([9,-7,12])

# print(np.linalg.solve(A,b))

# ch2 모듈로 푸는 것에 오류가 생기는듯 ->input이 정수여서 문제
# input이 정수면 output이 정수로 반올림 되서 나오는 오류였음
# LU= LUdecomp(A)
# x=LUsolve(LU,b) 
# print(x) 
# print(A@x)

# #scipy 모듈로 풀기
# lu, piv= lu_factor(A) 
# x=lu_solve((lu,piv),b)
# print(x)
# print(A@x)


# #scipy Module을 이용한 풀이
# A=np.array([[4,8,10,],[8,13,16],[20,16,-91]])
# b=np.array([24,18,-119])

# lu, piv= lu_factor(A) 
# x=lu_solve((lu,piv),b)
# print(x)
# print(A@x)

# #sparse matrix: 음 수업에서 문제가 많았었는디. 복습해야하나
# #A
# n=10
# c=4*np.ones(n)
# e=2*np.ones(n-1)
# d=np.ones(n-1)
# # print(np.diag(d))
# # print(np.diag(e,k=1))
# # print(np.diag(c,k=-1))
# C=np.diag(c)
# E=np.diag(e,k=1)
# D=np.diag(d,k=-1) 
# A= C+D+E 
# print(A)
 
# x=np.zeros(n)
# y=np.zeros(n)
# dp =np.zeros(n)
# cp= np.zeros(n-1)
# dp= d.copy()
    
# for k in range(1,n):
#         lam=  c[k-1]/d[k-1]
#         dp[k] =d[k] -lam*e[k-1]
#         cp[k-1] = lam

# #전진 대입법        
# y[0]= b[0]    
# for k in range(1,n):
#     y[k]= b[k]- cp[k-1]*y[k-1]

# #후진 대입법
# x[n-1]=y[n-1]/dp[n-1]
# for k in range(n-2,-1,-1): 
#     x[k] =( y-[k] - e[k]*x[k+1])/dp[k]
    
#문제 3

A=np.array([[2,1,0,0,0]
            ,[1,2,1,0,0]
            ,[0,1,2,1,0]
             ,[0,0,1,2,1]
             ,[0,0,0,1,2]]) 
Aori=A.copy()
b= np.array([1,1,1,1,1])
n=len(b)
#solve using the tridiagonal matrix solver
#Find U,L,x 
#IN A@x=b 
#doolittle 도 가능 

L= np.eye(n)
#Gauss Elimination
for k in range (0,n-1):
    for j in range(k+1,n):
        lam = A[j,k]/A[k,k] 
        A[j,:]= A[j,:] - lam * A[k,:]
        L[j,k] =lam 

U=A   

print(U)
print(L)
print(L@U)
print(np.linalg.solve(Aori,b))
print(np.linalg.solve(L@U,b))
#L@U값이 A가 아니더라도 해는 같네?
#
#A=np.array([[2,-2,0,0,0]
#             ,[-2,5,-6,0,0]
#             ,[0,6,16,12,0]
#              ,[0,0,12,39,-6] 
#              ,[0,0,0,-6,14]])







