import numpy as np
# #Problem1 Ax=b 문제를 Gaussian Ellimination 과 Back subsitution로 풀기
# #Augmented Matrix 만들기
# A= np.array([[1,2,4],[3,8,14],[2,6,13]])
# b= np.array([3,13,4])
# Aaug=np.column_stack([A,b]) 
# Aori=A.copy() #원랫값 저장
# bori=b.copy()
# n=np.size(b)

# #Gaussian Elimination 1)pivot 정하기, 2)pivot 아래 열 원소 0으로 만들기
# lam1=Aaug[1,0]/Aaug[0,0]
# Aaug[1,:]=Aaug[1,:]- lam1*Aaug[0,:]
# lam2=Aaug[2,0]/Aaug[0,0]
# Aaug[2,:]=Aaug[2,:]- lam2*Aaug[0,:]
# lam3=Aaug[2,1]/Aaug[1,1]
# Aaug[2,:]=Aaug[2,:]- lam3*Aaug[1,:]
# #A랑 b 다시 부여하기(Back subsitution 계산을 위해)
# A=Aaug[:,0:3]
# b=Aaug[:,3]
# # #Back subsitution 계산하기
# x=np.zeros(n)
# x[2]=(b[2] -np.dot(A[2,:],x))/A[2,2] 
# x[1]=(b[1] -np.dot(A[1,:],x))/A[1,1]
# x[0]=(b[0] -np.dot(A[0,:],x))/A[0,0] 
# #x=3,4,-2

# #A랑 b 다시 부여하기
# A= Aori
# b= bori
# #검산 x=3,4,-2

# print(np.linalg.solve(A,b))
# print(x)
# print(A@x)

# #Problem2  문제를 풀기전 방정식을 재정렬하고 가우스 소거법 사용하기
# #Aaug 행렬을 재정렬 하였음
# Aaug=np.array([[1,2,0,-2,0,-4],[0,1,-1,1,-1,-1],[0,1,0,2,-1,1],[0,0,2,1,2,1],[0,0,0,-1,1,-2]])
# Aori=Aaug[:,0:5].copy() #원랫값 저장
# bori=Aaug[:,5].copy()
# n=np.size(bori)
# #Gauss Elimination으로 풀기
# #[0,0] pivot 열 아래 원소들 없으므로 생략
# #[1,1] pivot 열 아래 원소는 [2,1] 하나 
# lam1= Aaug[2,1]/Aaug[1,1]
# Aaug[2,:]= Aaug[2,:]- lam1*Aaug[1,:]
# #[2,2] pivot 열 아래 원소는 [3,2] 하나 
# lam2= Aaug[3,2]/Aaug[2,2]
# Aaug[3,:]= Aaug[3,:]- lam2*Aaug[2,:]
# #[3,3] pivot 열 아래 원소는 [4,3] 하나 
# lam3= Aaug[4,3]/Aaug[3,3]
# Aaug[4,:]= Aaug[4,:]- lam3*Aaug[3,:]
# #A랑 b 다시 부여하기(Back subsitution 계산을 위해)
# A=Aaug[:,0:5]
# b=Aaug[:,5]

# # #Back subsitution 계산하기
# x=np.zeros(n)
# x[4]=(b[4] -np.dot(A[4,:],x))/A[4,4] 
# x[3]=(b[3] -np.dot(A[3,:],x))/A[3,3] 
# x[2]=(b[2] -np.dot(A[2,:],x))/A[2,2] 
# x[1]=(b[1] -np.dot(A[1,:],x))/A[1,1]
# x[0]=(b[0] -np.dot(A[0,:],x))/A[0,0] 
# #x=[2,-2,1,1,-1]

# # #A랑 b 다시 부여하기
# A= Aori
# b= bori

# #검산 x=[2,-2,1,1,-1]
# print(x)
# print(np.linalg.solve(A,b))
# print(A@x)
# print(b)

# #Problem3 하삼각행렬을 만들고 푸는 Gauss Elimination 코드 짜보기
# #기본설정
# Aaug=np.random.rand(3,4) #랜덤 3*4행렬 
# Aori=Aaug[:,0:3].copy() #원랫값 저장
# bori=Aaug[:,3].copy()
# n=np.size(bori)
# #Gauss Elimination 
# for k in range (n-1,0,-1): 
#     for j in range(k-1,-1,-1):
#             lam = Aaug[j,k]/Aaug[k,k]
#             Aaug[j,:]= Aaug[j,:] - lam *Aaug[k,:] #j+1행에 pivot 행*lambda 빼기.
            
# #A랑 b 부여하기(Back subsitution 계산을 위해)          
# A=Aaug[:,0:3]
# b=Aaug[:,3]
# #Foward substitution으로 해 구하기
# x=np.zeros(n)

# for k in range(0,n):
#         x[k]=(b[k] -np.dot(A[k,:],x))/A[k,k] 

# # 다시 A 값과 b값 부여하기
# A=Aori
# b=bori
# #검산하기 A@x-b=0
# print(Aaug)
# print(A@x-b)

#Proble4 LU분해를 통해 문제 풀기
#기본설정
Aaug=np.random.rand(3,4) #랜덤 3*4행렬 
Aori=Aaug[:,0:3].copy() #원랫값 저장
bori=Aaug[:,3].copy()
A=Aaug[:,0:3]
b=Aaug[:,3]
n=np.size(bori)
L=np.eye(n)
print(L)
#U는 Gauss elimination된 A 행렬이고, L은 단위 행렬에 가우스 연산 과정내에서 lambda값을 더하여 구할수 있다
for k in range (0,n-1): 
    for j in range(k+1,n):
            lam = A[j,k]/A[k,k]
            A[j,:]= A[j,:] - lam *A[k,:] #j+1행에 pivot 행*lambda 빼기.
            L[j,k]=lam     
#U에 연산된 값 저장하고 A는 원랫값 다시 부여하기
U=A
A=Aori            
# Ax=b, LUx=b, Ux=y, Ly=b로 1)Ly=b서 y를 2) Ux=y서 x를 구한다
x=np.zeros([n,1])
y=np.zeros([n,1])
#Ly=b 구하기 
for k in range(0,n):
        y[k]=(b[k] -np.dot(L[k,:],y))/L[k,k] 
#Uy=y 구하기 
for k in range(n-1,-1,-1):
        x[k]=(y[k] -np.dot(U[k,:],x))/U[k,k] 
#구한 x값 검산
b=bori        
print(x)
print(A@x)
print(b)

#Problem5 여러 물체가 줄로 연결된 경사면과 도르레
#기본설정
m=[10,4,5,6]
mu=[0.25,0.3,0.2]
g=10
theta= 40*np.pi/180
sin=np.sin(theta)
cos=np.cos(theta)

# x=[T1,T2,T3,a]로 본다 x[T1,T2,T3,a]=[34.68,47.01,66.3,1.045]
A=np.array([[1/m[0],0,0,1],[-1/m[1],1/m[1],0,1],[0,-1/m[2],1/m[2],1],[0,0,-1/m[3],1]])
b= g* np.array([sin-mu[0]*cos,sin-mu[1]*cos,sin-mu[2]*cos,-1])
x=np.linalg.solve(A,b)
print(x)

