# 209. Minimum Size Subarray Sum
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


def minSubArrayLen(s, nums):
    curr_min = float('inf')
    curr = 0
    for i in range(len(nums)):
        curr = 0
        for j in range(i, len(nums)):
            curr += nums[j]
            # if found a fit
            # j - i is the number of elements
            if curr >= s:
                curr_min = min(curr_min, (j-i) + 1)
                break

    return curr_min


def minSubArrayLen(s, nums):
    if not nums:
        return 0

    i, j, curr_min = 0, 0, float('inf')
    total = nums[0]
    while j < len(nums):
        if total < s:
            j += 1
            if j < len(nums):
                total += nums[j]
        else:
            curr_min = min(curr_min, j - i + 1)
            # reduce your total by value of the i as we slide the window
            total -= nums[i]
            i += 1
    return curr_min if curr_min != float('inf') else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2 ([4,3])
