# 337. House Robber III
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:

# Input: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \
#      3   1

# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:

# Input: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \
#  1   3   1

# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


def rob(self, root: TreeNode) -> int:
    res = self.robSub(root)
    return max(res[0], res[1])

# dfs solution
# first value on in the array will be sum without root val
# second value in the array will be sum with root val


def robSub(self, root):
    if not root:
        return [0, 0]

    left = self.robSub(root.left)
    right = self.robSub(root.right)
    res = [0, 0]
    res[0] = max(left[0], left[1]) + max(right[0], right[1])
    res[1] = root.val + left[0] + right[0]

    return res


# slow doesn't pass all leet code test cases TLE
def rob(self, root: TreeNode) -> int:
    if not root:
        return 0

    return max(self.robInclude(root), self.robExclude(root))


def robInclude(self, root):
    if not root:
        return 0
    return robExclude(root.left) + robExclude(root.right) + root.val


def robExclude(self, root):
    if not root:
        return 0
    return self.rob(root.left) + self.rob(root.right)
