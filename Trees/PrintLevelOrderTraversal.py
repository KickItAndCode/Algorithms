from collections import deque

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 

    queue = deque()

def levelOrder(tree):
    if tree is None:
        return

    queue = deque()
    queue.append(tree)
    while len(queue) != 0:
        temp = deque()
        while len(queue) != 0:
            node = queue.pop()
            print(str(node.val) + ' ')
            if node.left is not None:
                temp.append(tree.left)
            if node.right is not None:
                temp.append(tree.right)
            queue = temp


def levelOrder2(self, root):

    levels = []
    if not root:
        return levels

    def helper(node, level):
        # start the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.val)

        # process child nodes for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return levels

"""
"""
def levelOrder3(self, root):
    if not root: return []
    queue, res = deque([root]), []

    while queue:
        cur_level, size = [], len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            cur_level.append(node.val)
        res.append(cur_level)
    return res


"""
Level order printing with two queues
Create two queues
Initialize the first with root
While both queues are not empty 
pop from q1 and add its childen to the opposite queue
then the same for q2
each time a queue is empty you print a new line 
"""

def levelOrder4 (root):
    if not root: return []
    
    q1, q2 = deque(), deque()
    q1.append(root)

    while len(q1) > 0 or len(q2) > 0:
        while len(q1) > 0:
           
            curr = q1.pop()
            print(curr.val, end='')

            if curr.left:
                q2.append(curr.left)
            if curr.right:
                q2.append(curr.right)    
           
        print('\n',end= '')

        while len(q2) > 0:
            curr = q2.pop()
            print(curr.val, end = '')

            if curr.left:
                q1.append(curr.left)
            if curr.right:
                q1.append(curr.right)
   
        print('\n',end='')


root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.left.left = Node(6)

levelOrder4(root)
