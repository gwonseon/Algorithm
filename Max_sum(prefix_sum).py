def max_sum_array(A):
    def find(A, left, right):
        # 분할을 더이상 못하면
        # 1번과 2번 경우의 재귀를 멈추기 위한 가정
        if left == right:
            return A[0]

        else:

            m = (left + right) // 2
            # A를 m을 기준으로 왼쪽 오른쪽으로 나눠 1번 2번 경우를 구한다
            left_side = find(A, left, m)
            right_side = find(A, m + 1, right)

            # m을 기준으로 왼쪽 부분의 합
            sum = 0
            left_part = A[m]
            for i in range(m, left - 1, -1):
                sum += A[i]
                left_part = max(left_part, sum)
            # m을 기준으로 오른쪽 부분의 합
            sum = 0
            right_part = A[m + 1]
            for i in range(m + 1, right + 1):
                sum += A[i]
                right_part = max(right_part, sum)
        # 왼쪽부분(1번), 오른쪽부분(2번), 양쪽에 걸치는 경우(3번)를(을) 비교해 가장 큰 값 리턴
        return max(left_side, right_side, left_part + right_part)

    # 재귀함수로 T(n/2)씩 비교해서 2T(n/2), A개수 만큼 비교하기 때문에 cn
    return find(A, 0, len(A) - 1)


A = [int(x) for x in input().split()]
sol = max_sum_array(A)
print(sol)


# O(n^2)
