# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
from collections import Counter


def firstUniqChar(s):
    map = Counter(s)

    for i, el in enumerate(s):
        if map[el] == 1:
            return i
    return -1


print(firstUniqChar("leetcode"))
print(firstUniqChar("dad"))
