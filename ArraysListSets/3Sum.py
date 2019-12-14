
# 15. 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# # there's only going to be 3 numbers. So to find the combinations of 3 numbers, he is iterating through the list with the first pointer, and then trying to find two extra numbers to sum to 0. Since the list is ordered, the right pointer will always be higher than the middle pointer. So if the sum is too large, you can move the right pointer back one. On the other hand, if the sum is too small (below 0), then move the middle pointer up one.


def threeSum(nums):
    if not nums:
        return []
    nums.sort()
    res = []

    for i in range(len(nums)-2):
        # duplicate number check
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i + 1, len(nums)-1

        while l < r:
            summ = nums[i] + nums[l] + nums[r]
            if summ < 0:
                l += 1
            elif summ > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1

                l += 1
                r -= 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
