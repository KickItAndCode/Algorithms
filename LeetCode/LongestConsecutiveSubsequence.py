# Longest Consecutive Subsequence
# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
# Examples:

# Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
# Output: 4
# The subsequence 1, 3, 4, 2 is the longest subsequence
# of consecutive elements


# Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
# Output: 5
# The subsequence 36, 35, 33, 34, 32 is the longest subsequence
# of consecutive elements.


# One Solution is to first sort the array and find the longest subarray with consecutive elements. Time complexity of this solution is O(nLogn). Thanks to Hao.W for suggesting this solution.

def longestConsecutive(nums):
    if not nums:
        return 0

    nums.sort()

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if nums[i] == nums[i-1]+1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)

# Efficient Solution. The idea is to use Hashing. We first insert all elements in a Set. Then check all the possible starts of consecutive subsequences. Below is the complete algorithm.

# Create an empty hash.

# Insert all array elements to hash.

# Do following for every element arr[i]

# Check if this element is the starting point of a subsequence. To check this, we simply look for arr[i] – 1 in the hash, if not found, then this is the first element a subsequence.

# If this element is the first element, then count number of elements in the consecutive starting with this element. Iterate from arr[i] + 1 till the last element that can be found.

# If the count is more than the previous longest subsequence found, then update this.


def longestConsecutive(nums):
    maxLength, length, numSet = 0, 0, set(nums)

    # loop through all numbers
    for num in numSet:
          # if the num -1 isn't in the set we could be at the first of the sequence
        if num - 1 not in numSet:
            current_num = num
            length = 1

            # loop until you're outside of the sequence
            while current_num + 1 in numSet:
                current_num += 1
                length += 1

            # update max
            maxLength = max(maxLength, length)

    return maxLength

# different version by removing elements as you go


def longestConsecutive(nums):
    res, left = 0, set(nums)
    while left:
        l = r = left.pop()
        while l - 1 in left:
            left.remove(l - 1)
            l -= 1
        while r + 1 in left:
            left.remove(r + 1)
            r += 1

        res = max(res, r - l + 1)
    return res


print(longestConsecutiveSub([1, 9, 3, 10, 4, 20, 2]))  # 4
print(longestConsecutiveSub([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]))  # 5
