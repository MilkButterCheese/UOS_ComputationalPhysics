import numpy as np
import math
from scipy.special import factorial2
from scipy import special 
import matplotlib.pyplot as plt


# #Problem1 erfc과 부분합 그래프 그리기

# #정의역 정하기
# x= np.linspace(1,4,1000)

# #erfc 함수 부여하기
# erfc=special.erfc(x)

# #S0 정하기
# S0=np.exp(-x**2)/(x*np.sqrt(np.pi)) 

# # S5와 S10 구하기
# S5=0
# S10=0

# for k in range(0,5):
#         S5 = S5+ np.exp(-x**2)/(x*np.sqrt(np.pi))* (-1)**k * factorial2(2*k-1,)/(2*x**2)**k
        
# for k in range(0,10):
#         S10 = S10+ np.exp(-x**2)/(x*np.sqrt(np.pi))* (-1)**k * factorial2(2*k-1,)/(2*x**2)**k

# plt.ylim(-1,1)
# plt.plot(x,erfc,'r')
# plt.plot(x,S0,'b')
# plt.plot(x,S5,'g')
# plt.plot(x,S10,'violet')
# plt.show()


#Problem2 erfc과 부분합 오차 구하기

#x=2로 정하기
x=2 

#erfc함수 정해두기
erfc=special.erfc(x)

#S[k] 정하기
S=np.zeros([1,10])
for k in range(0,10):
    for j in range(0,k+1):
        if j==0:
            S[0,k]= S[0,k] + np.exp(-x**2)/(x*np.sqrt(np.pi))
        else:
            S[0,k] = S[0,k]+ np.exp(-x**2)/(x*np.sqrt(np.pi))* (-1)**j * factorial2(2*j-1,)/(2*x**2)**j   

#오차 계산하기(%단위로 구함)
erofer=np.zeros([1,10])       
for k in range(0,10):
    erofer[0,k] = abs(erfc-S[0,k])/erfc *100
    
print(S)
print(erofer)



k=np.array([0,1,2,3,4,5,6,7,8,9])
plt.xlim(0,10)
plt.ylim(0,10)
plt.plot(k,erofer[0,k],'r')
plt.show()