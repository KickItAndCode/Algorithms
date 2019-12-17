# https: // leetcode.com/problems/number-of-distinct-islands/
# 694. Number of Distinct Islands
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's(representing land) connected 4-directionally(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated(and not rotated or reflected) to equal the other.

# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.

# Notice that:
# 11
# 1
# and
# 1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.


def numDistinctIslands(self, grid: List[List[int]]) -> int:
    seen = set()

    def explore(r, c, di=0):
        if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                grid[r][c] and (r, c) not in seen):
            seen.add((r, c))
            shape.append(di)
            explore(r+1, c, 1)
            explore(r-1, c, 2)
            explore(r, c+1, 3)
            explore(r, c-1, 4)
            shape.append(0)

    shapes = set()
    for r in xrange(len(grid)):
        for c in xrange(len(grid[0])):
            shape = []
            explore(r, c)
            if shape:
                shapes.add(tuple(shape))

    return len(shapes)


def numDistinctIslands(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    self.steps = ''
    distinctIslands = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # 'o' for origin
                self.helper(grid, i, j, 'o')
                distinctIslands.add(self.steps)
                self.steps = ''
    return len(distinctIslands)


def helper(self, grid, i, j, direct):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
        self.steps += direct
        grid[i][j] = 0
        self.helper(grid, i+1, j, 'd')  # down
        self.helper(grid, i-1, j, 'u')  # upper
        self.helper(grid, i, j+1, 'r')  # right
        self.helper(grid, i, j-1, 'l')  # left
        self.steps += 'b'  # back
