from nose.tools import assert_equal
from heapq import *

# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Time O(nlogn) Space O(1)


def nthLargestNumber2(nums, n):
    nums.sort()
    return nums[len(nums) - n]


# using a heap provides O(n) creating using heapify then you can
# pop off elements until you have the nth element
# Time O(N) Space O(1)
def nthLargestNumber(nums, n):
    heapify(nums)
    for i in range(0, len(nums) - n):
        heappop(nums)
    return heappop(nums)


class NthLargestNumberTest (object):

    def test(self, sol):
        assert_equal(sol([4, 2, 5, 22, 1, 10], 3), 5)
        assert_equal(sol([4, 2, 5, 22, 1, 10], 2), 10)
        assert_equal(sol([4, 2, 5, 6, 10], 2), 6)
        assert_equal(sol([2, 1], 1), 2)
        print("ALL TEST CASES PASSED")


# Run and test
t = NthLargestNumberTest()
t.test(nthLargestNumber)

# O(nlgn) time


def findKthLargest1(self, nums, k):
    return sorted(nums, reverse=True)[k-1]

# O(nk) time, bubble sort idea, TLE


def findKthLargest2(self, nums, k):
    for i in xrange(k):
        for j in xrange(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]

# O(nk) time, selection sort idea


def findKthLargest3(self, nums, k):
    for i in xrange(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in xrange(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]

# O(k+(n-k)lgk) time, min-heap


def findKthLargest4(self, nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in xrange(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

# O(k+(n-k)lgk) time, min-heap


def findKthLargest5(self, nums, k):
    return heapq.nlargest(k, nums)[k-1]

# O(n) time, quick selection


def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)
