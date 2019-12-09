def isBalanced(root):
    if not root:
        return True

    lh, rh = Height(root.left), Height(root.right)

    return (abs(lh-rh) <= 1) and isBalanced(root.left) and isBalanced(root.right)


def Height(root):

    if root is None:
        return 0

    left = Height(root.left)
    right = Height(root.right)
    return max(left, right) + 1
