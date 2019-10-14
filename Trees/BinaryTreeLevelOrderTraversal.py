#  102. Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of
# its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# [20 30]


def levelOrder(root):
    res, level = [], [root]
    while root and level:
        currlevel, nextLevel = [], []

        for node in level:
            currlevel.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        res.append(currlevel)
        level = nextLevel
    return res


#     10
#   /    \
# 20      30
#           \
#            40
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.right = TreeNode(40)
levelOrder(root)
