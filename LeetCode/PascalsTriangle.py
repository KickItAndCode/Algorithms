# 118. Pascal's Triangle

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
def generate(numRows):
    res = []
    row = [1]
    for i in range(numRows):
        newRow = [0] * (i + 1)
        for j in range(i + 1):
            newRow[j] = getItem(row, j-1) + getItem(row, j)
        row = newRow
        res.append(row)
    return res


def getItem(arr, index):
    if index < 0 or index >= len(arr):
        return 0
    return arr[index]


print(generate(7))
