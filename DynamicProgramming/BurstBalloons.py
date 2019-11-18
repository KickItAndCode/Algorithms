# 312. Burst Balloons
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:

# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


def maxCoins2(iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                                      nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]

# Top Down ~800ms


def maxCoins(nums):
    nums, memo = [1] + nums + [1], {}

    def dp(l, r):
        if l + 1 == r:
            return 0
        if (l, r) not in memo:
            memo[(l, r)] = max(dp(l, i) + nums[l] * nums[i] * nums[r] + dp(i, r)
                               for i in range(l + 1, r))
        return memo[(l, r)]
    return dp(0, len(nums) - 1)

# Button Up ~200ms


def maxCoins(nums):
    nums, N = [1] + nums + [1], len(nums) + 2
    dp = [[0] * N for _ in range(N)]
    for gap in range(2, N):
        for i in range(N - gap):
            j = i + gap
            dp[i][j] = max(dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                           for k in range(i + 1, j))
    return dp[0][N - 1]


# PERSONAL STRUGGLE SOLUTION NO EVEN CLOSE
def maxCoins(nums):
    nums = [1] + nums + [1]  # build the complete array
    n = len(nums)

    # loop through all coins
    dp = [0] * len(nums)

    while nums:
        # find the max you'd get by bursting a certain balloon
        curr_max = float("-inf")
        indexToDelete = -1
        for i in range(len(nums)):
            coins = burst(nums, i)
            if coins > curr_max:
                indexToDelete = i
                curr_max = coins
            dp[i] = coins

        nums = removeBalloon(nums, indexToDelete)

    return sum(dp)


def removeBalloon(nums, i):
    return nums[:i] + nums[i+1:]


def burst(nums, i):
    if i == 0 and len(nums) > 1:
        return nums[i] * nums[i+1]
    elif i == len(nums) - 1:
        return nums[i] * nums[i-1]
    else:
        return nums[i] * nums[i+1] * nums[i-1]


print(maxCoins2([3, 1, 5, 8]))


# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
