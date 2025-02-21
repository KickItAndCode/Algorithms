# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

from nose.tools import assert_equal


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    Reverse a linked list iteratively.
    Time: O(n), Space: O(1)
    """
    curr = head
    prev = None
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def reverseAlgoExpert(head):
    """
    Alternative iterative approach to reverse a linked list.
    Time: O(n), Space: O(1)
    """
    p1, p2 = None, head
    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1


def reverseWithDummy(head):
    """
    Reverse a linked list using a dummy node and stack.
    Time: O(n), Space: O(n)
    """
    dummy = Node(-1)
    stack = []
    while head:
        stack.append(head)
        head = head.next

    head = dummy
    while stack:
        curr = stack.pop()
        head.next = Node(curr.val)
        head = head.next
    return dummy.next


def create_test_list():
    """Create a test linked list: 1->2->3->4"""
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    return a


def verify_reversed_list(reversed_list):
    """Verify the list is properly reversed"""
    assert_equal(reversed_list.val, 4)
    assert_equal(reversed_list.next.val, 3)
    assert_equal(reversed_list.next.next.val, 2)
    assert_equal(reversed_list.next.next.next.val, 1)


# Test all reverse functions
test_list = create_test_list()
verify_reversed_list(reverseList(test_list))

test_list = create_test_list()
verify_reversed_list(reverseAlgoExpert(test_list))

test_list = create_test_list()
verify_reversed_list(reverseWithDummy(test_list))

# Visualization for the first method
test_list = create_test_list()
print("Original list: 1->2->3->4")
print("Reversed list:", end=" ")
curr = reverseList(test_list)
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("NULL")
