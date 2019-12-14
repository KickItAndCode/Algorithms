
# As an initial example, pretend we have 5 dice with 6 faces each and we want to determine how many ways to make 18.
# In other words, what is dp(5, 6, 18)?

# At first glance, this is seems difficult and overwhelming. But if we make one simple observation, we can reduce this big problem into several smaller sub-problems. We have 5 dice, but let's first just look at ONE of these dice(say the last one). This die can take on f different values(1, ..., f), so we can consider what happens when we fix its value to any of these possibilities. In this case, f = 6.

# Case 1: The last die is a 1. The remaining 4 dice must sum to 18-1 = 17. This can happen dp(4, 6, 17) ways.
# Case 2: The last die is a 2. The remaining 4 dice must sum to 18-2 = 16. This can happen dp(4, 6, 16) ways.
# Case 3: The last die is a 3. The remaining 4 dice must sum to 18-3 = 15. This can happen dp(4, 6, 15) ways.
# Case 4: The last die is a 4. The remaining 4 dice must sum to 18-4 = 14. This can happen dp(4, 6, 14) ways.
# Case 5: The last die is a 5. The remaining 4 dice must sum to 18-5 = 13. This can happen dp(4, 6, 13) ways.
# Case 6: The last die is a 6. The remaining 4 dice must sum to 18-6 = 12. This can happen dp(4, 6, 12) ways.

# dp(5, 6, 18) = dp(4, 6, 17) + dp(4, 6, 16) + dp(4, 6, 15) + dp(4, 6, 14) + dp(4, 6, 13) + dp(4, 6, 12)

# We sum up the solutions for each of these 6 cases to arrive at our result. Of course, each of these cases branches off into 6 cases of its own, and the recursion only resolves when d = 0. The handling of this base case is explained below.


# The general relation is:
# dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)

# The base case occurs when d = 0. We can make target = 0 with 0 dice, but nothing else.
# So dp(0, f, t) = 0 iff t != 0, and dp(0, f, 0) = 1.

# Use memoization to avoid repeated calculations and don't conisider negative targets.

# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355940/C%2B%2B-Coin-Change-2

def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    memo = {}

    def dp(d, target):
        if d == 0:
            return 0 if target > 0 else 1
        if (d, target) in memo:
            return memo[(d, target)]
        to_return = 0
        for k in range(max(0, target-f), target):
            to_return += dp(d-1, k)
        memo[(d, target)] = to_return
        return to_return
    return dp(d, target) % (10**9 + 7)


def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
    dp[0][0] = 1
    mod = 10 ** 9 + 7
    for i in range(1, d + 1):
        for j in range(1, target + 1):
            k = 1
            while k <= min(j, f):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % mod
                k += 1
    return dp[d][target] % mod
