# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]


def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    findCombinations(candidates, 0, target, [], res)
    return res


def findCombinations(candidates, index, target, path, res):

    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i-1]:
            continue
        findCombinations(candidates, i+1, target -
                         candidates[i], path+[candidates[i]], res)


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(combinationSum2([2, 5, 2, 1, 2], 5))
