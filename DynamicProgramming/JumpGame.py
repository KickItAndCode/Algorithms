# 55. Jump Game
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.

# Time O(n^2) Space O(N)


def canJumpDP(nums):
    dp = [False]*len(nums)
    dp[0] = True
    for i in range(1, len(nums)):
        for j in range(i-1, -1, -1):
            if dp[j] == True and nums[j] + j >= i:
                dp[i] = True
                break
    return dp[-1]


# Approach 4: Greedy

# Once we have our code in the bottom-up state, we can make one final, important observation.
# rom a given position, when we try to see if we can jump to a GOOD position, we only ever use
#  one - the first one (see the break statement). In other words, the left-most one. If we keep
#  track of this left-most GOOD position as a separate variable, we can avoid searching for it
# in the array. Not only that, but we can stop using the array altogether.

# Iterating right-to-left, for each position we check if there is a potential jump that reaches
#  a GOOD index (currPosition + nums[currPosition] >= leftmostGoodIndex). If we can reach a GOOD
# index, then our position is itself GOOD. Also, this new GOOD position will be the new leftmost
#  GOOD index. Iteration continues until the beginning of the array. If first position is a GOOD
#  index then we can reach the last index from the first position.

# To illustrate this scenario, we will use the diagram below, for input array nums =
#  [9, 4, 2, 1, 0, 2, 0]. We write G for GOOD, B for BAD and U for UNKNOWN. Let's assume we have
#  iterated all the way to position 0 and we need to decide if index 0 is GOOD. Since index 1 was
#  determined to be GOOD, it is enough to jump there and then be sure we can eventually reach index 6.
#  It does not matter that nums[0] is big enough to jump all the way to the last index. All we need is one way.

# Index	0	1	2	3	4	5	6
# nums	9	4	2	1	0	2	0
# memo	U	G	B	B	B	G	G


def canJumpGreedy(nums):
    lastPos = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastPos:
            lastPos = i
    return lastPos == 0


def canJump(nums):
    curr_max = 0
    for i in range(len(nums)):
        if i > curr_max:
            return False
        curr_max = max(curr_max, i + nums[i])
    return True


print(canJumpDP([2, 3, 1, 1, 4]))  # true
print(canJumpDP([3, 2, 1, 0, 4]))  # false
print(canJumpGreedy([2, 3, 1, 1, 4]))  # true
print(canJumpGreedy([3, 2, 1, 0, 4]))  # false
print(canJump([2, 3, 1, 1, 4]))  # true
print(canJump([3, 2, 1, 0, 4]))  # false
