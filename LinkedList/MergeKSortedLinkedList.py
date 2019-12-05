# 23. Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


from heapq import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    heap = []
    dummy = ListNode(-1)
    for curr in lists:
        while curr:
            heappush(heap, (curr.val))
            curr = curr.next

    head = dummy
    while heap:
        val = heappop(heap)
        head.next = ListNode(val)
        head = head.next

    return dummy.next
