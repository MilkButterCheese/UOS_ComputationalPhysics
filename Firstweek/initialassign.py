import numpy as np 
import matplotlib.pyplot as plt 
import scipy

#Problem2
#https://github.com/MilkButterCheese/UOS_ComputationalPhysics


#Problem3
ex=np.array([1,0]) 
ey=np.array([0,1])

# A*ex=[a,0] A*ey=[0,1]
for a in np.arange(-1,1,0.1):
    A= ([[0,a],[0,1]]) 
    y=np.dot(A,ey)
    plt.arrow(0,0,y[0],y[1],head_width=0.01,color='red')
    plt.axhline(y=1, color='b', linewidth=0.01)
    plt.show


#Problem4 
#0.5*A*(u+v)=A*ex, 0.5*A*(u-v)=A*ey
Acol1= 0.5*(np.array([3,2])+np.array([-1,-2]))
Acol2= 0.5*(np.array([3,2])-np.array([-1,-2]))
A=np.c_[Acol1,Acol2]
print(A)

#Problem 5
#x+y=40, 2x+4y=92 
A=np.array([[1,1],[2,4]])
Ainv=np.linalg.inv(A)
b=np.array([40,92])
y=np.dot(Ainv,b)
print(y)
# x=34 닭의 수 y=6 토끼의 수
