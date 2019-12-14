# 16. 3Sum Closest

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1=2).


def threeSumClosest(nums, target):
    nums.sort()
    res, diff = 0, float("inf")

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            holdDifference = abs(s-target)

            # 0 case
            if not holdDifference:
                return s

                # if this current difference is better than the best diff so far update it
            if holdDifference < diff:
                res = s
                diff = holdDifference

            if s < target:
                l += 1
            elif s > target:
                r -= 1

    return res


print(threeSumClosest([-1, 2, 1, -4], 1))  # 2 (-1, 2,1)
