# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# return an array with the max sum and the array of values to get the sum


def maxSubIncreasingSubSequence(nums):
    dp = [None for x in nums]
    sums = nums[:]
    maxSumIdx = 0
    for i in range(len(nums)):
        currNum = nums[i]
        for j in range(0, i):
            otherNum = nums[j]
            if otherNum < currNum and (sums[j] + currNum) >= sums[i]:
                sums[i] = sums[j] + currNum
                dp[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(nums, dp, maxSumIdx)]


def buildSequence(nums, dp, currIdx):
    res = []
    while currIdx is not None:
        res.append(nums[currIdx])
        currIdx = dp[currIdx]
    return list(reversed(res))


print(maxSubIncreasingSubSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 7
print(maxSubIncreasingSubSequence([10, 9, 2, 5, 3, 7, 101, 18]))  # 115
