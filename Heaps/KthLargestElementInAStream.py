# 703. Kth Largest Element in a Stream

# Design a class to find the kth largest element in a stream. Note that
# it is the kth largest element in the sorted order, not the kth distinct
#  element.

# Your KthLargest class will have a constructor which accepts an integer
#  k and an integer array nums, which contains initial elements from the
#  stream. For each call to the method KthLargest.add, return the element
#  representing the kth largest element in the stream.

# Example:

# int k = 3
# int[] arr = [4, 5, 8, 2]
# KthLargest kthLargest = new KthLargest(3, arr)
# kthLargest.add(3)
# // returns 4
# kthLargest.add(5)
# // returns 5
# kthLargest.add(10)
# // returns 5
# kthLargest.add(9)
# // returns 8
# kthLargest.add(4)
# // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.


"""
Create a pq - keep it only having the k-largest elements by popping off small elements.
With only k elements, the smallest item (self.pool[0]) will always be the kth largest.

If a new value is bigger than the smallest, it should be added into your heap.
If it's bigger than the smallest (that are already the kth largest), it will certainly be within the kth largest of the stream.
"""

from heapq import *


class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
