# find the max sum subarray of a fixed sie k


def findMaxSumSubarray(nums, k):

    maxValue = float("-inf")
    currRunningSum = 0

    for i in range(len(nums)):
        # add val for max sum
        currRunningSum += nums[i]

        if i >= k-1:
            maxValue = max(maxValue, currRunningSum)
            # remove value from beginning of window
            currRunningSum -= nums[i - (k-1)]

    return maxValue


print(findMaxSumSubarray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
