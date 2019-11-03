# 91. Decode Ways
# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


def numDecodings(s):

    # create a dp array of the size
    dp = [0 for x in range(len(s) + 1)]

    # base case solving
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    # loop through s
    for i in range(2, len(s) + 1):
        # grab single digit
        oneDigit = int(s[i-1: i])
        # if the single digit is valid then update our dp array with its value from dp array
        if oneDigit >= 1:
            dp[i] += dp[i-1]

        # grab two digits
        twoDigit = int(s[i-2: i])
        # if the two digit is valid then update our dp array with its value from dp array for the last two
        if 10 <= twoDigit <= 26:
            dp[i] += dp[i-2]
    return dp[len(s)]


print(numDecodings("12"))
print(numDecodings("226"))
