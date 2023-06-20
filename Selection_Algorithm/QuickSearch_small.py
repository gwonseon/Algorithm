def QuickSelect(L, k):
    A, M, B = [], [], [] # Small, Middle, Large sets to p
    p = L[0]  # pivot p is the first element of A
    for a in L:
        if a < p: A.append(a)
        elif a == p: M.append(a)
        else: B.append(a)
    if len(A) >= k: return QuickSelect(A, k)
    elif len(A)+len(M) < k: return QuickSelect(B, k-len(A)-len(M))
    else: return p

A = [int(x) for x in input("n개의 수를 차례로 입력: ").split()]
k = int(input("몇 번째로 작은 수를 원하나요? "))
print(QuickSelect(A, k))


# WorstCase : O(n^2)
# BestCase  : O(n)

