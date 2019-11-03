# 349. Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
# Example 2:

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.


# with a set([1,2,4]) you can find the intersection with another set using the & operrator

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums2) & set(nums1))


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def findIntersection(set1, set2):
        return [x for x in set1 if x in set2]

    num1Set = set(num1)
    num2Set = set(num2)

    if len(num2Set) > len(num1Set):
        return findIntersection(set1, set2)
    else:
        return findIntersection(set2, set1)
