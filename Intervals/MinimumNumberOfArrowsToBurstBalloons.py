

# 452. Minimum Number of Arrows to Burst Balloons
# There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

# Example:

# Input:
# [[10,16], [2,8], [1,6], [7,12]]

# Output:
# 2

# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

def findMinArrowShots(points):
    # Sort by left cordinate, then by width
    sorted_points = sorted(points, key=lambda x: (x[1], x[1] - x[0]))
    last_shot = -float('inf')
    shot_count = 0

    for baloon in sorted_points:
        if baloon[0] > last_shot:
            last_shot = baloon[1]
            shot_count += 1

    return shot_count


def findMinArrowShots(points):
    points = sorted(points, key=lambda x: x[1])
     arrow = float('-inf')
      res = 0
       for l, r in points:
            if l > arrow:
                res += 1
                arrow = r
        return res


print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
