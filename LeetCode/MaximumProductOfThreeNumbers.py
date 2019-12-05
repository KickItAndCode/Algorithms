# 628. Maximum Product of Three Numbers

# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:

# Input: [1, 2, 3]
# Output: 6


# Example 2:

# Input: [1, 2, 3, 4]
# Output: 24


# Note:

# The length of the given array will be in range[3, 104] and all elements are in the range[-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


# this solution handles negative numbers by looking at the lowest two numbers as well as the high positive numbers

# -1000 -1000 1 2 8
# the solutionneeds to handle this as using the negative numbers if there are two of them as
# the correct solution

# sort the numbers
# take the max of the bottom two negatives and top positive compared with the
# product of the top three positives

def maximumProduct(nums):
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3])


print(maximumProduct([1, 2, 3]))  # 6
print(maximumProduct([-10, 2, -15,  3]))  # 450
print(maximumProduct([5, 2, -15,  3]))  # 30
