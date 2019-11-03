# 112. Path Sum

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
#  such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


#  recursively go down each path subtracting its value from the sum and check if
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False

    # must be a leaf and the value is the sum
    if not root.left and not root.right and root.val == sum:
        return True

    sum -= root.val

    return self.hasPathSum(root.right, sum) or
    hasPathSum(root.left, sum)
