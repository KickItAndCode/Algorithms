# 289. Game of Life
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, 1), (1, -1), (-1, -1))
    rows = len(board)
    cols = len(board[0])

    copyBoard = [[board[row][col]
                  for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):

            liveNeighbors = 0
            for x, y in dirs:
                xx, yy = row + x, col + y

                # validate and do something
                if 0 <= xx < len(board) and 0 <= yy < len(board[0]) and copyBoard[xx][yy] == 1:
                    liveNeighbors += 1

            if copyBoard[row][col] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                board[row][col] = 0

            if copyBoard[row][col] == 0 and liveNeighbors == 3:
                board[row][col] = 1
