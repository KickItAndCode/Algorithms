def fillSurroundedRegions(board):
    m, n = len(board), len(board[0])
    # track W's to be processed and start with a set of vertices
    queue = ([(i, j)for k in range(n) for i, j in ((k, 0), (k, m-1))] +
             [(i, j) for k in range(m) for i, j in((0, k), (n-1, k))])

    while queue:
        x, y = queue.pop(0)
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = "T"
            # add each surrounding cell to the queue
            queue.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

        # loop through each row in the board
        # then each cell in board
        # if the value isn't T then place B
        # if it is T place B
    board[:] = [['B' if c != 'T' else "W" for c in row] for row in board]
    return board


print(fillSurroundedRegions([
    ['B', "B", "B", "B"],
    ["W", "B", "W", "B"],
    ['B', "W", "W", "B"],
    ['B', "B", "B", "B"]
]))
print(fillSurroundedRegions([
    ['B', "B", "B", "B"],
    ["B", "B", "W", "B"],
    ['W', "W", "B", "B"],
    ['B', "B", "B", "W"]
]))
