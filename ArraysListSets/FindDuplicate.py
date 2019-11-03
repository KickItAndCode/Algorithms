# 287. Find the Duplicate Number

# Given an array nums containing n + 1 integers where each integer is
#  between 1 and n (inclusive), prove that at least one duplicate
# number must exist. Assume that there is only one duplicate number,
# find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it
#  could be repeated more than once.


def findDuplicate(nums):
    nums.sort()

    for i in range(len(nums)):
        if i + 1 <= len(nums) - 1 and nums[i] == nums[i + 1]:
            return nums[i]


def findDuplicate2(nums):
    slow = fast = nums[0]
    # find the intersection points of the two pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # find the entrance to cycle
    p1 = nums[0]
    p2 = fast
    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]
    return p1
# 1, 2, 3, 4, 4


print(findDuplicate2([1, 2, 4, 3, 4, ]))
print(findDuplicate2([3, 1, 3, 4, 2]))
print(findDuplicate2([1, 3, 4, 2, 2]))
