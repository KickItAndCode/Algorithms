# 419. Battleships in a Board
# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


def countBattleships(board):
    res = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            # found
            if board[i][j] == "X":
                res += 1
                dfs(i, j, board)
    return res


def dfs(i, j, board):
    # invalid cases
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != "X":
        return

    board[i][j] = "."
    dfs(i+1, j, board)
    dfs(i-1, j, board)
    dfs(i, j+1, board)
    dfs(i, j, board)

# faster version taking advantage of the fact that its always coming from above or to the left


def countBattleships2(board):
    res = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            # keep going if not a ship
            if board[i][j] == ".":
                continue
            # verticalally still on same ship
            if i > 0 and board[i-1][j] == "X":
                continue
            # horizontally still on the same ship
            if j > 0 and board[i][j-1] == "X":
                continue

            res += 1
    return res


print(countBattleships2([["X", ".", ".", "X"], [
      ".", ".", ".", "X"], [".", ".", ".", "X"]]))  # 2
