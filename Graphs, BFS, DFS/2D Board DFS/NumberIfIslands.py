# 200. Number of Islands

# Given a 2d grid map of '1's(land) and '0's(water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

#  This problem uses dfs by\if they have been explored
#  So when they cell is seen again they aren't counted as an addional island


def numIslands(grid):
    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return 0
        # set to 0 to not visit again
        grid[i][j] = '0'
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j-1)
        return 1

    numIslands = 0
    if not grid:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                # visited an island
                numIslands += dfs(grid, i, j)

    return numIslands


# print(numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
#       "1", "1", "0", "0", "0"], ["0", "0", "0", "0, "0"]]))
print(numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "", "0"], [
      "0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
