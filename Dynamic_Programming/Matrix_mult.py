import math

def matrix_mult(P,n,C):
    for L in range(2,n+1):
      for i in range(1, n-L+2):
        j = i + L -1
        C[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
        for k in range(i, j):
          cost = C[i][k] + C[k+1][j] + P[i-1]*P[k]*P[j]
          if cost < C[i][j]:
            C[i][j] = cost
    return C[1][n]

n = int(input()) # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
p = [int(x) for x in input().split()] # M_i = p_i x p_{i+1}
C = [[0]*(n+1) for _ in range(n+1)] # 비용을 저장할 2차원 리스트 C 초기화
for i in range(1,n):
	C[i][i] = 0
min_cost = matrix_mult(p,n,C)
print(min_cost)