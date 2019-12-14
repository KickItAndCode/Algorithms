# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.


# Run time O(row * log(column))


def searchMatrix(matrix, target):
    def targetInRow(row, target):
        left, right = 0, len(row)-1
        while left <= right:
            mid = (left + right) // 2
            cur = row[mid]
            # print(cur, end=' ')
            if cur == target:
                return True
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    ans = False
    for row in matrix:
        # print(row)
        if not row or row[0] > target or ans == True:
            return ans
        ans = targetInRow(row, target)
    return ans


# O(m+n)
def searchMatrix2(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False
    row, col = 0, len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        cur = matrix[row][col]
        if cur == target:
            return True
        elif cur > target:
            col -= 1
        else:
            row += 1
    return False


print(searchMatrix2([
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 5))  # True


print(searchMatrix2([
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 20))  # false
