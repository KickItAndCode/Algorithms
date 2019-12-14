# 713. Subarray Product Less Than K

# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:

# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.


# 2, 5, 6, 10
# l         r


# Two pointer O(n) time O(1) space:
# Initialize a left index j = 0 and a right index i = 0.
# As we iterate i over range(len(nums)), we keep updating res, the cumulative product of all entries from j to i.
#  As soon as res >= k, we move the left index to the right until res < k. The length i - j + 1 is then the number of subarrays ending with i where the product of all elements in the subarray is less than k.


def numSubarrayProductLessThanK(nums, k):

    if len(nums) == 0 or k <= 1:
        return 0

    start, end, prod, res = 0, 0, 1, 0

    while end < len(nums):
        # keep track of the product so far in the window
        prod *= nums[end]
        end += 1

        # if the prod is too great we move the left index to the right until its not
        while prod >= k:
            prod /= nums[start]
            start += 1

        # Add the index diff to res
        res += end - start
    return res


def numSubarrayProductLessThanK2(nums, k):
    if not nums:
        return 0

    end, prod, res = 0, 1, 0

    # loop through all nums
    for i in range(len(nums)):
        # keep track of the product so far in the window
        prod *= nums[i]
        # if the window is two great
        if prod >= k:
            # if the prod is too great we move the left index to the right until its not
            while prod >= k and end <= i:
                prod /= nums[end]
                end += 1

        res += i - end + 1

    return res


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # 8
