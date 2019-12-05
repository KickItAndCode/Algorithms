# 384. Shuffle an Array
# Shuffle a set of numbers without duplicates.

# Example:

# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);

# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();

# // Resets the array back to its original configuration [1,2,3].
# solution.reset();

# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

from random import randrange


class Solution:

    def __init__(self, nums):
        self.num = nums
        self.original = list(nums)

    def reset(self):
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

# O(n^2) Time
    def shuffle(self):
        # create a
        aux = list(self.nums)
        for i in range(len(self.nums)):
            removeidx = randrange(len(aux))
            self.num[i] = aux.pop(removeidx)
        return self.nums

    # O(N) Time
    def shuffle(self):
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.array

        # Your Solution object will be instantiated and called as such:
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
