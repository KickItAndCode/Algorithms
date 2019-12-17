# 695. Max Area of Island
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the sgiven grid does not exceed 50.


def maxAreaOfIsland(grid):
    max_res = 0

    # traverse matrix
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # anytime we find an island we do dfs
            if grid[i][j] == 1:
                max_res = max(max_res, dfs(grid, i, j))

    return max_res


def dfs(grid, i, j):
    # make sure its in bounds
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
        return 0

    # flip to 0 to not count it again later
    grid[i][j] = 0
    count = 1

    count += dfs(grid, i + 1, j)
    count += dfs(grid, i - 1, j)
    count += dfs(grid, i, j + 1)
    count += dfs(grid, i, j - 1)
    return count


print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

# maxAreaOfIsland([[0,0,0,0,0,0,0,0]])
