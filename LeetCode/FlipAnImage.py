# 832. Flipping an Image


# iven a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example 1:

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:

# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

#    In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
# helps us find the i-th value of the row, counting from the right.

# Time Complexity: O(N)O(N), where N is the total number of elements in A.
# Space Complexity: O(1)O(1) in additional space complexity.
def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    for row in A:
        for i in range((len(row)+1) // 2):
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1

    return A


def flipAndInvertImage2(A):
    return [[1 - i for i in i[::-1]] for i in A]


def flipAndInvertImage3(A):
    # traverse verticall
    for i in range(len(A)):
        j = 0
        k = len(A[i]) - 1
        # reverse horizontal
        while j < k:
            A[i][k], A[i][j] = A[i][j], A[i][k]
            j += 1
            k -= 1

        for j in range(len(A[i])):
            A[i][j] = A[i][j] ^ 1  # if its 1 make it 0 if its 0 make it 1

    return A


def flipAndInvertImage4(A):
    for row in A:
        row.reverse()

    n_rows, n_cols = len(A), len(A[0])
    for row in range(0, n_rows):
        for col in range(0, n_cols):
            A[row][col] = A[row][col] ^ 1
    return A


print(flipAndInvertImage3([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
