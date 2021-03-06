#함수 만들기
def func(x,y):
    return x+y
print(func(2,3))

#lambda 선언문:
a = lambda x, y : x +y
print(a(2,3))

#numpy와 matplotlib import 모듈 불러오기 
import numpy as np
import matplotlib.pyplot as plt
import scipy
from numpy import sin, cos, exp

print(sin(np.pi/2))

#단위 벡터 표기
ex= np.array([1,0])
ey= np.array([0,1])
 
#plt.arrow: 벡터 화살표 그리기 xlim: plot 영역 정하기 
plt.arrow(0,0,ex[0],ex[1],head_width=0.2,color='b')
plt.arrow(0,0,ey[0],ey[1],head_width=0.2,color='r')
plt.xlim(-2,2)
plt.ylim(-2,2)


# alpha라는 매개변수를 바꿔하며 벡터를 사용하여 일직선을 생선하자
#alpha=0->(0,1)
#alpha-1 ->(1,1)
#alpha=2->(2,1)

#A라는 행력 A*xvec=bvec: A는 Linear Operator
#A= ([[1,alpha],[0,alpha]]) 

# u= np.array([1,1])
# for alpha in np.arrange(-1,1,0.2):
#     A =np.array([[1,alpha],
#                 [0,alpha]])
# np.dot(A,ex)
# np.dot(A,ey)

# v=np.dot(A,u)
# plt.arrow(0,0,v[0],v[1],head_width=0.1,color='red')
# plt.show()

# A=np.array([[1,2],[0,3]])
# b=np.array([5,4])
# #A*x=b를 만족시키는 x 찾기

# #1 역행렬 구하기
# Ainv=np.linalg.inv(A)
# print(Ainv)
# x= np.dot(Ainv,b)
# print(x)

# #2 linalg.solve로 풀기
# x= np.linalg.solve(A,b)
# print(x)

#소거법 이용하기 

#행인 A와 B가 1차원 등가속 운동을 하고 있다 A와 B는 서로 100미터 떨어져 있으며 v_0=0m/scipy로 출발한다.A는 가속도 a_1
# B는 가속도 a_2로 걷는다 가정하자. 두사람이 서로 반대로 걸을때는 30초, 같은 방향으로 걸을땐 90가 걸린다 a_1과 a_2로 구하는 script로 만들기

A=np.array([[0.5*30**2,0.5*30**2],[0.5*90**2,-0.5*90**2]])
b=np.array([100,100])
Ainv=np.linalg.inv(A)
print(Ainv)
x=np.dot(Ainv,b)
print(x)

# A와 B 행인이 등속 운동을 한다. 서로의 초기 거리는 100m. 서로 반대방향으로 걸을때 걸리는 시간은 5초이다. 서로 같은 방향으로 걸을때 걸리는 속도는 15초

A=np.array([[5,5],[15,-15]])
b=np.array([100,100])
Ainv=np.linalg.inv(A)
print(Ainv)
x=np.dot(Ainv,b)
print(x)


A=np.array([[1,1],[1,-1]])
Ainv=np.linalg.inv(A)
b_1=np.array([3,-1])
b_2=np.array([-1,-2])
x_1=np.dot(Ainv,b_1)
x_2=np.dot(Ainv,b_2)
print(x_1,x_2)











