import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#t와 m=sin(alpha/2)^2 준비하기
t=np.linspace(0,10,100)
m=np.array([np.sin(0.00873/2)**2,np.sin(0.262/2)**2,np.sin(0.524/2)**2,np.sin(0.785/2)**2,np.sin(1.05/2)**2])
alpha=[0.00873,0.262,0.524,0.785,1.05]

#ellipj로 타원 함수들 불러오기
ellipf1= np.array(sp.ellipj(t,m[0]))
ellipf2= np.array(sp.ellipj(t,m[1]))
ellipf3= np.array(sp.ellipj(t,m[2]))
ellipf4= np.array(sp.ellipj(t,m[3]))
ellipf5= np.array(sp.ellipj(t,m[4]))

#ellipj 함수서 sn함수만 뺴오기
sn1=ellipf1[0,:]
sn2=ellipf2[0,:]
sn3=ellipf3[0,:]
sn4=ellipf4[0,:]
sn5=ellipf5[0,:]

#theta값 정의하기
theta1=2*np.arcsin(np.sqrt(m[0])*sn1)
theta2=2*np.arcsin(np.sqrt(m[1])*sn2)
theta3=2*np.arcsin(np.sqrt(m[2])*sn3)
theta4=2*np.arcsin(np.sqrt(m[3])*sn4)
theta5=2*np.arcsin(np.sqrt(m[4])*sn5)

#K값 정의하기
K1= np.array(sp.ellipk(m[0]))
K2= np.array(sp.ellipk(m[1]))
K3= np.array(sp.ellipk(m[2]))
K4= np.array(sp.ellipk(m[3]))
K5= np.array(sp.ellipk(m[4]))

#그래프 그리기

plt.plot(t*K1,theta1/alpha[0],'r')
plt.plot(t*K2,theta2/alpha[1],'g')
plt.plot(t*K3,theta3/alpha[2],'b')
plt.plot(t*K4,theta4/alpha[3],'y')
plt.plot(t*K5,theta5/alpha[4],'m')
plt.show()