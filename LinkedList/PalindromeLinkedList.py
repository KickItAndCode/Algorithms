# 234. Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# convert to a list and then reverse the last and
# compare with regular list


def isPalindrome(self, head: ListNode) -> bool:
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr.next

    return nums == nums[::-1]


# slow fast pointers
# move slow to one past halfway
# reverse first half of the last on the way
# traverse reverse first half and second half
# checking for equality
#
def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev
