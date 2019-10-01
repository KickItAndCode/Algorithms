# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?


# from Node import *


from nose.tools import assert_equal


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: Node) -> Node:
    curr = head
    prev = None
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


# def reverse(head):
#     curr = head
#     prev = None
#     next = None

#     while curr:

#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with vals 1,2,3,4
a.next = b
b.next = c
c.next = d
print(a.next.val)
print(b.next.val)
print(c.next.val)
#
reverseList(a)
#
#
# print(d.next.val)
# print(c.next.val)
# print(b.next.val)
