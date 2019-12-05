# 378. Kth Smallest Element in a Sorted Matrix
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# You may assume k is always valid, 1 ≤ k ≤ n2.


from heapq import *


def kthSmallest(matrix, k):
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heappush(heap, matrix[i][j])
    for i in range(k - 1):
        heappop(heap)

    return heappop(heap)


print(kthSmallest([
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 8))
