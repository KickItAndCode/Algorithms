from nose.tools import assert_equal
# 169. Majority Element

# Given an array of size n, find the majority element.
# The majority element is the element that appears more
# than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the
#  majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2


def majorityElement(nums):
    map = {}

    for n in nums:
        if n in map:
            map[n] += 1
        else:
            map[n] = 1
    currMax = (float('-inf'), 0)

    for k, v in map.items():
        if v > currMax[1]:
            currMax = (k, v)
    return currMax[0]


class MajorityElementTest(object):

    def test(self, sol):
        assert_equal(sol([3, 2, 3]), 3)
        assert_equal(sol([2, 2, 1, 1, 1, 2, 2]), 2)
        print("ALL TEST CASES PASSED")


# Run and test
t = MajorityElementTest()
t.test(majorityElement)
