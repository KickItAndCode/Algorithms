# 54. Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


def spiralOrder(matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))  # left to right
        if matrix and matrix[0]:  # top to dwon
            for row in matrix:
                res.append(row.pop())
        if matrix:  # right to left
            res.extend(matrix.pop()[::-1])
        if matrix and matrix[0]:  # bottom to up
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res


def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    ans = []
    m, n = len(matrix), len(matrix[0])
    u, d, l, r = 0, m - 1, 0, n - 1
    while l < r and u < d:
        ans.extend([matrix[u][j] for j in range(l, r)])
        ans.extend([matrix[i][r] for i in range(u, d)])
        ans.extend([matrix[d][j] for j in range(r, l, -1)])
        ans.extend([matrix[i][l] for i in range(d, u, -1)])
        u, d, l, r = u + 1, d - 1, l + 1, r - 1
    if l == r:
        ans.extend([matrix[i][r] for i in range(u, d + 1)])
    elif u == d:
        ans.extend([matrix[u][j] for j in range(l, r + 1)])
    return ans


print(spiralOrder(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
))
