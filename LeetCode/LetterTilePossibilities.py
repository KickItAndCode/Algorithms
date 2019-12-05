# 1079. Letter Tile Possibilities
# You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.


# Example 1:

# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: "AAABBC"
# Output: 188


# Note:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

# def numTilePossibilities(tiles):
#     if not tiles:
#         return 0

#     res = []
#     helper(tiles, "", res)
#     return len(res)


# def helper(tiles,  path, res):

#     for j, char in enumerate(tiles):
#         helper(tiles[j + 1:], path + tiles[j], res)
#     res.append(path)


def numTilePossibilities(tiles):
    res = set()
    for i in range(1, len(tiles) + 1):
        helper(tiles, "", i, res)
    return len(res)


def helper(tiles, curr, k, res):
     # return so that the loop below doesn't continue when you meet the length requirement
    if k == len(curr):
        res.add(curr)
        return

    # start at size 1 and move until size len(tiles), +1 because range doesn't include the endpoint

    for i in range(len(tiles)):
        # call helper with everything but the current value
        helper(tiles[:i] + tiles[i+1:], curr + tiles[i], k, res)


def numTilePossibilities3(tiles):
    res = {''}
    for c in tiles:
        res |= {d[:i] + c + d[i:] for d in res for i in range(len(d) + 1)}
    return len(res) - 1


print(numTilePossibilities("AAB"))
print(numTilePossibilities("AAABBC"))
