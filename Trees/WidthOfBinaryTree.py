# 662. Maximum Width of Binary Tree
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input:

#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input:

#           1
#          /
#         3
#        / \
#       5   3

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input:

#           1
#          / \
#         3   2
#        /
#       5

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input:

#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

# As we need to reach every node in the given tree, we will have to traverse the tree, either with a depth-first search, or with a breadth-first search.

# The main idea in this question is to give each node a position value. If we go down the left neighbor, then position -> position * 2; and if we go down the right neighbor, then position -> position * 2 + 1. This makes it so that when we look at the position values L and R of two nodes with the same depth, the width will be R - L + 1.


def widthOfBinaryTree(self, root: TreeNode) -> int:
    # root depth position
    queue = [(root, 0, 0)]

    currDepth = left = res = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth + 1, pos * 2))
            queue.append((node.right, depth + 1, pos * 2 + 1))

            if currDepth != depth:
                currDepth = depth
                left = pos
            res = max(pos - left + 1, , res)
    return res


 def widthOfBinaryTree(self, root):
        if not root: 
            return []
        
        width, level = 0, [(root, 1)]
        
        # Keep going until current level has some nodes.
        while level:
            # Put all children of current level in next_level.
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:   # Make sure to not put the Null nodes
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2+1))
            level = next_level
        return width
    
# level order traversal for reference very similar 
def levelOrder(root):
    res, level = [], [root]
    while root and level:
        currlevel, nextLevel = [], []

        for node in level:
            currlevel.append(node.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        res.append(currlevel)
        level = nextLevel
    return res
