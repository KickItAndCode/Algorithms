# maximum subset sums with no adjacent elements

# Write a function that takes in an array of positive integers
# representing the max sum of non adjacent elements in the array.
# If the sum cannot be generated, the fucntion should return 0

# [75, 105, 120, 75, 90, 135]
# 330 [75, 120, 135]


def maxSubsetSumNoAdjacent(nums):

    if not len(nums):
        return

    elif len(nums) == 1
    return nums[0]

    dp = [0] * (len(nums))
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]


print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
# Answer 330 [75, 120, 135]
