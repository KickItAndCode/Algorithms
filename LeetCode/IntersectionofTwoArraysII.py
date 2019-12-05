# 350. Intersection of Two Arrays II
# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2, 2]
# Example 2:

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]
# Note:

# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
from collections import Counter


def intersect(nums1, nums2):

    nums1 = Counter(nums1)
    nums2 = Counter(nums2)
    res = []
    # nums 1 is larger
    if len(nums1) > len(nums2):
        for k, v in nums1.items():
            if k in nums2.keys():
                while nums1[k] and nums2[k]:
                    nums2[k] -= 1
                    nums1[k] -= 1
                    res.append(k)

    else:
        for k, v in nums2.items():
            if k in nums1.keys():
                while nums1[k] and nums2[k]:
                    nums2[k] -= 1
                    nums1[k] -= 1
                    res.append(k)
    return res


def intersect(nums1, nums2):

    counts = collections.Counter(nums1)
    res = []

    for num in nums2:
        if counts[num] > 0:
            res += num,
            counts[num] -= 1

    return res


print(intersect([1, 2, 2, 1], [2, 2]))  # [2,2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4,9]
