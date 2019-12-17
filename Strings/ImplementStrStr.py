# 28. Implement strStr()
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Accepted


def strStr(haystack, needle):

    if len(needle) > len(haystack):
        return -1

    start = 0

    for end in range(len(haystack)):
        if haystack[end] == needle[0]:
            # expand
            allMatch = True
            start = end
            for i in range(len(needle)):
                if haystack[end] != needle[i]:
                    allMatch = False
                    break
                end += 1
            if allMatch:
                return start

    return -1


def strStr(haystack, needle):
    L, n = len(needle), len(haystack)

    for start in range(n - L + 1):
        if haystack[start: start + L] == needle:
            return start
    return -1


def strStr(self, haystack: str, needle: str) -> int:
    L, n = len(needle), len(haystack)
    if L == 0:
        return 0

    pn = 0
    while pn < n - L + 1:
        # find the position of the first needle character
        # in the haystack string
        while pn < n - L + 1 and haystack[pn] != needle[0]:
            pn += 1

        # compute the max match string
        curr_len = pL = 0
        while pL < L and pn < n and haystack[pn] == needle[pL]:
            pn += 1
            pL += 1
            curr_len += 1

        # if the whole needle string is found,
        # return its start position
        if curr_len == L:
            return pn - L

        # otherwise, backtrack
        pn = pn - curr_len + 1

    return -1


print(strStr("Leetcode", "code"))
