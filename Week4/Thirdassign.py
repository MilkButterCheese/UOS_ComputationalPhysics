import numpy as np
from ch2 import *
import matplotlib.pyplot as plt
import time
start= time.time()

#Problem 1 LU 분해로 역행렬 구하기
A=np.array([[6,2,0,0,0],[-1,7,2,0,0],[0,-2,8,2,0],[0,0,3,7,-2],[0,0,0,3,5]],dtype='float32')
B=np.eye(5)
x=np.zeros((5,5))
y=np.zeros((5,5))
n=(np.shape(B))[0]
Aori=A.copy()
#Gauss Elimination Ax[il=b[i], A=LU 
#U = Gauss elmimation후 L L=eye[5] +lam 값
L=np.eye(5)
for k in range (0,n-1):
    for j in range(k+1,n):
            lam= A[j,k]/A[k,k]
            A[j,:]= A[j,:] -lam* A[k,:]
            L[j,k]= L[j,k]+ lam
U=A
#LU가 모두 구해짐
#LUx[i]=B[i] Ux[:,i]=y[:,i]로 두고 Ly[:,i]=B[:,i]로 y[:,i] 구하고 x[:,i] 구하기
#Ly[i]=B[i] 는 전진대입법을 사용한다
for j in range (0,n):
    for i in range(0,n):
        y[i,j]= (B[i,j]-np.dot(L[i,:],y[:,j]))/L[i,i]
#y값을 찾았으므로 x값을 찾는다. 
#Lx[:,i]=y[:,i]는 후진대입법으로 찾는다.
for j in range (0,n):
    for i in range(n-1,-1,-1):
        x[i,j]= (y[i,j]-np.dot(U[i,:],x[:,j]))/U[i,i]
#오차 확인
# print(L@U@x-B)
print(np.linalg.inv(Aori))
print(x)
#해당 문제의 x값은 A의 역행렬 값과 같음 Gauss Jordan method로 보임

# Problem 2 
# LUdecompose3 풀이법
n=12
A= 4*np.eye(n,k=0)  -1*np.eye(n,k=-1) -1*np.eye(n,k=+1)
b= 5*np.ones(n)
b[0]=b[0]+4

c= -1*np.ones(n-1)
d=  4*np.ones(n)
e= -1*np.ones(n-1)

c, d, e =LUdecomp3(c,d,e)
x = LUsolve3(c,d,e,b)
print("걸린 시간은 ",time.time()-start)
# n=8일때 decomp3 풀이시간: 0.0002181529998779297, 0.00019431114196777344, 0.00031375885009765625
# n=10일때 decomp3 풀이시간: 0.00030112266540527344, 0.00023102760314941406, 0.000225067138671875
# n=12일때 decomp3 풀이시간: 0.0002257823944091797 , 0.00022149085998535156,  0.0002505779266357422 

n=10
A= 4*np.eye(n,k=0)  -1*np.eye(n,k=-1) -1*np.eye(n,k=+1)
b= 5*np.ones(n)
b[0]=b[0]+4
# Aori=A.copy()
A= LUdecomp(A)
x = LUsolve(A,b)

# print(Aori@x)

print("걸린 시간은 ",time.time()-start)
# n=8일때 decomp 풀이시간: 0.0004558563232421875, 0.027350902557373047, 0.0004725456237792969
# n=10일때 decomp 풀이시간: 0.0005800724029541016,  0.006646633148193359, 0.01594996452331543 
# n=12일때 decomp 풀이시간: 0.0005037784576416016,  0.0006608963012695312, 0.006196737289428711 


#Problem3 
A= np.array([[2,-1,0,0,0],[-1,4,-1,0,0],[0,-1,4,-1,-2],[0,0,-1,2,-1],[0,0,-2,1,3]])
k=2.5
b=np.zeros((5,5))
for j in range(0,5):
    b[:,j]= j* np.ones(5)/k

print(b)

x= np.linalg.solve(A,b)
print(x)
w=[0,1,2,3,4]
plt.plot(w,x)
plt.show()

