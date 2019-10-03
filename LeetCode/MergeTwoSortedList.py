from nose.tools import assert_equal

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 1, 2, 4

# 1, 3, 4

# Recursive
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1

    start = None
    if l1.val < l2.val:
        start = l1
        start.next = self.mergeTwoLists(l1.next, l2)
    else:
        start = l2
        start.next = self.mergeTwoLists(l1, l2.next)

    return start


# Iterative
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

    if not l1:
        return l2
    if not l2:
        return l1

    temp = dummyHead = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next

    if l1:
        temp.next = l1
    if l2:
        temp.next = l2

    return dummyHead.next
