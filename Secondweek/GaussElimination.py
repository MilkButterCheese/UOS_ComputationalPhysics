#Gauss Elimination의 계산 아이디어
#1. 연립방정식의 해는 (1)행의 위치를 서로 바꾸거나 (2) 행에 스칼라배를 하거나 (3)어떤 행에 다른행에 스칼라배 한것 만큼 빼더라도 그 해집합은 바뀌지 않는다.
#2. 주대각선 성분들은 Pivot이라 불린다. (1,1) Pivot부터 시작하여 Pivot이 속한 열 아래 원소들을 0으로 만든다. 
#3. 그러면 대각성분을 경계로 아랫삼각형이 모두 0인 꼴의 행렬이 만들어진다. 이를 행사다리꼴(Row Echelon Form)이라 부른다.
#4. 해를 구하기 위하여 행에서 가장 먼저 0이 아닌 원소가 나오고 그 다음 원소들이 다 0이 아닌꼴로 바꾸었을때 이를 기약 행 사다리꼴(reduced row echelon form)이라 부른다.

#Gauss Elimination의 계산 알고리즘
#1.(1,1)을 pivot으로 삼는다. a[j,1]-lambda*a[1,1]=0, lambda=a[j,1]/a[1,1]로 정의하자.
#2.a[j,k]= a[j,k]- lambda*a[1,k]를 해주자.(j행에 1번째 행에 lambda배 한 것을 뺴주는 것) k는 1부터 n까지 
#3.(2,2)을 pivot으로 삼는다 a[j,2]-lambda*a[2,2]0. lambda=a[j,2]/a[2,2]
#4. a[j,k]= a[j,k] -lambda*a[2,k]를 해주자.(j헹에 2번째 헹에 lambda배를 해주는 것을 빼는것) k는 2부터 n까지
#5. 위와 같은 계산을 계속 반복한다. pivot이 (n-1,n-1)으로 삼아 계산할 때 까지 



#기본설정
import numpy as np

a_aug=np.random.rand(3,4) #3*4행렬 
a= a_aug[0:3,0:3]
b= a_aug[:,3]
a_shape=a_aug.shape
n=a.shape[0]
bmat=np.random.rand(3,3) #3*3행렬 

#test module
# print(a_aug)
# print(a)
# print(b)
# print(a_shape)
# print(n)

#Problem1 Gauss elimination 알고리즘 짜기

# print(a)

# for k in range (0,n-1):
#     for j in range(k+1,n):
#         if a[j,k] != 0:
#             print("we are loop in",j,k)
#             lamb = a[j,k]/a[k,k]
#             a[j,:]= a[j,:] - lamb *a[k,:] #j+1행에 pivot 행*lambda 빼기.
#             b[j]= b[j]-lamb *b[k]
            
# print(a)
# print(b)

# #back substitution으로 해 구하기
# x=np.zeros(n)

# for k in range(n-1,-1,-1):
#         x[k]=(b[k] -np.dot(a[k,:],x))/a[k,k] 
    
# print(x)
# print(np.dot(a,x)-b)
    
#Problem2 Gauss Elimination 아랫삼각행렬꼴로 만들기

# print(a)

# for k in range (n-1,-1,-1):
#     for j in range(k-1,-1,-1):
#         if a[j,k] != 0:
#             print("we are loop in",j,k)
#             lamb = a[j,k]/a[k,k]
#             a[j,:]= a[j,:] - lamb *a[k,:] #j+1행에 pivot 행*lambda 빼기.
#             b[j]= b[j]-lamb *b[k]
            
# print(a)
# print(b)

# #back substitution으로 해 구하기
# x=np.zeros(n)

# for k in range(0,n):
#         x[k]=(b[k] -np.dot(a[k,:],x))/a[k,k] 
    
# print(x)
# print(np.dot(a,x)-b)

#Problem3 b벡터 대신 bmat가 올때 bmat에 컬럼에 각각 대응하는 해 구하는 함수 만들기

print(a)

for i in range(0,3):
    for k in range (0,n-1):
        for j in range(k+1,n):
               if a[j,k] != 0:
                        print("we are loop in",j,k)
                        lamb = a[j,k]/a[k,k]
                        a[j,:]= a[j,:] - lamb *a[k,:] #j+1행에 pivot 행*lambda 빼기.
                        bmat[j,i]= bmat[j,i]-lamb *bmat[k,i]
                        
#back substitution으로 해 구하기
    print(a)
    print(bmat)
    x=np.zeros((n,n))
    
for i in range(0,3):
    for k in range(n-1,-1,-1):
            x[k,i]=(bmat[k,i] -np.dot(a[k,:],x[:,i]))/a[k,k] 
                    
print(x)
print(np.dot(a,x)-bmat)