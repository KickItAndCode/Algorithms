# 113. Path Sum II

# Given a binary tree and a sum, find all root-to-leaf paths where
#  each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  recursively go down each path subtracting its value from the sum
#  and check if


def pathSum(self, root: TreeNode, sum: int) -> bool:
    res = []
    self.pathSumHelper(root, sum, [], res)
    return res


def pathSumHelper(self, root, sum, curr, res):
    if not root:
        return

    # must be a leaf and the value is the sum
    if not root.left and not root.right and root.val == sum:
        curr.append(root.val)
        res.append(curr[:])
        return

    sum -= root.val
    curr.append(root.val)
    self.pathSumHelper(root.left, sum, curr[:], res)
    self.pathSumHelper(root.right, sum, curr[:], res)
