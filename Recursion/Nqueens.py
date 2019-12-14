# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


# def solveNQueens(n):
#     def helper(row):
#         if row == n:
#             # all queens legally places
#             result.append(col_placement[:])
#             return
#         for col in range(n):
#             if all(abs(c-col) not in (0, row-i) for i, c in enumerate(col_placement[:row])):
#                 col_placement[row] = col
#                 helper(row + 1)
#     result = []
#     col_placement = [0] * n
#     helper(0)
#     return result


# print(solveNQueens(4))


def solveNQueens(n):

    def helper(row, n, colPlacements, res):
        if row == n:
            # all n queens ahve been placed in the n rows. We have reached the bottom of our recursion. We can now add the colplacements to the result
            res.append(generateBoardFromPlacements(colPlacements, n))
            return

        # try all columns in the current row that we are making a choice on.

        # the colPlacements list will hold the column we place a queen for the i'th row

        # so if I have [1,3,0,2] that means it s a 4x4 grid
        # row index 0 has a queen placed in column index 1
        # row index 1 has a queen placed in column index 3
        # row index 2 has a queen placed in column index 0
        # row index 3 has a queen placed in column index 2

        for col in range(n):
            # record a column placement for this row
            colPlacements.append(col)

            # if it is a valid placement we recurse t work on the nedt row row +1 in a recursive call

            if isValid(colPlacements):
                helper(row + 1, n, colPlacements, res)

            # we are done exploring with the placement and now we will remove it from our colplacements we will loop back around and try more columnb placements for this row if theyre are any left

            del colPlacements[-1]

    def isValid(colPlacements):
        rowWeAreValidatingOn = len(colPlacements) - 1
        # loop and check our placements in every row previous against the placement that we just made
        for ithQueenRow in range(rowWeAreValidatingOn):
           #  Get the absolute difference between:
           #  The column of the already placed queen we are comparing against -> colPlacements.get(ithQueenRow)
           # The column of the queen we just placed -> colPlacements.get(rowWeAreValidatingOn)

            distance = abs(
                colPlacements[ithQueenRow] - colPlacements[rowWeAreValidatingOn])

            # if the absolute distance is 0
            # then we placed in a columb being attacked by the i'th queen

            # if the absolute distance is == rowDistance
            # then queen is getting attacked diagonally

            rowDistance = rowWeAreValidatingOn - ithQueenRow
            if distance == 0 or distance == rowDistance:
                return False
        return True

    def generateBoardFromPlacements(colPlacements, n):
        board = []
        totalItemsPlaced = len(colPlacements)
        for row in range(totalItemsPlaced):
            s = ''
            for col in range(n):
                if col == colPlacements[row]:
                    s += "Q"
                else:
                    s += '.'
            board.append(s)
        return board

    res = []
    helper(0, n, [], res)
    return res


print(solveNQueens(4))
