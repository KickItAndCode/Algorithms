# 1038. Binary Search Tree to Greater Sum Tree
# Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# We need to do the work from biggest to smallest, right to left.
# pre will record the previous value the we get, which the total sum of bigger values.
# For each node, we update root.val with root.val + pre.


# This method for tree traversal is known as a reverse in-order traversal, and allows us to guarantee visitation of each node in the desired order. The basic idea of such a traversal is that before visiting any node in the tree, we must first visit all nodes with greater value. Where are all of these nodes conveniently located? In the right subtree.

# Intuition

# One way to perform a reverse in-order traversal is via recursion. By using the call stack to return to previous nodes, we can easily visit the nodes in reverse order.

# Algorithm

# For the recursive approach, we maintain some minor "global" state so each recursive call can access and modify the current total sum. Essentially, we ensure that the current node exists, recurse on the right subtree, visit the current node by updating its value and the total sum, and finally recurse on the left subtree. If we know that recursing on root.right properly updates the right subtree and that recursing on root.left properly updates the left subtree, then we are guaranteed to update all nodes with larger values before the current node and all nodes with smaller values after.
def bstToGst(root):
    s = [0]

    def inOrder(root):
        if root:
            inOrder(root.right)
            root.val += s[0]
            s[0] = root.val
            inOrder(root.left)
    inOrder(root)
    return root


class Solution:
    def __init__(self):
        self.val = 0

    def bstToGst(self, root):
        if not root:
            return TreeNode(0)

        self.bstToGst(root.right)
        root.val += self.val
        self.val = root.val
        self.bstToGst(root.left)

        return root


# Intuition

# If we don't want to use recursion, we can also perform a reverse in-order traversal via iteration and a literal stack to emulate the call stack.

# Algorithm

# One way to describe the iterative stack method is in terms of the intuitive recursive solution. First, we initialize an empty stack and set the current node to the root. Then, so long as there are unvisited nodes in the stack or node does not point to null, we push all of the nodes along the path to the rightmost leaf onto the stack. This is equivalent to always processing the right subtree first in the recursive solution, and is crucial for the guarantee of visiting nodes in order of decreasing value. Next, we visit the node on the top of our stack, and consider its left subtree. This is just like visiting the current node before recursing on the left subtree in the recursive solution. Eventually, our stack is empty and node points to the left null child of the tree's minimum value node, so the loop terminates.

def convertBST(self, root):
    total = 0

    node = root
    stack = []
    while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
        while node is not None:
            stack.append(node)
            node = node.right

        node = stack.pop()
        total += node.val
        node.val = total

        # all nodes with values between the current and its parent lie in
        # the left subtree.
        node = node.left

    return root
