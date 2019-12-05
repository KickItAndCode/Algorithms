# 257. Binary Tree Paths
# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


def binaryTreePaths(root):
    if not root:
        return []
    res, path = [], ""
    helper(res, path, root)
    return res


def helper(res, path, curr):
    # is leaf
    if not curr.left and not curr.right:
        res.append(path + str(curr.val))
    if curr.left:
        helper(res, path + str(curr.val) + "->", curr.left)
    if curr.right:
        helper(res, path + str(curr.val) + "->", curr.right)
