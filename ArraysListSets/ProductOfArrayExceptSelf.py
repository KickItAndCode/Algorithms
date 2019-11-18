# 238. Product of Array Except Self
# Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


def productExceptSelf(nums):
    length = len(nums)
    res = [0] * length

    res[0] = 1

    # res[i] containers the product of all the elements to the left
    for i in range(1, length):
        res[i] = nums[i-1] * res[i-1]

    # prod containers the product of all the elements to the right
    prod = 1
    for i in reversed(range(length)):
        # for the index 'i' prod would contain the product of all elements to the right. We update prod accordingly
        res[i] = res[i] * prod
        prod *= nums[i]
    return res
# Scan Forward and the Scan backward


def productExceptSelf3(nums):

    output = [1]*len(nums)
    n = len(nums)

    prod = 1
    for i in range(1, n):
        prod = prod*nums[i-1]
        output[i] *= prod

    prod = 1
    for i in range(n-2, -1, -1):
        prod = prod*nums[i+1]
        output[i] *= prod

    return output


def productExceptSelf2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * len(nums)
    for i in range(len(nums)):
        before = nums[:i]
        after = nums[i+1:]
        together = before + after

        for j in range(len(together)):
            res[i] *= together[j]
    return res


print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8 6]
