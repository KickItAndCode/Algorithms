# 79. Word Search
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# # board =
#  [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


def exist(board, word):

    for i in range(len(board)):
        for j in range(len(board[0])):
            # find first letter
            if board[i][j] == word[0] and dfs(board, i, j, 0,  word):
                return True

    return False


def dfs(board, i, j, count, word):
    # found word
    if count == len(word):
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
        return False

    temp = board[i][j]
    board[i][j] = " "

    found = dfs(board, i+1, j, count + 1, word) or dfs(board, i-1, j, count + 1,
                                                       word) or dfs(board, i, j-1, count + 1, word) or dfs(board, i, j+1, count + 1, word)

    board[i][j] = temp
    return found


print(exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCCED"))  # true
print(exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "SEE"))  # true
print(exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCB"))  # false
