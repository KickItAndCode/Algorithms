# 59. Spiral Matrix II
# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


def generateMatrix2(n):
    if not n:
        return []
    res = [[0 for _ in range(n)] for _ in range(n)]
    left, right, top, down, num = 0, n-1, 0, n-1, 1
    while left <= right and top <= down:
        for i in range(left, right+1):
            res[top][i] = num
            num += 1
        top += 1
        for i in range(top, down+1):
            res[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left-1, -1):
            res[down][i] = num
            num += 1
        down -= 1
        for i in range(down, top-1, -1):
            res[i][left] = num
            num += 1
        left += 1
    return res


def generateMatrix(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        if A[(i+di) % n][(j+dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


print(generateMatrix2(3))
