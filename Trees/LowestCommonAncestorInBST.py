class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


# Favorite Solution
# Time O(N) | Space O(N)
# if both the numbers are less than the parent then go to the right
#  recursively
# if both the bumbers are greater than the parent than look to the
# right
# else return the root


def LCA3(root, p, q):
    # If both p and q are greater than parent
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    # If both p and q are lesser than parent
    elif p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    # We have found the split point, i.e. the LCA node.
    else:
        return root

    """
using recursion identify find out if the current value
is greater than the max of the two nodes you're trying to find
if so recursively look on the left side

if the current value is less than the min of the two nodes then
look on the right

otherwise return the root as that is the LCA

"""


def lca(root, n1, n2):

    if root.val > max(n1, n2):
        return lca(root.left, n1, n2)
    elif root.val < min(n1, n2):
        return lca(root.right, n1, n2)
    else:
        return root


def lca2(root, x, y):
    if root is None:
        return None

    if root.val == x or root.val == y:
        return root

    leftSearchResult = lca2(root.left, x, y)
    rightSearchResult = lca2(root.right, x, y)

    if leftSearchResult is None:
        return rightSearchResult
    if rightSearchResult is None:
        return leftSearchResult

    return root


# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

#             20

#         8       22
#    4      12
#         10  14


t = lowestCommonAncestor(root, root.left.left, root.left.right)
print(f"LCA is : {t.val}")

# n1 = 14
# n2 = 8
# t = lca2(root, n1, n2)
# print(f"LCA of {n1} and {n2} is {t.val}")

# n1 = 10
# n2 = 22
# t = lca2(root, n1, n2)
# print(f"LCA of {n1} and {n2} is {t.val}")
