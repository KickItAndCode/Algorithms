# 63. Unique Paths II

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right


def uniquePathsWithObstacles(obstacleGrid):
    iLen, jLen = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for x in range(jLen)] for x in range(iLen)]

    # make first cell 1 or 0 if it has a obstacle

    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(0, iLen):
        for j in range(0, jLen):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i + 1 >= 0:
                    dp[i][j] += dp[i+1][j]
                if j + 1 >= 0:
                    dp[i][j] += dp[i][j+1]
    return dp[0][-1]


print(uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
