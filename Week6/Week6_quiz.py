import numpy as np

#Problem1 
# f(x)= x^4- 4x+1, f'(x)=4x^3 -4 
#1-1
x0=2 
x_true = 1 
def gradf(x):
    gradf= 4*x**3 -4 
    return gradf
r=gradf(x_true)-gradf(x0)

#1-2
#f(x)= (x0+alpha*4)^4 -4(x0+alpha*r) 
#f'(x)= 4*r*(x0+alpha*4)^3 -4r=0
#(x0+alpha*r)=1 
alpha=(1-x0)/r 
print(alpha) #0.03571428571428571
x1=x0+alpha*r
print(x1) #1
#1-3
print(gradf(x1)) #값은 0 최소점임. 2차함수 f(x)가 f'(x)=0인 곳은 극소점이기 떄문


#Problem2 
# #기본 설정
A=np.array([[3,2],[2,6]])
b=np.array([2,8])
n=len(b)

x=np.zeros((n,n+1))
x[:,0]= np.array([1,2])
r=np.zeros((n,n))
s=np.zeros((n,n))
d=np.zeros(n) #beta임
a=np.zeros(n) #alpha임

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

print(r) #r0, r1값 [-5,6] , [-0.99270073, 0.82725061]
print(s) #s0 s1 값 [-5 6], [-1.12956944, 0.66300815]
print(a[0]) #alpba 0 값 0.14841849148418493
print(d[0]) # beta 0 값 0.02737374275548931
print(x) #x0,x1,x2 값 [1,2] [0.25790754, 1.10948905] ,[-0.28571429, 1.42857143]
print(A@x[:,2])

#Problem 3
def ConjGrad(A,x,btol=1e-9):
    n= len(b)
    r= b-A@x
    s=r.copy()
    for i in range(n):
        u=A@s 
        alpha= np.dot(s,r)/np.dot(s,u)
        x= x+ alpha *s 
        r= b- a@x 
        if(np.sqrt(np.dot(r,r))<tol):
            break  
        else: 
            beta= -np.dot(r,u)/np.dot(s,u)
            s= r+ beta*s   
    return x
    
    
    
    
