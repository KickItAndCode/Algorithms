# 416. Partition Equal Subset Sum
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.


# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].


# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

def canPartition(nums):

    # if this number is not a multiple of two they can't be split
    total = sum(nums)
    if total % 2 != 0:
        return False

    return canPartitionHelper(nums, 0, 0, total, {})


def canPartitionHelper(nums, i, curr_sum, total, cache):
    # current state
    current = str(i) + str(curr_sum)
    # check cache
    if current in cache:
        return cache[current]
    # base case truthy
    if curr_sum * 2 == total:
        return True
    # base case falsy
    if curr_sum > total // 2 or i >= len(nums):
        return False
    # recursion.. take or don't take a number
    found = canPartitionHelper(nums, i + 1, curr_sum, total,
                               cache) or canPartitionHelper(nums, i + 1, curr_sum + nums[i], total, cache)

    # store value in cache
    cache[current] = found

    return found


print(canPartition([1, 5, 11, 5]))
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

print(canPartition([1, 2, 3, 5]))
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
