
# 490. The Maze


# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.


# Example 1:

# Input 1: a maze represented by a 2D array

# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0

# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)

# Output: true

# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

# Example 2:

# Input 1: a maze represented by a 2D array

# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0

# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)

# Output: false

# Explanation: There is no way for the ball to stop at the destination.


# Note:

# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.


# this problem is from elements of programmning in python not leetcode

from collections import deque
from collections import namedtuple
Coordinate = namedtuple('Coordinate', ('x', 'y'))
WHITE, BLACK = range(2)

# Time O (V + E) vertices and edges


def searchMaze(maze: List[List[int]], s: Coordinate, e: Coordinate):

    def searchMazeHelper(curr):
        # check curr is within maze and is a white pixel
        if not(0 <= curr.x < len(maze) and 0 <= curr.y < len(maze[curr.x])) and maze[curr.x][curr.y] == WHITE:
            return False
        path.append(curr)

        maze[curr.x][curr.y] = BLACK

        if curr == e:
            return True

        # tricking run maze helper on each direction of the cell
        if any(map(searchMazeHelper, map(Coordinate, (curr.x - 1, curr.x + 1, curr.x, curr.x), (curr.y, curr.y, curr.y - 1, curr.y + 1)))):
            return True

        # Cannot find a path, remove the emtry added in path.append(curr)
        del path[-1]
        return False

    path = []
    searchMazeHelper(s)
    return path


# https://leetcode.com/articles/the-maze/

# BFS solution
def hasPath(self, maze, start, destination):
    queue = [start]
    n = len(maze)
    m = len(maze[0])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while queue:
        i, j = queue.pop(0)
        # mark visited
        maze[i][j] = 2

        if i == destination[0] and j == destination[1]:
            return True

        for x, y in dirs:
            row = i + x
            col = j + y
            while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                row += x
                col += y
            row -= x
            col -= y
            if maze[row][col] == 0:
                queue.append([row, col])
    return False

# DFS solution


def hasPath(self, maze, start, destination):
    m, n = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    def dfs(x, y):
        if x == destination[1] and y == destination[0]:
            return True
        if (x, y) in visited:
            return False
        visited.add((x, y))
        for d in directions:
            xx, yy = x, y
            while 0 <= xx < n and 0 <= yy < m and (not maze[yy][xx]):
                xx += d[0]
                yy += d[1]
            xx -= d[0]
            yy -= d[1]
            if dfs(xx, yy):
                return True
        return False

    return dfs(start[1], start[0])


class Solution(object):
    def hasPath(self, matrix, start, end):
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # up down left right
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        visited[start[0]][start[1]] = True

        q = deque([start])

        while q:
            tup = q.popleft()
            if tup[0] == end[0] and tup[1] == end[1]:
                return True

            for dir in dirs:
                # Roll the ball until it hits a wall
                row = tup[0] + dir[0]
                col = tup[1] + dir[1]

                while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 0:
                    row += dir[0]
                    col += dir[1]

                # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
                (new_x, new_y) = (row - dir[0], col - dir[1])

                # Check if the new starting position has been visited
                if not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
        return False
