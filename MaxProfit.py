# 121. Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the
# price of a given stock on day i.

# If you were only permitted to complete at most one
# transaction(i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6),
# profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max
# profit = 0.

from nose.tools import assert_equal


# Brute force solution is to compare each number with each other number
# this would result in O(n)^2 time


# One pass O(n)
# By keeping track of the minimum buy and the max  profit
# then comparing to the current profit and update each value throughout
# you can find the max profit in one pass

def maxProfitFast(prices):
    max_profit, min_buy = 0, float('inf')
    for price in prices:
        # current profit if compared to the curr min buy price
        curr_profit = price-min_buy

        # if the current price is less than the curr min buy price
        # then update the min buy
        min_buy = min(min_buy, price)

        # update max profit if the current profit is greater than the previous
        max_profit = max(max_profit, curr_profit)
    return max_profit


class MaxProfitTest(object):

    def test(self, sol):
        assert_equal(sol([7, 1, 5, 3, 6, 4]), 5)
        assert_equal(sol([7, 6, 4, 3, 1]), 0)
        print("ALL TEST CASES PASSED")


# Run and test
t = MaxProfitTest()
t.test(maxProfitFast)
