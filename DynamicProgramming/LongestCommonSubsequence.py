# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some
# characters(can be none) deleted without changing the relative order of the remaining
#  characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common
#  subsequence of two strings is a subsequence that is common to both strings.


def longestCommonSubsequence(str1, str2):
    dp = [[None] * (len(str2) + 1) for i in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i - 1][j-1] + 1  # diagonal
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


print(longestCommonSubsequence("abcde", "ace"))  # 3 ace
print(longestCommonSubsequence("abc", "abc"))  # 3 abc
print(longestCommonSubsequence("abc", "def"))  # 0
print(longestCommonSubsequence("AGGTAB", "GXTXAYB"))  # 3 XYZW
