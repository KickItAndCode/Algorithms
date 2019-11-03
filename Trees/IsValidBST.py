# 98. Validate Binary Search Tree

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

def isValidBST(self, root: TreeNode) -> bool:

    def valid(node, lower, upper):
        if not node:
            return True
        if lower is not None and node.val <= lower:
            return False
        if upper is not None and node.val >= upper:
            return False
        return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)

    return valid(root, None, None)
