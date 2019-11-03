# 101. Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


def isSymmetric(self, root: TreeNode) -> bool:
    return self.isMirror(root, root)


def isMirror(self, left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return (left.val == right.val) and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)


def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    queue = []
    queue.append((root.left, root.right))
    while queue:
        l, r = queue.pop()
        # both are null
        if l is None and r is None:
            continue
        # at least one is null
        if l is None or r is None:
            return False

        # if they're not equal its not not symmetrical
        if l.val != r.val:
            return False

        # add the children to the queue
        queue.append((l.left, r.right))
        queue.append((l.right, r.left))
    return True
