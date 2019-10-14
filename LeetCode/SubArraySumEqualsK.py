# 560. Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
# Note:
# The length of the array is in range[1, 20, 000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

from nose.tools import assert_equal


def subarraySum(nums, k):


class SubarraySumTest(object):

    def test(self, solution):

        assert_equal(solution([1, 1, 1], 2), 2)

        print('All test cases passed.')


# Run Tests
t = SubarraySumTest()
t.test(subarraySum)
