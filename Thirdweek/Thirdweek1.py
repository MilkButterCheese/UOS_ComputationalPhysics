#  이번주 과제 있음 
#  화요일 과제 ->월요일 제출 목요일 퀴즈를 하되 수업 길이를 줄이기

#학습 내용

# 1. 복습
# 2. 가우스 소거법 -> LU 분해법
# 3. 응용문제
# 4. 숄레스키 

# 1.연립방정식의 해 
# 예) A=[[2,3],[1,1]] b=[1,1] 
# det(A) !=0이면 해가 존재 
# 불량조건: det(A)det(A^(-1))를 computing 시켰을떄 ~0인경우 

#Problem 1.
# A=[[6,-4,1],[-4,6,-4],[1,-4,6]] 
# B=[[-14,22],[36,-18],[6,7]] 
import numpy as np

A=np.array([[6,-4,1],[-4,6,-4],[1,-4,6]]) 
B=np.array([[-14,22],[36,-18],[6,7]]) 
x= np.zeros([3,2])

Ainv=np.linalg.inv(A)

x[:,0]=np.dot(Ainv,B[:,0])
x[:,1]=np.dot(Ainv,B[:,1])

# a=1 b=2일때 서로의 값을 바꾸려면?
#temp =a
# a=b 
# b=temp 혹은
# a,b = b,a


#Problem3 b벡터 대신 B가 올때 B에 컬럼에 각각 대응하는 해 구하는 함수 만들기

A_shape=A.shape
n=A_shape[0]
B_shape=B.shape
m=B_shape[1]

# print(A)
# print(B)
# print(m)
# print(n)
# hstack이란 명령어가 열을 쌓는건데 알아보기

# for i in range(0,m):
#     for k in range (0,n-1):
#         for j in range(k+1,n):
#                if A[j,k] != 0:
#                         print("we are loop in",j,k)
#                         lamb = A[j,k]/A[k,k]
#                         A[j,:]= A[j,:] - lamb *A[k,:] #j+1행에 pivot 행*lambda 빼기.
#                         B[j,i]= B[j,i]-lamb *B[k,i]
                        
# #back substitution으로 해 구하기
# print(A)
# print(B)
# x= np.zeros((n,m))
# print(x)
    
# for i in range(0,m):
#     for k in range(n-1,-1,-1):
#             x[k,i]=(B[k,i] -np.dot(A[k,:],x[:,i]))/A[k,k] 
                    

# print(x)
# print(B)
# print(np.dot(A,x))


#LU 분해법

#A*A= 요소별 곱하기
#A@A=np.dot(A,A): 행렬곱

#LU 분해의 다양한 정의와 제한조건
#Doolittle's decomposition L_ii=1 
#Crout's Decomposition U_ii=1 
#Choleski's Decomposition L=U.transpose() >Hermitian이나 대칭 행렬들에 씀

#A = LU 
#A@x=b   
#L@U@X= b , U@x= y 라 정의
#L@y=b에서 y값을 구하고 U@x=y 를 통해 x값을 구함

#[L/U]=[[U11,U12,U13],[L21,U22,U23],[L31,L32,L33]]
#L=[[L11,0,0],[L21,L22,0],[L31,L32,L33]]
#L@x=[[L11x1],[L21x1+L22x2],[L31x1+L32x2+L33x3]][[c1],[c2],[c3]]
#x1=c1/L11, x2=(c3-L31x1-L32x2)/L22  
#x_n=(cn-Lnjxj)/Lnn

LU=A.copy()
LU[1,0] =A[1,0]/A[0,0]
LU[2,0] =A[2,1]/A[1,1]
LU[2,1]= A[2,1]/A[1,1]
print(LU)

