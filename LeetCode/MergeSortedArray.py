# 88. Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]


def merge(nums1, m, nums2, n):

    i, j, = m - 1, n - 1
    rightWall = len(nums1) - 1
    while j >= 0 and i >= 0:

        num1 = nums1[i]
        num2 = nums2[j]
        if num1 > num2:
            nums1[rightWall] = num1
            i -= 1
        elif num1 <= num2:
            nums1[rightWall] = num2
            j -= 1
        rightWall -= 1

    if i < 0:
        nums1[:j+1] = nums2[:j + 1]

    return nums1


# print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))  # [1,2,2,3,5,6]
print(merge([2, 0], 1, [1], 1))  # [1,2]
