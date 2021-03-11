import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#종속변수 설정하기
k=np.array([0.25 ,0.5 ,0.75 ,0.9 ,0.99])
u=np.linspace(-0.5,0.5,100)

#타원적분 K(k)함수값 구하기
integralk=sp.ellipk(k)
print(integralk)


#타원함수 모음집에서 sn,cu,dn함수만 꺼내오기, 주기를 1로  normalize 하기
ellipf1=np.array([sp.ellipj(u*4*integralk[0],k[0])])
ellipf2=np.array([sp.ellipj(u*4*integralk[1],k[1])])
ellipf3=np.array([sp.ellipj(u*4*integralk[2],k[2])])
ellipf4=np.array([sp.ellipj(u*4*integralk[3],k[3])])
ellipf5=np.array([sp.ellipj(u*4*integralk[4],k[4])])
y1=ellipf1[0,0,:]
y2=ellipf2[0,0,:]
y3=ellipf3[0,0,:]
y4=ellipf4[0,0,:]
y5=ellipf5[0,0,:]

#그래프 그리기
plt.plot(u,y1)
plt.plot(u,y2)
plt.plot(u,y3)
plt.plot(u,y4)
plt.plot(u,y5)
plt.show()


