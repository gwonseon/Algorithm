def two_sum(X, Y, t):
    for i in X:  # O(n)
        j = t - i
        left, right = 0, len(Y) - 1
        while left <= right:  # O(log n)
            m = (right + left) // 2
            if Y[m] < j:
                left = m + 1
            elif Y[m] > j:
                right = m - 1
            else:
                return True
    return False

    # O(n log n)


# 함수 two_sum을 적절한 형식으로 호출해 그 결과를 이용해 결과 출력
#
def three_sum(X, Y, Z):  # O(n^2 log n)
    for z in Z:
        if two_sum(X, Y, -z) == True:
            return True
    return False


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

print(three_sum(A, B, C))

# 수행시간 분석 및 Big-O 표기
# T(n) = O(n^2 log n)