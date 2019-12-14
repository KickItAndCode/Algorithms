#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# -----------
# pre = 5
# cur = 4

#     1
#    /
#   2
#  / \
# 3   4
#      \
#       5
#        \
#         6
# -----------
# pre = 4
# cur = 3

#     1
#    /
#   2
#  /
# 3
#  \
#   4
#    \
#     5
#      \
#       6
# -----------
# cur = 2
# pre = 3

#     1
#    /
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# -----------
# cur = 1
# pre = 2

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


prev = None


def flatten(self, root):
    if not root:
        return
    self.prev = root
    self.flatten(root.left)

    temp = root.right
    root.right, root.left = root.left, None
    self.prev.right = temp

    self.flatten(temp)


def flatten(self, root):
    stack = []
    while root or stack:
        # something on left and right. push right node onto stack, swap and move left
        if root.left and root.right:
            stack.append(root.right)
            root.right = root.left
            root.left = None
            root = root.right
        # if just left, then swap and traverse
        elif root.left:
            root.right = root.left
            root.left = None
            root = root.right
        # if just right, then just traverse rightwards
        elif root.right:
            root = root.right
        else:
            if stack:
                root.right = stack.pop()
            root = root.right
    return
