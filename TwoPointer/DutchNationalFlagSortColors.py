# 75. Sort Colors
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

# In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
# a) arr[l..i] elements less than pivot.
# b) arr[i+1..j-1] elements equal to pivot.
# c) arr[j..r] elements greater than pivot


# The idea of solution is to move curr pointer along the array, if nums[curr] = 0 - swap it with nums[p0], if nums[curr] = 2 - swap it with nums[p2].

# Algorithm

# Initialise the rightmost boundary of zeros : p0 = 0. During the algorithm execution nums[idx < p0] = 0.

# Initialise the leftmost boundary of twos : p2 = n - 1. During the algorithm execution nums[idx > p2] = 2.

# Initialise the index of current element to consider : curr = 0.

# While curr <= p2 :

# If nums[curr] = 0 : swap currth and p0th elements and move both pointers to the right.

# If nums[curr] = 2 : swap currth and p2th elements. Move pointer p2 to the left.

# If nums[curr] = 1 : move pointer curr to the right.

def sortColors(nums):

    # for all idx < p0 : nums[idx < p0] = 0
    # curr is an index of element under consideration
    p0 = curr = 0
    # for all idx > p2 : nums[idx > p2] = 2
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1


print(sortColors([2, 0, 2, 1, 1, 0]))  # Output: [0,0,1,1,2,2]
