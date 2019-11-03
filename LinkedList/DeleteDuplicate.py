# 83. Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates
#  such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3


def deleteDuplicates(self, head: ListNode) -> ListNode:

    if not head:
        return head

    curr = head.next
    prev = head

    while curr:
        if curr.val == prev.val:
            prev.next = curr.next
            curr = curr.next
        else:
            curr = curr.next
            prev = prev.next

    return head
