from nose.tools import assert_equal


# 283. Move Zeroes
# Given an array nums, write a function to move all 0's to the
# end of it while maintaining the relative order of the non-zero
# elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


# 1 0 0 3 9
#   i j


# def moveZeroes(nums):
#     """
#         Do not return anything, modify nums in-place instead.
#     """

#     for i in range(0, len(nums)):
#         j = i
#         while j <= len(nums) - 1 and nums[j] == 0:
#             j += 1

#         if j <= len(nums) - 1:
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#     return nums

# 0 1 0 3 12
# i
#   k
def moveZeroes(nums):
    """
        Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            j += 1
        else:
            nums[i-j], nums[i] = nums[i], nums[i-j]
    return nums


class MoveZeroesTest(object):

    def test(self, sol):
        assert_equal(sol([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        assert_equal(sol([2, 1, 0, 4, 12]), [2, 1, 4, 12, 0])
        print("ALL TEST CASES PASSED")


# Run and test
t = MoveZeroesTest()
t.test(moveZeroes)
