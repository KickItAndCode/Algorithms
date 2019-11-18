# 647. Palindromic Substrings
# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".


# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# A DP solution to this problem is to build a table with all possible string[start:end] combinations, storing which are palindromes and which are not (True or False). At any given moment, when you're checking if string[i:j] is a palindrome, you only need to know two things:

# Is string[i] equal to string[j]?
# Is string[i+1:j-1] a palindrome?
# For condition (1), a simple check might do, for condition (2), you use the table. If both conditions are met, mark table[i][j] as True and increase your count.

def countSubstrings(s: str) -> int:
    dp = [[False] * len(s) for x in range(len(s))]
    count = 0
    for i in range(len(s)-1, -1, -1):
        dp[i][i] = True
        count += 1
        for j in range(i+1, len(s)):
            if j == i+1 and s[i] == s[j]:
                dp[i][j] = True
                count += 1
            if j > i+1 and dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                count += 1
    return count


def countSubstrings2(s):

    res = 0
    dp = [[True] * len(s) for x in range(len(s))]

    # each character is a palindrome by default
    for i in range(len(s)):
        res += 1
        dp[i][i] = True

    for j in range(1, len(s)):
        for i in range(0, j):

            # if left and right char are equal and inner letter are less or equal to 2
            if s[i] == s[j] and j-i <= 2:
                dp[i][j] = True
                res += 1
            # condition where outer chars are equal and inner word length is greater than 1
            elif s[i] == s[j] and j-i > 2:
                if dp[i+1][j-1]:
                    res += 1
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = dp[i + 1][j-1]
            else:
                dp[i][j] = False
    return res


# Problem
# Number of palindromic substrings s[0..len-1]

# State
# state[i][j] is true if substring s[i, j] is palindromic

# Aim State
# decide all possible state[i][j] and count the element that is true

# State Transition
# state[i][j] is true if s[i] == s[j] and state[i+1][j-1] is true (j - i >= 2)
# state[i][j] is true if s[i] == s[j] (j - i == 1)
# state[i][j] is true (j - i == 0)
# i is decreasing, dist = j - i is increasing


def countSubstrings3(s):

    res = 0
    dp = [[None] * len(s) for x in range(len(s))]

    # each character is a palindrome by default
    for i in range(len(s)):
        res += 1
        dp[i][i] = True

    for i in range(len(s) - 1, -1 - 1):
        for dist in range(1, len(s) - 1):
            j = i + dist

            if dist == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = dp[i + 1][j-1] and (s[i] == s[j])

    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i][j]:
                res += 1

    return res


print(countSubstrings("abc"))  # 3
print(countSubstrings("aaa"))  # 6
