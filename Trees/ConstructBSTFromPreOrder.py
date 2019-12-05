# 1008. Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)


# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]


def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

    def helper(arr=[], limit=float("inf")):
        if arr and arr[0] < limit:
            val = arr.pop(0)
            node = TreeNode(val)
            node.left = helper(arr, val)
            node.right = helper(arr, limit)
            return node
        return None

    return helper(preorder)

# http://www.pythontutor.com/visualize.html#code=class%20TreeNode%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20x%29%3A%0A%20%20%20%20%20%20%20%20%20self.val%20%3D%20x%0A%20%20%20%20%20%20%20%20%20self.left%20%3D%20None%0A%20%20%20%20%20%20%20%20%20self.right%20%3D%20None%0A%0Adef%20bstFromPreorder%28preorder%29%3A%0A%0A%20%20%20%20def%20helper%28arr%3D%5B%5D,%20limit%3Dfloat%28%22inf%22%29%29%3A%0A%20%20%20%20%20%20%20%20if%20arr%20and%20arr%5B0%5D%20%3C%20limit%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20arr.pop%280%29%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20TreeNode%28val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20node.left%20%3D%20helper%28arr,%20val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20node.right%20%3D%20helper%28arr,%20limit%29%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20node%0A%20%20%20%20%20%20%20%20return%20None%0A%0A%20%20%20%20return%20helper%28preorder%29%0AbstFromPreorder%28%5B8,5,1,7,10,12%5D%29%0A&cumulative=false&curInstr=113&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
