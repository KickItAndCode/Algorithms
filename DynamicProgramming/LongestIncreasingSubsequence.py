# 300. Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest
#  increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101],
#  therefore the length is 4.
# Note:

# There may be more than one LIS combination, it is only necessary
#  for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


def lengthOfLIS(nums):

    if not nums:
        return 0

    # initialize at 1's at min each spot would be 1
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):

            # if true we can extend the LIS at i
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(lengthOfLIS([-1, 3, 4, 5, 2, 2, 2, 2]))
