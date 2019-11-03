# 653. Two Sum IV - Input is a BST
# Given a Binary Search Tree and a target number, return true
#  if there exist two elements in the BST such that their sum
# is equal to the given target.

# Example 1:

# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# Output: True


# Example 2:

# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 28

# Output: False


def findTarget(self, root: TreeNode, k: int) -> bool:
    res = []

    def InOrder(self, root, res):
        if not root:
            return
        self.InOrder(root.left)
        res.append(root.val)
        self.InOrder(root.right)
    self.InOrder(root, res)

    # 1 2 5 8 10 Target 6
    # L R
    l = 0
    r = len(res)-1
    for num in res:
        sum = res[l] + res[t]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return True
    return False
