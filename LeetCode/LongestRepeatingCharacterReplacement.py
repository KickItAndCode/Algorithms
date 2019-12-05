# 424. Longest Repeating Character Replacement

# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

# In one operation, you can choose any character of the string and change it to any other uppercase English character.

# Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.


# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
from string import ascii_uppercase

# The initial step is to extend the window to its limit, that is, the longest we can get to with maximum number of modifications. Until then the variable start will remain at 0.

# Then as end increase, the whole substring from 0 to end will violate the rule, so we need to update start accordingly (slide the window). We move start to the right until the whole string satisfy the constraint again. Then each time we reach such situation, we update our max length.

from collections import defaultdict


def characterReplacement(s, k):

    length = len(s)
    count = defaultdict(int)
    start, maxCount, maxLength = 0, 0, 0

    for i, c in enumerate(s):
        count[c] += 1
        maxCount = max(maxCount, count[c])

        if i - start + 1 - maxCount > k:
            count[s[start]] -= 1
            start += 1

        maxLength = max(maxLength, i - start + 1)

    return maxLength


print(characterReplacement("ABAB", 2))  # 4
print(characterReplacement("AABABBA", 1))  # 4
