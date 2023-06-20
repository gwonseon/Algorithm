def solve(A):
    # A를 sudoku 규칙에 맞게 채운다
    row, col = find_empty_cell(A)
    if row == 0:
        return True

    for num in range(1, 10):
        if is_safe(A, row, col, num):
            A[row][col] = num
            if solve(A):
                return True
            A[row][col] = 0
    return False


def find_empty_cell(A):
    for row in range(9):
        for col in range(9):
            if A[row][col] == 0:
                return row, col
    return 0, 0


def is_safe(A, row, col, num):
    for j in range(9):
        if A[row][j] == 0:
            return False

    for i in range(9):
        if A[i][col] == 0:
            return False

    row_s = 3 * int(row / 3)
    col_s = 3 * int(col / 3)
    row_e = row_s + 3
    col_e = col_s + 3

    for i in range(row_s, row_e):
        for j in range(col_s, col_e):
            if A[i][j] == 0:
                return False
    return True

A = [0]*9
for i in range(9):
	row = [int(x) for x in input()]
	A[i] = row


print(solve(A))