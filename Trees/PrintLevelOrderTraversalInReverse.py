from collections import deque

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 


"""
Using a stack and a queue
push root to the queue
then loop while queue isn't empty 
adding right then left childen of root
then push root to the stack


then loop through the stack while its not 
empty and pop from the stack print val each time
"""
def levelOrderReverse(root):
    if not root:
        return

    stack = deque()
    queue = deque()

    queue.appendleft(root)
    while len(queue) > 0:
        root = queue.pop()
        if root.right:
            queue.appendleft(root.right)
        if root.left:
            queue.appendleft(root.left)
        stack.append(root)

    while len(stack) > 0:
        print(stack.pop().val, end= "")


root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.left.left = Node(6)
print()
levelOrderReverse(root)
print()