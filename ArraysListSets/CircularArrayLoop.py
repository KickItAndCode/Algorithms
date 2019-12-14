# 457. Circular Array Loop
# You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

# Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.


# Example 1:

# Input: [2,-1,1,2,2]
# Output: true
# Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
# Example 2:

# Input: [-1,2]
# Output: false
# Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
# Example 3:

# Input: [-2,1,-1,-2,-2]
# Output: false
# Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.

def circularArrayLoop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    for i, num in enumerate(nums):
            # use a distinct marker for each starting point
        mark = str(i)

        # explore while node is new, direction is same, and is not self loop
        # note: if node has been marked by a different marker, no need to proceed. This gives O(n) time.
        while (type(nums[i]) == int) and (num * nums[i] > 0) and (nums[i] % len(nums) != 0):
            jump = nums[i]
            nums[i] = mark
            i = (i + jump) % len(nums)

        # if self loop, nums[i] is never marked
        # if nums[i] is marked, a cycle is found
        if nums[i] == mark:
            return True

    return False


print(circularArrayLoop([2, -1, 1, 2, 2]))  # true
print(circularArrayLoop([-1, 2]))  # false
print(circularArrayLoop([-2, 1, -1, -2, -2]))  # false
