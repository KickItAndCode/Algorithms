class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(val)
            else:
                curr = curr.right
    return root
