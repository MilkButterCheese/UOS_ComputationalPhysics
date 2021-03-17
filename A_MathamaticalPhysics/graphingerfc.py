import numpy as np
import math
from scipy.special import factorial2
from scipy import special 
import matplotlib.pyplot as plt

#정의역 정하기
x= np.linspace(1,4,1000)

#erfc 함수 부여하기
erfc=special.erfc(x)

#S0 정하기
S0=np.exp(-x**2)/(x*np.sqrt(np.pi)) 

# S5와 S10 구하기
S5=0
S10=0

for k in range(0,5):
        S5 = S5+ np.exp(-x**2)/(x*np.sqrt(np.pi))* (-1)**k * factorial2(2*k-1,)/(2*x**2)**k
        
for k in range(0,10):
        S10 = S10+ np.exp(-x**2)/(x*np.sqrt(np.pi))* (-1)**k * factorial2(2*k-1,)/(2*x**2)**k

plt.ylim(-1,1)
plt.plot(x,erfc,'r')
plt.plot(x,S0,'b')
plt.plot(x,S5,'g')
plt.plot(x,S10,'violet')
plt.show()

