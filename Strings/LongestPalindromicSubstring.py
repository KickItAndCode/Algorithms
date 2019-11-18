# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


def longestPalindrome(s):
    currLong = [0, 1]

    for i in range(1, len(s)):
        # odd case where you check around the val at i then expand
        odd = getLongestPalindromeFrom(s, i-1, i + 1)
        # even case where you split between current val and the previous then expand
        even = getLongestPalindromeFrom(s, i - 1, i)

        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currLong = max(longest, currLong, key=lambda x: x[1] - x[0])
    return s[currLong[0]:  currLong[1]]


def getLongestPalindromeFrom(s, left, right):
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break

        left -= 1
        right += 1

    return[left + 1, right]


print(longestPalindrome("babad"))  # "bab"
print(longestPalindrome("cbbd"))  # "bb"
print(longestPalindrome("abaxyzzyxf"))  # "bb"


def longestPalindrome2(s):
    res = ""
    for i in range(len(s)):
        odd = palindromeAt(s, i, i)
        even = palindromeAt(s, i, i+1)

        res = max(res, odd, even, key=len)
    return res

# starting at l,r expand outwards to find the biggest palindrome


def palindromeAt(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]
