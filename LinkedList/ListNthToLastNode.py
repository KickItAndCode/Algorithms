from nose.tools import assert_equal


class Node (object):
    def __init__(self, value):
        self.value = value
        self.next = None


def nth_to_last_node(n, head):

    slow = head
    fast = head

    for i in range(n-1):
        if not fast.next:
            raise LookupError('Error: N is large than the list')

        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow


def nth_to_last_node2(n, head):
    leader = head
    curr = head

    for i in range(n-1):
        if not leader.next:
            raise LookupError('Error')

        leader = leader.next

    while leader.next:
        curr = curr.next
        leader = leader.next

    return curr


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

####


class TestNLast(object):

    def test(self, sol):

        assert_equal(sol(2, a), d)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestNLast()
t.test(nth_to_last_node2)

# This would return the node d with a value of 4, because its the 2nd to last node.
# target_node = nth_to_last_node(2, a)
#
# target_node.value
