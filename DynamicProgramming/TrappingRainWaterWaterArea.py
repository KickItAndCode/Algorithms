# 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of rain water(blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxes = [0] * len(height)
    leftMax = 0
    for i in range(len(height)):
        currHeight = height[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, currHeight)

    rightMax = 0
    for i in reversed(range(len(height))):
        currHeight = height[i]
        minHeight = min(rightMax, maxes[i])
        if currHeight < minHeight:
            maxes[i] = minHeight-currHeight

        else:
            maxes[i] = 0

        rightMax = max(rightMax, currHeight)

    # containers the water after all this
    return sum(maxes)


# leet code solution
def trap(self, arr):
    height, left, right, water = [], 0, 0, 0
    for i in arr:
        left = max(left, i)
        height.append(left)
    height.reverse()
    for n, i in enumerate(reversed(arr)):
        right = max(right, i)
        water += min(height[n], right) - i
    return water


print(trap([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))  # 48
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
