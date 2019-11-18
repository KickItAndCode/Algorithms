# 45. Jump Game II
# Hard
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.


#  Time O (N^2)  | Space O (N)
def jump1(nums):
    # store in dp the min number of jumps needed to from 0 to i
    dp = [float('inf')] * len(nums)
    dp[0] = 0

    for i in range(len(nums)):
        curr = 0
        for j in range(i):
            # can we go from j to i
            if nums[j] + j >= i:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

# Time O(N) | Space O (1)


def jump(nums):

    jumps, steps, max_reach = 0, nums[0], nums[0]

    if len(nums) == 1:
        return 0

    for i in range(1, len(nums)-1):
        max_reach = max(max_reach, nums[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps + 1


print(jump([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
