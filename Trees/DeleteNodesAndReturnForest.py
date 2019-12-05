# 1110. Delete Nodes And Return Forest

# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest(a disjoint union of trees).

# Return the roots of the trees in the remaining forest.  You may return the result in any order.


# Example 1:


# Input: root = [1, 2, 3, 4, 5, 6, 7], to_delete = [3, 5]
# Output: [[1, 2, null, 4], [6], [7]]


# bottom up recursion
# after recusrive calls get to the both or the leaves
# then we process because we'll more information about the children

def delNodes(root, to_delete):
    remaining = []
    # make a set to have faster access
    toDeleteSet = set(to_delete)

    removeNodes(root, toDeleteSet, remaining)

    if root.val not in toDeleteSet:
        remaining.append(root)

    return remaining


def removeNodes(root, toDeleteSet, remaining):

    # stop when we get to leaves
    if not root:
        return None

    root.left = removeNodes(root.left, toDeleteSet, remaining)
    root.right = removeNodes(root.right, toDeleteSet, remaining)

    # if the curr val is in delete set we need to delete it
    if root.val in toDeleteSet:
        if root.left:
            remaining.append(root.left)
        if root.right:
            remaining.append(root.right)

        return None

    return root


def delNodes(self, root, to_delete):
    to_delete = set(to_delete)
    res = []

    def walk(root, parent_exist):
        if root is None:
            return None
        if root.val in to_delete:
            root.left = walk(root.left, parent_exist=False)
            root.right = walk(root.right, parent_exist=False)
            return None
        else:
            if not parent_exist:
                res.append(root)
            root.left = walk(root.left, parent_exist=True)
            root.right = walk(root.right, parent_exist=True)
            return root
    walk(root, parent_exist=False)
    return res
