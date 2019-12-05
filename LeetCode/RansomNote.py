# 383. Ransom Note
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

from collections import Counter


def canConstruct(ransomNote, magazine):
    map = Counter(magazine)

    for c in ransomNote:
        if c not in map or map[c] <= 0:
            return False

        map[c] -= 1
    return True


print(canConstruct("a", "b"))  # false
print(canConstruct("aa", "ab"))  # false
print(canConstruct("aa", "aab"))  # true
