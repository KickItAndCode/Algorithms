# 994. Rotting Oranges

# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell
# the value 1 representing a fresh orange
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent(4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


# Example 1:


# Input: [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4
# Example 2:

# Input: [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1
# Explanation:  The orange in the bottom left corner(row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0, 2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


# Approach 1: Breadth-First Search
# Intuition

# Every turn, the rotting spreads from each rotting orange to other adjacent oranges. Initially, the rotten oranges have 'depth' 0 [as in the spanning tree of a graph], and every time they rot a neighbor, the neighbors have 1 more depth. We want to know the largest possible depth.

# Algorithm

# We can use a breadth-first search to model this process. Because we always explore nodes (oranges) with the smallest depth first, we're guaranteed that each orange that becomes rotten does so with the lowest possible depth number.

# We should also check that at the end, there are no fresh oranges left.


def orangesRotting(self, grid):
    R, C = len(grid), len(grid[0])

    # queue - all starting cells with rotting oranges
    queue = collections.deque()
    for r, row in enumerate(A):
        for c, val in enumerate(row):
            if val == 2:
                queue.append((r, c, 0))

    def neighbors(r, c):
        for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

    d = 0
    while queue:
        r, c, d = queue.popleft()
        for nr, nc in neighbors(r, c):
            if A[nr][nc] == 1:
                A[nr][nc] = 2
                queue.append((nr, nc, d+1))

    if any(1 in row for row in A):
        return -1
    return d

 def orangesRotting(self, grid):
        n,m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append((i,j))
        res = 0
        while Q:
            for _ in range(len(Q)):
                i,j = Q.popleft()
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x,y))
            res += 1
        return max(0, res-1) if cnt == 0 else -1


def orangesRotting(self, grid: List[List[int]]) -> int:
    row, col = len(grid), len(grid[0])
    rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
    timer = 0
    while fresh:
        if not rotting: return -1
        rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
        fresh -= rotting
        timer += 1
    return timer
