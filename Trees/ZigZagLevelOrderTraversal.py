# 103. Binary Tree Zigzag Level Order Traversal
# n a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:

# [
#   [3],
#   [20,9],
#   [15,7]
# ]


def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    # standard level order traversal
    res, level = [], [root]
    while root and level:
        currLevel, nextLevel = [], []
        for node in level:
            currLevel.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        res.append(currLevel)
        level = nextLevel

    # reverse every other list in the list for zig zag
    for i in range(1, len(res), 2):
        res[i] = reversed(res[i])
    return res
