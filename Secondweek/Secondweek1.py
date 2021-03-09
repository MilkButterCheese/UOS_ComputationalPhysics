import numpy as np
# A= np.random.rand(3,4) 
# #Augmented A렬  

# a= A[0:3,0:3]
# print(a)
# b= A[:,3]
# print(b)

# #행렬의 행 크기 알기 
# print(A.shape) 
# #행렬의 
# print(len(a))


# a1=b1으로 둘경우 a1에 append등의 변수등을 쓰면
# A또한 변한다. 변경 이후까지 같아지기 않지 원하면 copy를 쓴다
# aa= a.copy()

# A= np.random.rand(3,4)
# a= A[0:3,0:3]
# aa= a.copy()
# #a=np.array([[1,1,1],[2,1,2],[3,1,4]])
                  
# b=A[:,3]
# bb=b.copy()
# n= len(a)
# xx=np.zeros(len(b))
# #가우스 소거법 알고리즘
# for k in range(0,n-1):   #pivot rows k= 0,1,...
#     for i in range(k+1,n):  #range i=1
#         if a[i,k] !=0:
#                print('We are in loop',i,k)
#                lam = a[i,k]/a[k,k]  #multiplier
#                #a[i,k]= 0 #소거 #a[i,k+1:n]까지 
#                a[i,k:n] = a[i,k:n]- lam*a[k,k:n]
#                b[i]=b[i]-lam*b[k]
                
# #Back substitution 
# for k in range(n-1,-1,-1): #from end to beginning
#     x[k]=(b[k] -np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]


# print(aa)    
# print(a)
# print(bb)
# print(b)

            
            
            
            
# import time 
# time_start=time.time()
# A=np.zeros((4000),(4000))

# for i in range(4000):
#     for j in range(4000):
#         A[i,j]= A[i,j] +1

# time_finish= time.time()
# print('totoal elapsed time',time_finish-time_start)
# #python은 유난히 for문에 시간이 오래걸림      
                

#연습문제 1. 결과가 아랫삼각행렬꼴로 나오는 가우스 소거법 알고리즘 짜기
                
A= np.random.rand(3,4)
a= A[0:3,0:3]
aa= a.copy()
#a=np.array([[1,1,1],[2,1,2],[3,1,4]])
                  
b=A[:,3]
bb=b.copy()
n= len(a)
xx=np.zeros(len(b))

#가우스 소거법 알고리즘
for k in range(n-1,0,-1):   #pivot rows k= n-1,n-2,..0(미포함)
    for i in range(k-1,-1,-1):  #range i=1
        if a[i,k] !=0:
               print('We are in loop',i,k)
               lam = a[i,k]/a[k,k]  #multiplier
               #a[i,k]= 0 #소거 #a[i,k+1:n]까지 
               a[i,k:n] = a[i,k:n]- lam*a[k,k:n]
               b[i]=b[i]-lam*b[k]

print(a)
#Back substitution 
#   x[k]=(b[k] -np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]

#연습문제 2 
bmat=np.array([[1,2,],[2,3],[4,5]])
print(bmat)

# #가우스 소거법 알고리즘 함수
def gauss(a,b):
    for k in range(0,n-1):   #pivot rows k= 0,1,...
        for i in range(k+1,n):  #range i=1
            if a[i,k] !=0:
                print('We are in loop',i,k)
                lam = a[i,k]/a[k,k]  #multiplier
                #a[i,k]= 0 #소거 #a[i,k+1:n]까지 
                a[i,k:n] = a[i,k:n]- lam*a[k,k:n]
                b[i]=b[i]-lam*b[k]
                #Back substitution 
                for k in range(n-1,-1,-1): #from end to beginning
                    x[k]=(b[k] -np.dot(a[k,k+1:n],x[k+1:n]))/ a[k,k]
    return x 



                
                
                
                
                
                
                
                
 