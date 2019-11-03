def sortedArrayToBST(self, nums):
    # check if array is empty

    # Get the mid point
    mid = len(nums) // 2

    # and create that nood as root
    root = TreeNode(nums[mid])

    # recursively slice from mid to the left and mid
    # to the right for the tree
    root.left = self.sortedArrayToBST(nums[: mid])
    root.right = self.sortedArrayToBST(nums[mid + 1:])

    return root
