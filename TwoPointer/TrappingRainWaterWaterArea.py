# 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of rain water(blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6


# easiest to understand

def trap2(bars):
    if not bars or len(bars) < 3:
        return 0

    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]

    while left < right:

        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)

        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1

        else:
            volume += r_max - bars[right]
            right -= 1
    return volume


def trap(height):

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
def trap1(arr):
    height, left, right, water = [], 0, 0, 0
    for i in arr:
        left = max(left, i)
        height.append(left)
    height.reverse()
    for n, i in enumerate(reversed(arr)):
        right = max(right, i)
        water += min(height[n], right) - i
    return water


# print(trap([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))  # 48
# print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap2([0, 3, 1, 2, 1, 0, 3, 1]))
