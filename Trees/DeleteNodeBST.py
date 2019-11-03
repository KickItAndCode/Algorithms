class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    curr = root
    parent = None

    # Search For Node

    while curr is not None:
        if curr.val < key:
            parent = curr
            curr = curr.right
        elif curr.val > key:
            parent = curr
            curr = curr.left
        # Found Case
        else:
            # Two Children
            if curr.left is not None and curr.right is not None:
                curr = curr.right.getMin()
                curr.right.deleteNode(curr, curr.val)
            # No Parent
            elif parent == None:
                if curr.left is not None:
                    curr.value = curr.left.value
                    curr.right = curr.left.right
                    curr.left = curr.left.Left
                elif curr.right is not None:
                    curr.value = curr.right.value
                    curr.left = curr.right.left
                    curr.right = curr.right.right
            elif parent.left = curr:
                parent.left = curr.left if curr.left is not None else curr.right
            elif parent.right = curr:
                parent.right = curr.left if curr.left is not None else curr.right
            break
    return root
    # Left

    # Right

    # Neither

    # parent is also the child


def deleteNode(self, root, key):
    if root == None:
        return root
    if root.val < key:
        root.right = self.deleteNode(root.right, key)
    elif root.val > key:
        root.left = self.deleteNode(root.left, key)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        # two children
        else:
            # find successor (right left most child)
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.value
            # delete leaf
            root.right = self.deleteNode(root.right, root.val)
