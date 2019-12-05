# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example:

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(self, root):
    # take care of base cases
    # if a node is empty, add 'x' to string
    # you can set 'x' to any mark as you want
    if not root: return 'x'
    # preoder(Root->left->right)
    # ex,
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    #
    # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
    # if you look at the return statement close, it is actually very intuitive
    # for value 1, you have 2 as left child and 3 as right child
    # for value 2, you have 'x'(None) as left child and 'x'(None) as right child, so on.
    return root.val, self.serialize(root.left), self.serialize(root.right)


def deserialize(self, data):
    #######################INTUITION#########################
    # The initial data string will be something like below:#
    # (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))#
    # if you loop through string:
    # 1                                 -> this is node value
    # (2, 'x', 'x')                     -> this is node left
    # (3, (4, 'x', 'x'), (5, 'x', 'x')) -> this is node right
    ########################################################
    # always take care of base case: if the node's value is 'x' then return None
    if data[0] == 'x': return None
    # create new treenode for node value
    node = TreeNode(data[0])
    # do the recursive to unpack string value
    node.left = self.deserialize(data[1])
    node.right = self.deserialize(data[2])
    # return the new TreeNode that we just created
    return node


class Codec:

    def serialize(self, root):

        if not root:
            return "X"

        leftSerialized = serialize(root.left)
        rightSerialized = serialize(root.right)

        return root.val + "," + leftSerialized + rightSerialized

    def deserialize(self, data):

        if not data:
            return None

        nodesLeftQueue = []
        nodesLeftQueue + s.split(",")
        return helper(nodesLeftQueue)

        def helper(nodesLeftQueue):
            node = queue.pop(0)
            if node == "X":
                return None

            newNode = TreeNode(int(node))
            newNode.left = helper(nodesLeftQueue)
            newNode.right = helper(nodesLeftQueue)

            return newNode


class Codec:

    def serialize(self, root):

        if not root:
            return "X"

       return root.val, serialize(root.left), serialize(root.right)

    def deserialize(self, data):

        if data[0] == "X":
            return None

        node = TreeNode(data[0])            
        newNode.left = deserialize(data[1])
        newNode.right = deserialize(data[2])

        return node
''
