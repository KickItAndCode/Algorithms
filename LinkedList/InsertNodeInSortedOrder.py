class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def InsertNode(val, head):

    if not head:
        return Node(val)

    # case val needs to be interted at the beginning
    if val < head.val:
        NewHead = Node(val)
        NewHead.next = head
        return NewHead

    # val in between two nodes
    curr = head
    while curr.next:
        if curr.val <= val <= curr.next.val:
            temp = curr.next
            NewNode = Node(val)
            curr.next = NewNode
            NewNode.next = temp
            return head
        curr = curr.next

    # vall at the end

    if not curr.next and val > curr.val:
        curr.next = NewNode(val)
