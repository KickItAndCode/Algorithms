from Node import *
from nose.tools import assert_equal


def cycle_check(node):

    slow = node
    fast = node

    while fast != None and fast.nextnode != None:
        slow = slow.nextnode
        fast = fast.nextnode.nextnode

        if slow == fast:
            return True

    return False


# def cycle_check(node):

#     slow = node
#     fast = node.nextnode

#     while fast and fast.nextnode:

#         if slow == fast:
#             return True

#         slow = slow.nextnode
#         fast = fast.nextnode.nextnode

#     return False
# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")

# Run Tests


t = TestCycleCheck()
t.test(cycle_check)
