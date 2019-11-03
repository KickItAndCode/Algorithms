# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most
#  frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of
#  unique elements.
# Your algorithm's time complexity must be better than
# O(n log n), where n is the array's size.

# put items into a map by count as val
# sort the map by value
# return k number of items from the sorted list


def topKFrequent(nums, k):
    map = {}
    for i in nums:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    arr = sorted(map, key=map.get, reverse=True)
    return(arr[:k])


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
