# Longest Subarray having sum of elements atmost ‘k’
# Given an array of integers, our goal is to find the length of largest subarray having sum of its elements atmost ‘k’ where k>0.

# Examples:

# Input : arr[] = {1, 2, 1, 0, 1, 1, 0},
#            k = 4
# Output : 5
# Explanation:
#  {1, 2, 1} => sum = 4, length = 3
#  {1, 2, 1, 0}, {2, 1, 0, 1} => sum = 4, length = 4
#  {1, 0, 1, 1, 0} =>5 sum = 3, length = 5


# Approach
# An efficient approach is to use sliding window technique.

# Traverse the array and check if on adding the current element its sum is less than or equal to k.
# If it’s less than k then add it to sum and increase the count.
# Else
# Remove the first element of subarray and decrease the count.
# Again check if on adding the current element its sum is less than or equal to k.
# If it’s less than k then add it to sum and increase the count.
# Keep track of Maximum count.
def longestSubarrayHavingSumAtMostK(nums, k):
    count, maxLength, currSum = 0, 0, 0

    for i in range(len(nums)):

        # adding the current number doesn't break
        if currSum + nums[i] < k:
            currSum += nums[i]
            count += 1

        # Else, remove first element of current
        # window and add the current element
        elif(currSum != 0):
            currSum = currSum - nums[i - count] + nums[i]

        maxLength = max(maxLength, count)

    return maxLength


print(longestSubarrayHavingSumAtMostK([1, 2, 1, 0, 1, 1, 0], 4))  # 5
