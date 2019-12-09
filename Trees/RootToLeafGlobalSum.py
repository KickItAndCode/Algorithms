class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


# TIme O(n) and Space O(h)
def SumRootToLeaf(root):

    def helper(tree, partialPathSum=0):
        if not tree:
            return 0

        partialPathSum = partialPathSum * 2 + tree.val

        # leaf
        if not tree.left and not tree.right:
            return partialPathSum
        # non leaf
        return (helper(root.left, partialPathSum) + helper(root.right, partialPathSum))

    return helper(tree)
