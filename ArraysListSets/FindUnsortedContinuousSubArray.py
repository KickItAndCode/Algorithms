# 581. Shortest Unsorted Continuous Subarray
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort[6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range[1, 10, 000].
# The input array may contain duplicates, so ascending order here means <= .


# 2, 6 ,4, 8, 10 , 9, 15
# 2  4  6  8  9    10 15


def findUnsortedSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    sortedNums = sorted(nums)
    l = 0
    r = 0
    for i in range(len(nums)):
        if nums[i] != sortedNums[i]:
            l = i
            break
    for j in range(len(nums)-1, -1, -1):
        if nums[j] != sortedNums[j]:
            r = j
            break
    return r - l+1 if r - l else 0
