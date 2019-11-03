# 82. Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate
#  numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3


def deleteDuplicates(self, head: ListNode) -> ListNode:
    def listToLinkedList(lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

    map = {}

    curr = head
    while curr:
        if curr.val in map:
            map[curr.val] += 1
        else:
            map[curr.val] = 1

        curr = curr.next

    none_dups = []
    for k, v in map.items():
        if v == 1:
            none_dups.append(k)

    newHead = listToLinkedList(none_dups)
    return newHead


def deleteDuplicate(self, head):
    dummy = ListNode(0)
    dummy.next = head

    pre = dummy
    curr = head

    while curr:
        if curr.next and curr.val == curr.next.val:
            # loop until you get a value that isn't curr as they
            #  are next to each other
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next
            # now curr should not be the duplicated value.
            # attach the curr.next as the next value for prev
            pre.next = curr.next
        else:
            pre = pre.next
        curr = curr.next
    return dummy.next
