class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def union(l1, l2):
    pass


def intersection(l1, l2):

    Dummy = ListNode(-1)
    NewHead = None
    Dummy.next = NewHead
    if not l1 or not l2:
        return None

    while l1 and l2:
        if l1.val == l2.val:
            NewHead = ListNode(l1.val)
            NewHead = NewHead.next
        l1 = l1.next
        l2 = l2.next

    return Dummy.next


# Create a list of 4 nodes
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d


e = ListNode(1)
f = ListNode(5)
g = ListNode(6)
h = ListNode(2)

e.next = f
f.next = g
g.next = h


# Set up order a,b,c,d with vals 1,2,3,4

print(union(a, e))
print(intersection(a, e))
#
