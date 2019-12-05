# 64. Minimum Path Sum
# iven a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


def minPathSum(grid):

    if not grid:
        return

    r, c = len(grid), len(grid[0])
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    # initialize the first row by adding the only path vertically
    # [1 0 0]
    # [2 0 0]
    # [6 0 0]
    for i in range(1, r):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    # then add horizontally
    # [1 4 5]
    # [2 0 0]
    # [6 0 0]
    for i in range(1, c):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    # now take the min of the path above it or the path to its left plus the curr val
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]


# O(2*n) space
def minPathSum2(grid):
    if not grid:
        return
    r, c = len(grid), len(grid[0])
    pre = cur = [0] * c
    pre[0] = grid[0][0]
    for i in range(1, c):
        pre[i] = pre[i-1] + grid[0][i]
    for i in range(1, r):
        cur[0] = pre[0] + grid[i][0]
        for j in range(1, c):
            cur[j] = min(cur[j-1], pre[j]) + grid[i][j]
        pre = cur
    return cur[-1]

# O(n) space


def minPathSum(grid):
    if not grid:
        return
    r, c = len(grid), len(grid[0])
    cur = [0] * c
    cur[0] = grid[0][0]
    for i in range(1, c):
        cur[i] = cur[i-1] + grid[0][i]
    for i in range(1, r):
        cur[0] += grid[i][0]
        for j in range(1, c):
            cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
    return cur[-1]

# change the grid itself


def minPathSum4(grid):
    if not grid:
        return
    r, c = len(grid), len(grid[0])
    for i in range(1, c):
        grid[0][i] += grid[0][i-1]
    for i in range(1, r):
        grid[i][0] += grid[i-1][0]
    for i in range(1, r):
        for j in range(1, c):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


print(minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
))  # 7 Explanation: Because the path 1→3→1→1→1 minimizes the sum.
