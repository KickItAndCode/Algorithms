# 674. Longest Continuous Increasing Subsequence

# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.


def findLengthOfLCIS2(nums):

    if not nums:
        return 0

    length, maxLength, i = 1, 1, 0
    while i < len(nums):

        # compare with the num next to it
        while i + 1 < len(nums) and nums[i] < nums[i + 1]:
            length += 1
            i += 1

        # update max
        maxLength = max(maxLength, length)
        # Reset length
        length = 1
        # increment to continue traversing
        i += 1
    return maxLength


def findLengthOfLCIS(nums):
    ans = wall = 0
    for i in range(len(nums)):
        if i and nums[i-1] >= nums[i]:
            wall = i
        ans = max(ans, i - wall + 1)
    return ans


def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    res = 1
    c = 1
    for i in range(1, len(nums)):
        c = c + 1 if nums[i] > nums[i-1] else 1
        res = max(res, c)
    return res


print(findLengthOfLCIS2([1, 3, 5, 4, 2, 3, 4, 5]))  # 4
print(findLengthOfLCIS2([1, 3, 5, 4, 7]))  # 3
print(findLengthOfLCIS2([2, 2, 2, 2, 2]))  # 1
