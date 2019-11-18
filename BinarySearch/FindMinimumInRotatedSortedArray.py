# 153. Find Minimum in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0, 1, 2, 4, 5, 6, 7] might become[4, 5, 6, 7, 0, 1, 2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3, 4, 5, 1, 2]
# Output: 1
# Example 2:

# Input: [4, 5, 6, 7, 0, 1, 2]
# Output: 0


def findMin(nums):
    l, r = 0, len(nums) - 1
    while nums[l] > nums[r]:
        mid = (l + r) // 2

        # search left
        if nums[mid] < nums[r]:
            r = mid
        # search right
        else:
            l = mid + 1
    return nums[l]


print(findMin([3, 4, 5, 1, 2]))  # 1
print(findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
