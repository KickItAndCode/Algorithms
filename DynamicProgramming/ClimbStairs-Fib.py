# 70. Climbing Stairs
# You are climbing a stair case. It takes n steps to reach
# to the top.

# Each time you can either climb 1 or 2 steps. In how many
#  distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(self, n: int) -> int:
    a, b = 1, 1
    for nums in range(n):
        a, b = b, b + a
    return a


def climbStairs(self, n: int) -> int:
    steps = [1, 1]
    for i in range(2, n+1):
        steps.append(steps[i-1] + steps[i-2])
    return steps[n]


def climbStairsDP(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


def climbStairsRec(n):
    if n == 0:
        return 0
    if n <= 2:
        return n

    return climbStairsRec(n-1) + climbStairsRec(n-2)


def climbStairs(self, n: int) -> int:
    memo = [0] * n
    return self.helper(0, n, memo)

    def helper(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]

        memo[i] = self.helper(i + 1, n, memo) + self.helper(i+2, n, memo)
        return memo[i]


print(climbStairsRec(3))
print(climbStairsDP(3))
