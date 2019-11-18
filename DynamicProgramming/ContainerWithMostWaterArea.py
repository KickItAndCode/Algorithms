# 11. Container With Most Water

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# you are given an array of integers. Each non zero integer represetns the height of a pillar of width 1


# solution concept

# The idea is that we start the "walls" of our container on the leftmost and rightmost pole. Then we need to move the left and right wall to hopefully make them bigger:

# If the left side is smaller than the right side, we move the left side forward.
# Otherwise we move the right side back.
# We stop when it's not possible to move any. As we do this, we keep track of the max volume we've seen.

# This problem follows a very similar pattern than the 3-SUM problem where we need to move two pointers to meet some requirement.
def maxArea(height):
    area, left, right = 0, 0, len(height) - 1

    while left < right:
        area = max(area, min(height[right], height[left]) * (right - left))
        # update the walls of the container looking for larger walls

        if height[left] < height[right]:  # left wall is the smallest
            left += 1
        else:
            right -= 1

    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
