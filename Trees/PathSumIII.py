# 437. Path Sum III
# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# DFS with memoization: Use a variable prevSum to record the sum of all node values from the root r to the parent p of the current node. Then including the current node, the sum becomes currSum = prevSum + node.val. Now for each node on the path, we can calculate their respective currSum, we use a dictionary rec to record the frequency of all such sums. If the sum of nodes on a path ending with the current node has value sum, it implies that currSum - sum is in rec. Moreover, the number of such paths is rec[currSum - sum]. Then we can do DFS on the left and right child of the current node, with currSum being their prevSum. Also note that we need to do rec[currSum] -= 1 after DFS on the left and right child of the current node, because the current node is not on the path of DFSs on other nodes, hence currSum is not available for other DFSs.

# Time complexity: O(n), space complexity: O(n).


def pathSum(self, root, target):
    self.ans = 0
    cache = collections.defaultdict(int)
    cache[0] = 1

    def dfs(root, cur_sum):
        if not root:
            return
        cur_sum += root.val
        self.ans += cache[cur_sum - target]
        cache[cur_sum] += 1
        dfs(root.left, cur_sum)
        dfs(root.right, cur_sum)
        cache[cur_sum] -= 1

    dfs(root, 0)
    return self.ans


 def pathSum(self, root, target):
    def findSum(root, totSum):
        if not root: return
        totSum += root.val
        res[0] += partSums[totSum - target]
        partSums[totSum] += 1
        findSum(root.left, totSum)
        findSum(root.right, totSum)
        partSums[totSum] -= 1
    
    res = [0]
    partSums = collections.Counter([0])
    findSum(root, 0)
    return res[0]


