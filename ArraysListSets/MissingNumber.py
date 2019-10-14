# 268. Missing Number
# Given an array containing n distinct numbers 
# taken from 0, 1, 2, ..., n, find the one that is 
# missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2
# Example 2:

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant extra space complexity?

# O(logN ) | O(n)
def missingNumber(nums):
    nums.sort()
    rangeSet = set(range(len(nums)+ 1))
    numsSet = set(nums)
    res = rangeSet - numsSet
    return  res.pop()
    

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal
import collections

class TestFinder(object):

    def test(self,sol):
        assert_equal(sol([3,0,1]),2)
        assert_equal(sol([9,6,4,2,3,5,7,0,1]),8)
        print ('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(missingNumber)
