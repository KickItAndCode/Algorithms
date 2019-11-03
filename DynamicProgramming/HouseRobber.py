# 198. House Robber

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security system connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money
#  of each house, determine the maximum amount of money you can rob tonight
#  without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and
# rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# [ 0, 0 , 0 ,0]


def rob(nums):

    if len(nums) <= 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[- 1]


# def rob(nums):

#     left = left_left = 0
#     for i in range(len(nums)):
#         left, left_left = max(nums[i] + left_left, left), left
#     return left


# print(rob([1, 2, 3, 1]))
# print(rob([2, 7, 9, 3, 1]))
print(rob([2, 1, 1, 2]))
