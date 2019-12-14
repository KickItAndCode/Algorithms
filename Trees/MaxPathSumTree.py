#  123 Max Path Sum In Binary Tree

# Write a function that takes in a Binary Tree and returns its max path sum. A path is a collection of connected nodes where no node is connected to more than two other nodes
# a path sum is the sum of the values of the nodes in a particular path. Each Binary Tree node has a value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value.


# LEET CODE SOLUTION
# Bottom Up Optimized Solution: O(N)

# Bottom up template uses post-order traversal and usually returns two items. To visualize this algorithm, always start with bottom up picture returning 1 or 2 values
# In this algorithm, we can use post-order traversal and return the maximum sum in the subtree starting from the root.
# We call it lresult and rresult for left and right subtree


class Solution(object):
    def maxPathSum(self, root):
        self.max_so_far = float('-inf')
        self.helper(root)  # Maximum sum starting from root
        return self.max_so_far

    def helper(self, root):

        if root == None:
            return 0
        # Maximum sum starting from root.left
        lresult = max(self.helper(root.left), 0)

        # Maximum sum starting from root.left
        rresult = max(self.helper(root.right), 0)

        self.max_so_far = max(lresult + rresult + root.val, self.max_so_far)

        # Return maximum sum starting from root
        return max(lresult, rresult) + root.val

    def maxPathSum(self, root):
        self.max_so_far = float('-inf')
        self.helper(root)  # Maximum sum starting from root
        return self.max_so_far

    def helper(self, root):

        if root == None:
            return 0
        # Maximum sum starting from root.left
        lresult = self.helper(root.left)

        # Maximum sum starting from root.left
        rresult = self.helper(root.right)

        self.max_so_far = max(
            max(lresult, 0) + max(rresult, 0) + root.val, self.max_so_far)
        # Return maximum sum starting from root
        return max(lresult, rresult, 0) + root.val


def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    _, maxSum = findMaxSum(tree)
    return maxSum

# ALGO EXPERT SOLUTION FAULS 42 / 93 test cases passed.


def findMaxSum(root):
    if not root:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(root.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(root.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = root.val
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value +
                           rightMaxSumAsBranch, maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
    return (maxSumAsBranch, maxPathSum)
