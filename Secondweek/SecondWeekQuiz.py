import numpy as np

#problem1
a= np.zeros((1000,1000))
b=np.array([[2,3,0,0,0],[1,2,3,0,0],[0,1,2,3,0],[0,0,1,2,3]])
a[:4,:5]=b
c=np.array([[1,2,3,0],[0,1,2,3],[0,0,1,2]])
a[997:1000,996:1000]=c
#print(a)
print(a[:4,:5])
print(a[997:1000,996:1000])

#problem2
a=np.array([[1,2],[1,-3]])
b=np.array([10,5])
ainv=np.linalg.inv(a)
x=np.dot(ainv,b)
print(x)
print(np.dot(a,x)-b)

#problem 3
a=np.array([[-1,-2,-1,0,0],[-2,1,3,0,0],[2,0,0,-1,-2],[0,2,0,-2,1],[0,0,2,-1,3]])
b=np.array([-5,-7,4,2,0])
ainv=np.linalg.inv(a)
x=np.dot(ainv,b) # 순서대로 s,p,d,f,g의 값
print(x)
print(np.dot(a,x)-b)

#problem4
theta=np.pi/180*20
a=np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
print(a)
x=np.array([1,0])
y=np.dot(a,x)
print(y)

#problem5 
#a벡터를 행으로 쌓은 행렬과 v벡터를 열로 쌓은 벡터가 행렬곱하여 identity 행렬이므로 v는 a의 역행렬
a=np.array([[2.46,0,0],[-1.23,2.14,0],[0,0,10]])
ainv=np.linalg.inv(a)
v1=ainv[:,0]
v2=ainv[:,1]
v3=ainv[:,2]
# print(a)
# print(np.dot(a,v1))
# print(np.dot(a,v2))
# print(np.dot(a,v3))
print(v1)
print(v2)
print(v3)


