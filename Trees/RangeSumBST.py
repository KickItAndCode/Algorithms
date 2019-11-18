# 938. Range Sum of BST
# Easy

# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.


# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23


def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    def dfs(root):

        if root:
            self.sum += root.val if L <= root.val <= R else 0
            dfs(root.left)
            dfs(root.right)

    self.sum = 0
    dfs(root)
    return self.sum
