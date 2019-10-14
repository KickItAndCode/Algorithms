
# 572. Subtree of Another Tree

# Given two non-empty binary trees s and t, check whether tree t has
# exactly the same structure and node values with a subtree of s. A subtree of s
#  is a tree consists of a node in s and all of this node's descendants. The tree
# s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree
# of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    if not s:
        return False
    if self.isSameTree(s, t):
        return True
    return self.isSubtree(s.left, t) or self. isSubtree(s.right, t)


def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q


# this solution turns the tree into a string representation of the tree by traversing
# it uses a pound as a delimiter to weed out false positives
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def traverse_tree(node):
        if not node:
            return None
        return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"
    return traverse_tree(t) in traverse_tree(s)
