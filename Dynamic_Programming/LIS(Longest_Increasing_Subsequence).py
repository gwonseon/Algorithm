def print_IS(seq, x):
    LIST = [0] * len(seq)
    for i in range(len(seq)):
        if x[i]:
            LIST[i] = seq[i]
        else:
            print("_", end="")


def LIS_DP(seq):
    N = len(seq)
    x = [0] * N
    dp = [1] * N
    # LIS 알고리즘
    for i in range(1, N):
        for j in range(0, i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp), print_IS(dp, seq)


seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)