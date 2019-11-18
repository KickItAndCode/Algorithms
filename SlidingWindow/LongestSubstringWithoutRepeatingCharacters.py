# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
from collections import defaultdict


def lengthOfLongestSubstring(s):
    leftWall, j = 0, 0

    res = 0
    while leftWall < len(s):
        map = defaultdict(int)
        while j < len(s):
            if s[j] not in map:
                map[s[j]] = 1
                j += 1
            else:
                break

        res = max(j - leftWall, res)
        leftWall += 1
        j = leftWall
    return res


# his solution uses a "sliding window" hash set. Let me know if you have any questions!

# Detailed explanation:

# left and right are indexes into the string. These bound the current substring we're looking at. We also have a hash set, chars, which stores the characters in the current substring.

# Both indices start at 0. We check if string[right] is in our hash set of current characters; if it isn't, it's a unique character we can add to the current substring. So, we add it to the set of characters, and increment right. We also potentially update longest with the length of the current substring.

# If string[right] is in the hash set of characters, we remove string[left] from the hash set, and increment left. This is because the character at right is a duplicate of some character in the substring; we want to keep removing the leftmost character from the current substring until we remove that character. Then, since we have another candidate for longest non-repeating substring, we can enter the if block, and go back to incrementing right.

# By the time the while loop terminates, we've considered every substring with unique characters, and we know the length of the longest. left and right were incremented linearly through the string, and the hash set allowed for O(1) lookups, so the time complexity is O(n).

# Time O (N) | Space O(N)
def lengthOfLongestSubstring2(s):
    hashSet = set()
    res, i, j = 0, 0, 0
    while i < len(s) and j < len(s):
        if s[j] not in hashSet:
            hashSet.add(s[j])
            j += 1
            res = max(res, j-i)
        else:
            hashSet.remove(s[i])
            i += 1
    return res


print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring2("abcabcbb"))  # 3
print(lengthOfLongestSubstring2("bbbbb"))  # 1
print(lengthOfLongestSubstring2("pwwkew"))  # 3
