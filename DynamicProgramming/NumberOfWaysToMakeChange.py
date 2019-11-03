# 10 [ 1,5, 10, 25]

# 0 0 0 0 0 0 0 0 0 0
# 1 2 3 4 5 6 7 8 9 10


def numberOfWaysToMakeChange(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1

    for c in coins:
        for amount in range(1, target + 1):
            if c <= amount:
                dp[amount] += dp[amount-c]

    return dp[-1]


print(numberOfWaysToMakeChange(10, [1, 5, 10, 25]))
