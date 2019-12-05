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

# return array of the subsequence


def buildSequence(nums, dp, currIdx):
    res = []
    while currIdx is not None:
        res.append(nums[currIdx])
        currIdx = dp[currIdx]
    return list(reversed(res))


def lengthOfLIS2(nums):
    sequeneces = [None] * len(nums)
    lengths = [1] * len(nums)
    maxLengthIdx = 0

    for i in range(len(nums)):
        currNum = nums[i]
        for j in range(i):
            otherNum = nums[j]
            if otherNum < currNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequeneces[i] = j
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i

    return buildSequence(nums, sequeneces, maxLengthIdx)


# print(lengthOfLIS([16, 3, 5, 19, 10, 14, 12, 0, 15]))
# print(lengthOfLIS([-1, 3, 4, 5, 2, 2, 2, 2]))
# print(lengthOfLIS([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))  # 6
print(lengthOfLIS2([16, 3, 5, 19, 10, 14, 12, 0, 15]))
print(lengthOfLIS2([-1, 3, 4, 5, 2, 2, 2, 2]))
print(lengthOfLIS2([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))  # 6
