class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrderTraversalIterative(root):
    stack = []
    visit = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        visit.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    print(visit)


def preOrderTraversal(root):
    if root is None:
        return
    print(root.val)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def InOrderTraversalIterative(root):

    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            res.append(temp.val)
            root = temp.right
    print(res)

# Easier to understand involves a trick but is O(n)


def PostOrderTraversalIterative(root):
    stack = []
    visit = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        # add to front to have children come after
        visit.insert(0, curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    print(visit)

# def PostOrderTraversalIterative(root):
#     stack = []
#     visit = []
#     curr = root
#     while curr or stack:
#         if curr:
#             stack.append(curr)
#             curr = curr.left
#         else:
#             temp = stack[len(stack) - 1].right
#             if temp is None:
#                 temp = stack.pop()
#                 visit.append(temp.val)
#                 while stack and temp == stack[len(stack) - 1].right:
#                     temp = stack.pop()
#                     visit.append(temp.val)
#             else:
#                 curr = temp
#     print(visit)


def InOrderTraversal(root):
    if root is None:
        return
    InOrderTraversal(root.left)
    print(root.val)
    InOrderTraversal(root.right)


def PostOrderTraversal(root):
    if root is None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print(root.val)

    #        10
    #       /  \
    #      5    25
    #     / \   / \
    #    3  8  20   50


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right = TreeNode(25)
root.right.left = TreeNode(20)
root.right.right = TreeNode(50)

print(f"Pre Order Traversal ")
preOrderTraversalIterative(root)
print(f"Pre Order Traversal Recursive")
preOrderTraversal(root)
print(f"In Order Traversal ")
InOrderTraversalIterative(root)
print(f"In Order Traversal Recursive")
InOrderTraversal(root)
print(f"Post Order Traversal ")
PostOrderTraversalIterative(root)
print(f"Post Order Traversal Recursive")
PostOrderTraversal(root)
