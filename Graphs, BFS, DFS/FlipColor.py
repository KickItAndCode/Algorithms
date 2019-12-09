# BSS flip colors one level at a time


def flipColor(x, y, image):
    color = image[x][y]
    queue = [x, y]
    image[x][y] = not image[x][y]  # flip

    while queue:
        x, y = queue.pop(0)
        for nextX, nextY in ((x + y+1), (x, y-1), (x + 1, y), (x-1, y)):
            if (0 <= nextX < len(image) and 0 <= nextY < len(image[nextY]) and image[nextX][nextY] == color):

                # flip color
            image[nextX][nextY] = not image[nextX][nextY]
            queue.append((nextX, nextY))

# DFS recursive


def flipColor(x, y, image):
    color = image[x][y]
    image[x][y] = not image[x][y]  # flips

    for nextX, nextY in ((x + y+1), (x, y-1), (x + 1, y), (x-1, y)):
        if (0 <= nextX < len(image) and 0 <= nextY < len(image[nextY]) and image[nextX][nextY] == color):

            flipColor(nextX, nextY, image)
