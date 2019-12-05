# 199. Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1, 2, 3, null, 5, null, 4]
# Output: [1, 3, 4]
# Explanation:

#    1 < ---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


# this problem is level order traveral but you want to grab
# the last value in each level
def rightSideView(root):
    res, level = [], [root]
    while root and level:
        currlevel, nextLevel = [], []

        for node in level:
            currlevel.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        res.append(currlevel[-1])
        level = nextLevel
    return res
