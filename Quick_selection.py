def QuickSelect(L,k):

	p = L[0]
	
	S = []
	B = []
	M = []
	
	for i in L:
		if i < p:
			S.append(i)
		elif i > p:
			B.append(i)
		else:
			M.append(i)
		
	if len(S) >= k:
		return QuickSelect(S, k)
	elif (len(S) + len(M) )< k:
		return QuickSelect(B, k - len(S) - len(M))
	else:
		return p
	
n, k = map(int, input().split())
L = list(map(int, input().split()))

print(QuickSelect(L,k))
 