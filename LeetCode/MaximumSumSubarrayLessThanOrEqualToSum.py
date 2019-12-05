# Maximum sum subarray having sum less than or equal to given sum
# Given an array of integers and a sum. We have to find sum of subarray having maximum sum less than or equal to given sum in array.

# Examples:

# Input : arr[] = { 1, 2, 3, 4, 5 }
#         sum = 11
# Output : 10
# Subarray having maximum sum is { 1, 2, 3, 4 }

# Input : arr[] = { 2, 4, 6, 8, 10 }
#         sum = 7
# Output : 6
# Subarray having maximum sum is { 2, 4 } or { 6 }

# Constraints:
# 1<=T<=100
# 1<=n<=1000
# 1<=a[i],x<=100000


# Efficient Approach: The subarray having maximum sum can be found by using sliding window. If curr_sum is less than sum include array elements to it. If it becomes greater than sum remove elements from start in curr_sum.ß

def MaxSumSubarray(arr, sum):
    start, max_sum, curr_sum = 0, 0, arr[0]
    for i in range(1, len(arr)):

        # update max sum
        if curr_sum <= sum:
            max_sum = max(curr_sum, max_sum)

        # if curr sum becomes greater than sum
        # subtract startin elements of array

        while curr_sum + arr[i] > sum and start < i:
            curr_sum -= arr[start]
            start += 1

        # add elements to curr_sum
        curr_sum += arr[i]

    # final check to make sure we get the highest value
    if curr_sum <= sum:
        max_sum = max(max_sum, curr_sum)
    return max_sum


print(MaxSumSubarray([1, 2, 3, 4, 5], 11))  # 10
print(MaxSumSubarray([2, 4, 6, 8, 10], 7))  # 6
