# 340. Longest Substring with At Most K Distinct Characters
# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

from collections import defaultdict


# using a dynamic sliding window that expands and contracts
# update a min length to return each iteration

def lengthOfLongestSubstringKDistinct(s, k):
    l, r, length, map = 0, 0, 0, defaultdict(int)

    for r in range(len(s)):
        # always put the new value in the map. Expand
        map[s[r]] += 1

        # contract
        while len(map) > k:

            map[s[l]] -= 1
            # if when we contract and remove values if the mapping value is 0 remove it
            if map[s[l]] == 0:
                del map[s[l]]
            l += 1

        length = max(length, r-l + 1)
    return length


print(lengthOfLongestSubstringKDistinct("eceba", 2))  # 3
print(lengthOfLongestSubstringKDistinct("aa", 1))  # 2
