# 1011. Capacity To Ship Packages Within D Days
# A conveyor belt has packages that must be shipped from one port to another within D days.

# The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.


# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation:
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# Example 2:

# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6
# Explanation:
# A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# Example 3:

# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1


# Note:

# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500


# # Information on how to answer this problem

# The intuition for this problem, stems from the fact that

# a) Without considering the limiting limiting days D, if we are to solve, the answer is simply max(a)
# b) If max(a) is the answer, we can still spend O(n) time and greedily find out how many partitions it will result in.

# [1,2,3,4,5,6,7,8,9,10], D = 5

# For this example, assuming the answer is max(a) = 10, disregarding D,
# we can get the following number of days:
# [1,2,3,4] [5] [6] [7] [8] [9] [10]

# So by minimizing the cacpacity shipped on a day, we end up with 7 days, by greedily chosing the packages for a day limited by 10.

# To get to exactly D days and minimize the max sum of any partition, we do binary search in the sum space which is bounded by [max(a), sum(a)]

# Binary Search Update:
# One thing to note in Binary Search for this problem, is even if we end up finding a weight, that gets us to D partitions, we still want to continue the space on the minimum side, because, there could be a better minimum sum that still passes <= D paritions.

# In the code, this is achieved by:

# if res <= d:
#      hi = mid
# With this check in place, when we narrow down on one element, lo == hi, we will end up with exactly the minimum sum that leads to <= D partitions.


def shipWithinDays(weights, D):
    low, high = max(weights), sum(weights)
    while low < high:
        # guess the capacity of ship
        mid = (low+high)//2

        cur_cap = 0  # loaded capacity of current ship
        num_ship = 1  # number of ship needed

        #----simulating loading the weight to ship one by one----#
        for w in weights:
            cur_cap += w
            if cur_cap > mid:  # current ship meets its capacity
                cur_cap = w
                num_ship += 1
        #---------------simulation ends--------------------------#

        # we need too many ships, so we need to increase capacity to reduce num of ships needed
        if num_ship > D:
            low = mid+1
        # we are able to ship with good num of ships, but we still need to find the optimal max capacity
        else:
            high = mid

    return low


print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
