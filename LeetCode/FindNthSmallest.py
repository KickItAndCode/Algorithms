from nose.tools import assert_equal
from heapq import *


class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


def nthSmallestNumber(nums, n):
    maxHeap = []
    for item in nums:
        heappush(maxHeap, MaxHeapObj(item))

    for i in range(len(nums) - n):
        heappop(maxHeap)

    return heappop(maxHeap).val


def findKthSmallest(nums, k):
    if nums:
        pos = partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]


# choose the right-most element as pivot
def partition(nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low  # O(nlgn) time


class NthSmallestNumberTest (object):

    def test(self, sol):
        assert_equal(sol([4, 2, 5, 6, 10], 3), 5)
        assert_equal(sol([4, 2, 5, 6, 10], 2), 4)
        print("ALL TEST CASES PASSED")


# Run and test
t = NthSmallestNumberTest()
t.test(nthSmallestNumber)
