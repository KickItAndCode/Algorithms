# 46. Permutations
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def permute(nums):
    res = []

    if len(nums) <= 1:
        return [nums]

    for i, num in enumerate(nums):
        for perm in permute(nums[:i] + nums[i+1:]):
            res.append([num] + perm)
    return res


print(permute([1, 2, 3]))
