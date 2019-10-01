# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# at each level of the tree increment the counter for the level.
# In a recursive fashion return 0 of the current level is null
# if either of the left or right children are not null recursively follow that path and take the max of either sides level count
# if the current level exist but the children are null return 1 for that levels count

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left or root.right:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 1
