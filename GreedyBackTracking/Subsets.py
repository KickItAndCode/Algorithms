
# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


def subsets(nums):
    subsets = [[]]
    for n in nums:
        subsets += [s + [n] for s in subsets]
    return subsets

# iterative


def subsets(nums):
    if nums == []:
        return []
    nums.sort()  # sort the array to avoid descending list of int
    res = [[]]
    for element in nums:
        temp = []
        for ans in res:
                # append the new int to each existing list
            temp.append(ans+[element])
        res += temp
    return res

# best solution


def subsets2(nums):
    res, path = [], []
    # nums is the list of arguments that are not included in the subset yet
    # path is the current subset
    # res is the result

    def helper(nums, path, res):
        for i, el in enumerate(nums):
            helper(nums[i + 1:], path + [el], res)
        res.append(path)

    helper(nums, path, res)
    return res


print(subsets2([1, 2, 3]))
#                      [1 2 3] []
#                      /    |    \
#           [2 3][1]      [3][2]  [][3]
#           /     \          |
#  [3] [1 2]    [][1 3]  [] [2 3]
#      /
#   [][1 2 3]
