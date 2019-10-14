class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def searchBST(root, val):

    if not root:
        return
    if root.val == val:
        return root
    return searchBST(root.left, val) or searchBST(root.right, val)


def searchBSTIterative(root, va):
    while root:
        if root.val == val:
            break
        elif val < root.val:
            node = node.left
        else:
            node = node.right
    return root


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.right = TreeNode(40)
print(searchBST(root, 20))
