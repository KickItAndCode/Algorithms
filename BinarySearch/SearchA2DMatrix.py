# 74. Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false


def searchMatrix(matrix, target):

    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    l, r = 0, m*n - 1
    while l <= r:

        mid = l + (r - l) // 2
        midEl = matrix[mid // n][mid % n]
        if target == midEl:
            return True
        elif midEl < target:
            l = mid + 1
        elif midEl > target:
            r = mid - 1

    return False


print(searchMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15))
