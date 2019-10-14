# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more
# subtle.

from nose.tools import assert_equal


def maxSubArray(nums):
    currSum, maxSum = 0, float('-inf')

    for i in range(len(nums)):
        currVal = nums[i]
        currSum = max(currVal, currVal + currSum)
        maxSum = max(currSum, maxSum)
    return maxSum


class MaxSubArrayTest (object):

    def test(self, sol):
        assert_equal(sol([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        print("ALL TEST CASES PASSED")


# Run and test
t = MaxSubArrayTest()
t.test(maxSubArray)
