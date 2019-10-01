# 136. Single Number


# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2, 2, 1]
# Output: 1
# Example 2:

# Input: [4, 1, 2, 1, 2]
# Output: 4


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sets in python don't allow dups
        mem = set()

        for num in nums:
            if num in mem:
                mem.remove(num)
            else:
                mem.add(num)

        for num in mem:
            return num
