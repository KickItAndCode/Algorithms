# 226. Invert Binary Tree

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def _helper(node):
            if not Node:
                return None

            _helper(node.left)
            _helper(node.right)

            node.left, node.right = node.right, node.left
        _helper(root)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        self.invertTree(root)
        return root
