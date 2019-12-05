# 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.res = None

    def lowestCommonAncestor(root, p, q):

        def recurse_tree(curr):
            # if reach the end of a branch return false
            if not curr:
                return False
            # Left
            left = recurse_tree(curr.left)
            # Right
            right = recurse_tree(curr.right)

            # if the curr node is one of p or q
            mid = curr == p or curr == q

            # if any of the two three flags left, right or mid become true

            if mid + left + right >= 2:
                self.res = curr

            # return true if either of the three bool values is true
            return mid or left or right
        recurse_tree(root)
