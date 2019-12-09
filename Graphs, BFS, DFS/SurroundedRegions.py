# 130. Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


# "Save Every O region "
from collections import deque


def solve1(board):
    if not any(board):
        return

    m, n = len(board), len(board[0])

    # gets every value that is on the edge rows along the boundary
    save = [(i, j) for k in range(max(m, n))
            for (i, j) in ((0, k), (m-1, k), (k, 0), (k, n-1))]

    while save:
        i, j = save.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
    # Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.
    board[:] = [['X' if c != 'S' else "O" for c in row] for row in board]
    return board


def solve(board):
    queue = deque([])

    # gets every value that is on the edge rows along the boundary
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
            board[r][c] = "D"
            queue.append((r-1, c))
            queue.append((r+1, c))
            queue.append((r, c-1))
            queue.append((r, c+1))

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "D":
                board[r][c] = "O"
    return board


print(solve(
    [
        ["X", "X", "X", "X"],
        ["O", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
))

# result
# X X X X
# X X X X
# X X X X
# X O X X
