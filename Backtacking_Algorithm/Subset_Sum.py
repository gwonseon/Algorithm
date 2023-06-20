def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
    global sol
    v_sum = sum(A[i]*x[i] for i in range(k))
    if k == len(A):
        return
    else:
        if v_sum + A[k] <= S:
            x[k] = 1
            if v_sum + A[k] == S:
                sol += 1
                print_subset(x)
            else:
                subset_sum(k+1)
            x[k] = 0
            subset_sum(k+1)

A = list(set(int(x) for x in input().split()))
A.sort()
sol = 0
S = int(input())
x = [0] * len(A)
subset_sum(0)
if sol == 0:
    print([])
