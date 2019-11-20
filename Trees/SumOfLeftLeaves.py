# 404. Sum of Left Leaves
# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


def sumOfLeftLeaves(self, root):
    if not root:
        return 0

    elif root.left and not root.left.left and not root.left.right:
        return root.left.val + self.sumOfLeftLeaves(root.right)
    else:
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


def sumOfLeftLeaves(self, root):
    if not root:
        return 0

    sum = 0
    if root.left:
        self.helper(root.left, true)
    if root.right:
        self.helper(root.right, false)
    return sum


def helper(sum, root, fromLeft):
    # is leaf
    if not root.left and not root.right and fromLeft:
        sum += root.val
    else:
        if root.left:
            self.helper(root.left, true)
        if root.right:
            self.helper(root.right, false)
