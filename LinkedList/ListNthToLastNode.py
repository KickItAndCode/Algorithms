from nose.tools import assert_equal

class Node (object):
    def __init__ (self, value):
        self.value = value
        self.nextnode = None

def nth_to_last_node(n, head):

    slow = head
    fast = head

    for i in range(n-1):
        if not fast.nextnode:
            raise LookupError('Error: N is large than the list')


        fast = fast.nextnode

    while fast.nextnode:
        slow = slow.nextnode
        fast = fast.nextnode

    return slow



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):

    def test(self,sol):

        assert_equal(sol(2,a),d)
        print 'ALL TEST CASES PASSED'

# Run tests
t = TestNLast()
t.test(nth_to_last_node)

# This would return the node d with a value of 4, because its the 2nd to last node.
# target_node = nth_to_last_node(2, a)
#
# target_node.value
