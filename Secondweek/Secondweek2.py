#python은 element끼리 연산하는 것 보단 행렬이나 벡터단위로 연산하는게 훨씬 빠름
#python은 element끼리 연산해야 한다면 numpy-array보단 list를 사용하는게 연산이 빠름
#즉 numpy 사용땐 for문을 되도록 지양하는 것이 좋다

#LU Decomposition
#A의 역행렬을 구하는 연산은 행렬 사이즈 n에 4~5승에 비례하는 어마어마한 연산량을 필요로함
#어떤 행렬 A를 상삼각행렬L와 하 삼각행렬 U의 행렬곱으로 표현하는 것
#Gauss Elimination 처럼 연산량이 비교적 적은 선형방정식 풀이법
#L(하삼각행렬):대각성분 오른쪽 위가 0,대각성분은 1(변수를 줄이기 위해) 
#U(상삼각행렬):대각성분 왼쪽 아래가 0
#기본 노테이션:A=LU, Ax=LUx=b
#절차1.Ux=y로 두면 Ly=b로 y를 풀고
#절차2.Ux=y를 푼다
#LU분해는 scipy에 있음
import numpy as np
import scipy.linalg # 

a=np.array([[1,4,1],[1,6,1],[2,-1,2]])

