from collections import deque

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 

    queue = deque()

def levelOrderPrint(tree):
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


def levelOrder(self, root):

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

def levelOrder(self, root):
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

root = Node(2)
root.left = Node(1)
root.right = Node(3)

levelOrderPrint(root)
