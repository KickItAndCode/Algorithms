# 617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


# Iterative
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        stack = []
        stack = [[t1, t2]]
        while stack:
            current = stack.pop()
            if current[0] == None or current[1] == None:
                continue
            current[0].val += current[1].val
            if current[0].left == None:
                current[0].left = current[1].left
            else:
                stack.append([current[0].left, current[1].left])
            if current[0].right == None:
                current[0].right = current[1].right
            else:
                stack.append([current[0].right, current[1].right])
        return t1
