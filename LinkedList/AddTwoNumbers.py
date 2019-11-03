# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
#  contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# l1     1     3                              1
# +      +     +                              +
# l2     1     9                              1
# -----------------------------------------------------------------------------------
# cur    2    12(we need to put 2 here)        2+carry(carry from the previous 12)
#             12 %10 = 2
# 		    carry = 12//10 =1
# By adding a variable called carry can deal with this situation: align the
# addends vertically and add the columns, starting from the left-most column.
#  If a column's sum exceeds nine, the extra digit "carried" add into the next column.

# l1          1                  3                       1
# +           +                  +                       +
# l2          1                  9                       1
# -----------------------------------------------------------------------------------
# carry  0+1+1=3             0+3+9=12              1+1+1 = 3
# cur     3%10=3             12%10=2               3%10 = 3
# carry  3//10 =0             12//10=1             3//10 = 0


def addTwoNumbers(self, l1, l2):
    carry = 0
    val = 0
    dummy = curr = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1 + v2 + carry, 10)

        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.next


def addTwoNumbers(self, l1, l2):
    def toint(node):
        return node.val + 10 * toint(node.next) if node else 0

    def tolist(n):
        node = ListNode(n % 10)
        if n > 9:
            node.next = tolist(n / 10)
        return node
    return tolist(toint(l1) + toint(l2))


def addTwoNumbers(self, l1, l2):
    def toint(node):
        return node.val + 10 * toint(node.next) if node else 0
    n = toint(l1) + toint(l2)
    first = last = ListNode(n % 10)
    while n > 9:
        n /= 10
        last.next = last = ListNode(n % 10)
    return first
