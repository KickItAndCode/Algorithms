# 560. Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:

# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


# solution Cummulative Sum
# create a cumulative sum array, then to calculate the sum of elements between indices you can
# substract the cumulative sum corresponding to the two indices to obtain the sum directly
# instead of iterating over the subarray to obtain the sum

#


from collections import defaultdict

# Time O (n^2) | Space O (1)


def subarraySum3(nums, k):
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                count += 1
    return count

# Time O (N) |  Space O (N)


def subarraySum2(nums, k):
    map = defaultdict(int)
    sum, res = 0, 0
    map[0] = 1
    for i in range(len(nums)):
        sum += nums[i]
        target = sum - k
        if target in map:
            res += map[target]

        map[sum] += 1
    return res


print(subarraySum3([1, 1, 1], 2))  # 2
print(subarraySum3([1, 1, 1, 1, 1], 2))  # 3
