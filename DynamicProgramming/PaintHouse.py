# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.

# Input: [[1,2,3],[1,4,6]]
# Output: 3
# R   B   G
# [14, 2, 11]
# [11, 14, 5]
# [14, 3, 10]


# start with the second row and use the cost from the row above it
# add the min value from the non selected color row above it
# if you are on the red row you can only select the min from b, g
# do this for each index in the row
# take the min of the bottom row to find the min cost
def minCost(costs):
    if not costs:
        return 0

    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])

    return min(min(costs[len(costs)-1][0], costs[len(costs)-1][1]), costs[len(costs)-1][2])


print(minCost([[14, 2, 11], [11, 14, 5], [14, 3, 10]]))  # 10
print(minCost([[1, 2, 3], [1, 4, 6]]))  # 3
