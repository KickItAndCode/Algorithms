# 286. Walls and Gates
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:
# INF - 1  0  INF
# INF INF INF - 1
# INF - 1 INF - 1
# 0 - 1 INF INF
# After running your function, the 2D grid should be:
#     3 - 1   0   1
#     2   2   1 - 1
#     1 - 1   2 - 1
#     0 - 1   3   4

# standard DFS
# if you find a gate then run DFS on that cell


def wallsAndGates(rooms):
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            # found gate
            if rooms[i][j] == 0:
                dfs(i, j, rooms, 0)
    return rooms


def dfs(i, j, rooms, count):
    if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < count:
        return

    rooms[i][j] = count
    dfs(i+1, j, rooms, count + 1)
    dfs(i-1, j, rooms, count + 1)
    dfs(i, j+1, rooms, count + 1)
    dfs(i, j-1, rooms, count + 1)


print(wallsAndGates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647,
                                                       2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]))

# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
