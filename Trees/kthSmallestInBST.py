# Given a binary search tree, write a function kthSmallest to find
# the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

1, 2, 3, 4


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthSmallest(root: TreeNode, k):
    res = []
    inOrder(root, res)
    print(res)
    return res[k-1]


def inOrder(root, res):
    if not root:
        return
    inOrder(root.left, res)
    res.append(root.val)
    inOrder(root.right, res)

#      20
#   10    30
# 5        40


root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(5)
root.right = TreeNode(30)
root.right.right = TreeNode(40)
print(kthSmallest(root, 1))
# print(kthSmallest(root, 2))
# print(kthSmallest(root, 3))
