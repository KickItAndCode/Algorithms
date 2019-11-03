# 276. Paint Fence

# There is a fence with n posts, each post can be painted with one of
# the k colors.

# You have to paint all the posts such that no more than two adjacent
# fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.

# Painting Fence Algorithm

# Given a fence with n posts and k colors, find out the number of
# ways of painting the fence such that at most 2 adjacent posts have
#  the same color. Since answer can be large return it modulo 10 ^ 9 + 7.

# Examples:

# Input: n = 2 k = 4
# Output: 16
# We have 4 colors and 2 posts.
# Ways when both posts have same color: 4
# Ways when both posts have diff color:
# 4*(choices for 1st post) * 3(choices for
#                              2nd post) = 12

# Input: n = 3 k = 2
# Output: 6


# Same no of ways when color of last two post is same
# diff  no of ways when color of last two post is different

def countWays(n, k):
    dp = [0 for x in range(n+1)]

    dp[1] = k
    same, diff = 0, k
    for i in range(2, n + 1):
        same = diff
        diff = dp[i-1] * (k-1)
        dp[i] = (same + diff)
    return dp[n]


print(countWays(3, 2))
print(countWays(2, 4))
print(countWays(5, 2))
