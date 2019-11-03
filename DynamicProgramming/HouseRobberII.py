# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.


1 3 2 1 = 4

2 3 1 = 3

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Notice that the first house and the last house can not be both robbed,
#  so we have rob(nums) = max(rob(nums[1:], nums[:-1]). Since there are
# no circles in both nums[1:] and nums[:-1], we can simply apply the answers
# from House Rob


def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    return max([helper(nums[:-1]), helper(nums[1:])])
# or
    # return max([helper(nums[:len(nums)-1]), helper(nums[1:])])


def helper(nums):

    if len(nums) <= 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[len(nums) - 1]


# def rob(nums):

#     left = left_left = 0
#     for i in range(len(nums)):
#         left, left_left = max(nums[i] + left_left, left), left
#     return left


print(rob([1, 2, 3, 1]))    # 4
print(rob([2, 3, 2]))  # 3
