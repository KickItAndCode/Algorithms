# 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n(n=size
# of array), some elements appear twice and others
# appear once.

# Find all the elements of[1, n] inclusive that do
# not appear in this array.

# Could you do it without extra space and in O(n)
# runtime? You may assume the returned list does
#  not count as extra space.

# Example:

# Input:
# [4, 3, 2, 7, 8, 2, 3, 1]

# Output:
# [5, 6]

from nose.tools import assert_equal
# 1 2 3 4 7 8
# i j


# Take the difference of two sets and the resulting list is the answer
def findDisappearedNumbers(self, nums):
    l = set(sorted(nums))
    u = range(1, len(nums)+1)
    if len(l) > 0:
        return list(set(u) - l)
    else:
        return []


class FindDisappearedNumbersTest (object):
    def test(self, sol):
        assert_equal(sol([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
        print("ALL TEST CASES PASSED")


# Run and test
t = FindDisappearedNumbersTest()
t.test(findDisappearedNumbers)
