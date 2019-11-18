# 219. Contains Duplicate II
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


# use a hashmap to store values and its index
# if we run into a number thats already in our dictionary then we know its a dupe
# if its a dupe also check if its index distance from the original is less than or equal to k
# if so its our dupe return True
def containsNearbyDuplicate(nums, k):
    map = {}

    for i, num in enumerate(nums):
        if num in map and i - map[num] <= k:
            return True
        else:
            map[num] = i
    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # true
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # false
