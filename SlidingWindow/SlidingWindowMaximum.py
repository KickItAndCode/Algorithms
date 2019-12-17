# 239. Sliding Window Maximum
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

# Algorithm

# The algorithm is quite straigthforward :

# Process the first k elements separately to initiate the deque.

# Iterate over the array. At each step :

# Clean the deque :

# Keep only the indexes of elements from the current sliding window.

# Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.

# Append the current element to the deque.

# Append deque[0] to the output.

# Return the output array.

# Time complexity : O(N), since each element is processed exactly twice - it's index added and then removed from the deque.

# Space complexity :O(N), for an output array and for a deque.


def maxSlidingWindow(nums, k):
    if not nums:
        return

    if k > len(nums):
        return

    window, res = [], []

    # find out max for first window
    for i in range(k):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    res.append(nums[window[0]])

    for i in range(k, len(nums)):
        # remove all numbers that are smaller than current number from the tail of list
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # remove first number if it doesn't fall in the window
        if window and (window[0] <= i - k):
            window.pop(0)

        window.append(i)
        res.append(nums[window[0]])

    return res


def maxSlidingWindow2(nums, k):
    ans = []
    queue = []
    for i, v in enumerate(nums):
        if queue and queue[0] <= i - k:
            queue = queue[1:]
        while queue and nums[queue[-1]] < v:
            queue.pop()
        queue.append(i)
        if i + 1 >= k:
            ans.append(nums[queue[0]])
    return ans

# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # 3


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array = " + str(array))

print("Max = " + str(maxSlidingWindow2(array, 3)))

array = [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67]
print("Array = " + str(array))

print("Max = " + str(maxSlidingWindow2(array, 3)))
