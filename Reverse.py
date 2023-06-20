
# 재귀 방법
def reverse(L, a):
	n = len(L)
	if a < n//2:
		L[a], L[n-1-a] = L[n-1-a], L[a]
		reverse(L, a+1)

L = list(input())  # 문자열을 입력받아 리스트로 변환
reverse(L, 0)
print(''.join(str(x) for x in L))


# 비재쥐 방법
def reverse(A):
	n, i = len(A), 0
	while i < n//2:
		A[i], A[n-1-i] = A[n-1-i], A[i]
		i += 1

A = list(input())  # 문자열을 입력받아 리스트로 변환
reverse(A)
print(''.join(str(x) for x in A))

