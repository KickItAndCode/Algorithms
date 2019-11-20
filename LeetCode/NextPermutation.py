# 31. Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


def nextPermutation(nums):
    i = j = len(nums) - 1

    # find the right most pair where nums[i] > nums[i-1]
    while i > 0 and nums[i] <= nums[i-1]:
        i -= 1

    if i > 0:
        # find the first value at j where its less than your current value then swap
        while nums[j] <= nums[i-1]:
            j -= 1
        # exchange nums[i-1] and the right most element which larger than nums[i-1]
        nums[i-1], nums[j] = nums[j], nums[i-1]  # swap

    # reverse everything else
    # also handles the case where everything is in decensing order because I will be at 0
    nums[i:] = reversed(nums[i:])
    print(nums)


print(nextPermutation([1, 2, 3]))  # 1 3 2
print(nextPermutation([3, 2, 1]))  # 1 2 3
print(nextPermutation([1, 1, 5]))  # 1 5 1
