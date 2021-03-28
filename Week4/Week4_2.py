import numpy as np

#QUiz
# #Problem 1
# # def backdsub(A,b):
# #     n= len(b) 
# #     for k in range(n-1,-1,-1):
# #         b[k] = (b[k] - np.dot(A[k,:],b[k+1:n]))/A[k,k]
# #         return b
    
# #problem2
# #2-1
# X=np.zeros(6)
# X[0]= 1
# X[1]= 1
# X[2]= X[0]+X[1]
# X[3]= X[2]+X[1]
# X[4]= X[3]+X[2]
# X[5]= X[4]+X[3]

# #2-2
# #[x_1,...x_10] 까지의 파보나치 수열
# x=np.zeros(10)
# x[0]= 1
# x[1]= 1
# for k in range(2,10):
#     x[k] = x[k-1] +x[k-2]
    
# print(x)
# # b= [x_2,...,x_11] 의 파보나치 수열
# A=np.zeros(10)
# a= np.ones(10)
# A_1= np.diag(a)
# b=np.ones(9)
# A_2= np.diag(b, k=-1)
# A=A_1+A_2 
# b= A@x
# #problem2-3
# n=len(b)
# x=np.zeros(n)
# for k in range(0,10):
#     x[k]= (b[k] - np.dot(A[k,:],x))/A[k,k]
    
# print(x)


# #Problem3
# A= np.array([[0.95,0.05],[0.02,0.98]])
# x=np.array([30,24])

# #problem3-2
# lam=A[1,0]/A[0,0]
# A[1,:]=A[1,:] - lam*A[0,:]
# L=np.eye(2)
# L[1,0]=lam
# U=A

# #Problem 3-3
# #Ax(N-1)=x(N) 이기 때문에 x(N-1)= inv(A)*X(N)
# #inv(A) = inv(LU)= inv(U) * inv(L)  
# # L^(-1)@x_N_1=y U^(-1)@y=x
# invU=np.linalg.inv(U)
# invL=np.linalg.inv(L)
# x_2020= np.zeros(2)
# y=np.zeros(2)

# #U^(-1)@y=x 풀기 
# # y[1]=(x[1]-np.dot(invU,y)) / invU[1,1]
# # y[0]=(x[0]-np.dot(invU,y)) / invU[0,0]

# #시간이 부족해 invA로 풀었습니다
# invA=np.linalg.inv(A) 
# x_2018 =np.zeros(2)
# x_2018= invA@invA@invA@x   
# print(x_2018)

#Lecture 
#대칭 행렬, 5중 대각계수 행렬, 스케일된 피벗
A=np.array([[2,-2,0,0,0],[-2,5,-6,0,0],[0,-6,16,12,0],[0,0,12,39,-6],[0,0,0,-6,14]])
b=np.array([1,0,0,0,0])
print(np.linalg.solve(A,b))

# 대칭행렬 A= LDL^t 로 분해가능 
# ch2.py 에서 LUdecomp3 LUdecomp5 사용가능

#Scaled Pivot
#예시 1
#A=L@U=L@D@LT
A=np.array([[3,-3,3],[-3,5,1],[3,1,10]])

#gauss elimination
lam1=A[1,0]/A[0,0]
A[1,:]=A[1,:]-lam1*A[0,:]
lam2=A[2,0]/A[0,0]
A[2,:]=A[2,:]-lam2*A[0,:]
lam3=A[2,1]/A[1,1]
A[2,:]=A[2,:]-lam3*A[1,:]

L=np.eye(3)
L[1,0]= lam1 
L[2,0]= lam2 
L[2,1]= lam3 
U= A


print(L@A)
















