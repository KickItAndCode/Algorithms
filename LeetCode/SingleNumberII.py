# 137. Single Number II
# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3
# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99

from collections import Counter, defaultdict
import operator


def singleNumber(nums):
    map = defaultdict(int)
    for n in nums:
        map[n] += 1

    minNumber = (0, float("inf"))
    for k, v in map.items():
        if v < minNumber[1]:
            minNumber = (k, v)
    return minNumber[0]


def singleNumber2(nums):
    map = Counter(nums)
    return min(map.items(), key=operator.itemgetter(1))[0]


print(singleNumber([2, 2, 3, 2]))  # 3
print(singleNumber([0, 1, 0, 1, 0, 1, 99]))  # 99
