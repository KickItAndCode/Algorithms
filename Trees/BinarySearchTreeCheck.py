import math
# tree_vals = []
#
# def inorder(tree):
#     if tree != None:
#         inorder(tree.getLeftChild())
#         tree_vals.append(tree.getRootVal())
#         inorder(tree.getRightChild())
#
# def validBST (tree_vals):
#     return tree_vals == sorted(tree_vals)
#
# inorder(tree)
# validBST(tree_vals)


class Node:
    def __init__(self, k, val):
        self.key = k
        self.val = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <=  tree_min(node.right) and verify(node.left) and verify(node.right)):
        return True
    else:
        return False



def IsBST(root, min, max):
    if root is None:
         return True
    if root.val < min or root.val > max:
        return False
    
    return IsBST(root.left, min, root.val) and IsBST(root.right, root.val, max)


root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(IsBST(root,float("-inf"), float("inf") )) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

# print(verify(root)) # prints False, since 15 is to the left of 10
print(IsBST(root, -math.inf, math.inf)) 