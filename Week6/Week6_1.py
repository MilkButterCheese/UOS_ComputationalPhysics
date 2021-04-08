import numpy as np
from scipy.interpolate import* 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#Interpolation
#Interpid
#polyfit
#spline Interpolation Univariate Spline

#보간법 내삽
#데이터 좌표들이 주어졌을 때, 좌표들을 잇는 연속적인 그래프를 찾기
#Polynomial Interpolation: 그래프를 다항식으로 찾음

#Cubic spline

# x=np.array([1,2,3,4,5])
# y=np.array([3,6,3,6,4])
# #다항식 Fitting 
# pfit= np.polyfit(x,y,4)
# # print(pfit) #[0.2 3.8]이 나오는데 높은 차수부터 내려옴. y=0.2x+3.8..
# line= np.poly1d(pfit)
# xx=np.linspace(0,6,50)
# yy=line(xx)

# plt.plot(x,y,'*')
# plt.plot(xx,yy)
# plt.plot()

#data point 갯수와 같은 차수의 Polynomial로 그래프를 찾을시
#포인트들과  완벽히 맞게 됨

# # Optimize.curve_fit(f,xdata,ydata)

# def f(x,m,b): # 1차 함수
#     return m*x +b 

# parm, var= curve_fit(f,x,y)

# yy1=f(xx,parm[0],parm[1])
# print(yy1)
# plt.plot(x,y,'*')
# plt.plot(xx,yy1)
# plt.plot()

#Problem1
x= np.array([-2,1,4,-1,3,-4])
y= np.array([-1,2,59,4,24,-53])
pfit= np.polyfit(x,y,5)
line= np.poly1d(pfit)
xx=np.linspace(-5,5,50)
yy=line(xx)

plt.plot(x,y,'*')
plt.plot(xx,yy)
plt.plot()

#Problem2
#Data2.txt를 f(X)=A*sin(B*x+C) 꼴로 만들기
data= np.genfromtxt('/workspace/UOS_ComputationalPhy/Week6/Data2.txt',delimiter=',')
x=data[0]
y=data[1]

#data= loadtxt('filename',dtyple=None,delimiter=',')
#데이터를 못불러오네.. 
def f(x,A,B,C): # 1차 함수
    return A*np.sin(B*x+C)

parm, var= curve_fit(f,x,y)

xx=np.linspace(-2,10,60)
yy1=f(xx,parm[0],parm[1],parm[2])
print(yy1)
plt.plot(x,y,'*')
plt.plot(xx,yy1)
plt.plot()


#Problem3 
#v=v0*(1-exp(-t/tau)) 
#v=vo*(1-exp(-gamma*t))
# xx= np.linspace(0,1,100)
# yy=veloc(xx,5,0.1)
#plot(xx,yy,'_')

#