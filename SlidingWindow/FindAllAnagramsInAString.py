# 438. Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
from collections import Counter


def findAnagrams(s, p):
    start, map, res = 0, Counter(p), []

    if len(p) > len(s):
        return res

    # keeps track of fully visited chars
    count = len(map)

    # starting loop
    for end in range(len(s)):
        curr = s[end]

        # handle condition
        # s in t map decrement counter
        if curr in map:
            map[curr] -= 1
            # fully visited
            if map[curr] == 0:
                count -= 1

        # invalid cases to move the start of the window up
        while count == 0:
            curr = s[start]
            if curr in map:
                map[curr] += 1
                if map[curr] > 0:
                    count += 1

            # update res
            if end - start + 1 == len(p):
                res.append(start)

            start += 1

    return res


def findAnagrams2(s, p):
    if len(s) < len(p) or not s or not p:
        return []

    need = collections.Counter(p)
    res = []
    l, r, missing = 0, 0, len(p)

    while r < len(s):
        if need[s[r]] > 0:
            missing -= 1
        need[s[r]] -= 1

        if missing == 0:
            res.append(l)

        if r - l == len(p)-1:
            need[s[l]] += 1
            if need[s[l]] > 0:
                missing += 1
            l += 1

        r += 1

    return res


print(findAnagrams("cbaebabacd", "abc"))  # [0,6]
print(findAnagrams("abab", "ab"))  # [0,1,2]
