import numpy as np
from scipy.linalg import *
from ch2 import *

#LU 분해
#응용문제
#물리 응용문제 몇가지
#숄레스키 분해 

#일단 이건 잘못된거 같으니 무시하고 아래 문제만 보기
# amat= np.array([[3,-1,4],[-2,0,5],[7,2,-2]])
# a= amat.copy()

# #피벗 아래 1열 원소를 없애기
# lam1=a[1,0]/a[0,0]
# a[1,:]= a[1,:] - lam1*a[0,:]

# lam2=a[2,0]/a[0,0]
# a[2,:]= a[2,:] - lam2*a[0,:]

# # lam3=a[2,1]/a[1,1]
# # a[2,:]= a[2,:] - lam3*a[1,:]

# row2=a[1,:].copy()
# row3=a[2,:].copy()
# a[1,:]= row3 
# a[2,:]= row2

# print(a)
# U=a.copy()
# L=np.zeros([3,3])

# L= L +np.diag([1,1,1])
# L[1,0]=lam1 
# L[2,0]=lam2
# L[2,1]=0


# print(U)
# print(L)
# print(amat)
# print(L@U)

# #일단 내 코드는 잘못됬는데 가우스 소거>U행렬에 lambda 넣기, 전진대입을 함

# b=np.array([6,3,7])
# n= len(b)
# y=np.zeros(next(n))

# y[0]= np.zeros(n)
# y[0]= b[0] 

# #전진 대입법
# # for k in range(1,n):
# #     y[k] =b[k]- np.dot(L[k,0:k],b[0:k])
    
# # for k in range(n-1,-1,-1): 
# #   y[k]=(y[k]- np.dot(U[k,k+1:n],y[k+1:n]))/U[k,k]


#LU분해법으로 Ax=b LUx=b로 하여 풀기

#기본 설정
amat=np.array([[1,4,1],[1,6,-1],[2,-1,2]])
a=amat.copy()
b=np.array([7,13,5])
n=len(b)
# print(a)

#가우스 소거법
lam1=a[1,0]/a[0,0]
a[1,:]= a[1,:]- lam1*a[0,:]
lam2=a[2,0]/a[0,0]
a[2,:]=a[2,:]-lam2*a[0,:]
lam3=a[2,1]/a[1,1]
a[2,:]=a[2,:]-lam3*a[1,:]

#L과 U값 정하기
#아직 L을 구하는 방법이 잘 이해 안되니 찾아볼것
U=a.copy()

L=np.zeros([3,3])
L= L +np.diag([1,1,1])
L[1,0]=lam1 
L[2,0]=lam2
L[2,1]=lam3

##LU=A인가 검증
# print(amat)
# print(L@U)
# print(L)
# print(U)
y=np.zeros([n,1])

#전진 대입법으로 y 구하기 LUx=b Ly=b
for k in range(0,n):
    y[k]= (b[k]-np.dot(L[k,:],y))/L[k,k]
    
    
x=np.zeros([n,1])  
#후진 대입법으로 x 구하기 Ux=y 구하기
for k in range(n-1,-1,-1):
    x[k] = (y[k]-np.dot(U[k,:],x))/ U[k,k]

#검증
print(np.dot(np.linalg.inv(amat),b))
print(x)
print(amat@x)
print(b)

#도르레 문제
m1=20 
m2=40
m3=10
F1=10
F2=10

A= np.array([[m1,0,0,-3],[0,m2,0,-2],[0,0,m3,1],[-3,2,1,0]])
b=np.array([0,F1,F2,0])
print(np.dot(np.linalg.inv(A),b))