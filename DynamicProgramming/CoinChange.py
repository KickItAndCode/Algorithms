"""
Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1

5 + 1+1+1+1+1

5+5

10

With 1 coin being the minimum amount.

"""


from nose.tools import assert_equal


def rec_coin(target, coins):

    # default value set to target
    min_coins = target

    # base case to check if target is in coin values list
    if target in coins:
        return target

    else:

        # for every coin value that is <= my target value
        for i in [c for c in coins if c <= target]:

            # add a coin count (1) + recursive call which is a new target - the current coin
            num_coins = 1 + rec_coin(target - i, coins)

            # reset min if the new num coins is less than the min coins
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


rec_coin(10, [1, 5])


def rec_coin_dynam(target, coins, known_results):

    # default value
    min_coins = target

    # base cases
    if target in coins:
        known_results[target] = 1
        return 1

    # return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # for every coin value that is <= target
        for i in [c for c in coins if c <= target]:

            # recursive call adding a coin count and using the new target
            num_coins = 1 + rec_coin_dynam(target - i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins

                # reset the known resulting
                known_results[target] = min_coins

    return min_coins


def coin_change(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # loop over all values to target to build dp array
    for i in range(1, amount + 1):

        # find best options for that position

        # loop over each coin option
        for coin in coins:
            if coin <= i:
                dp[i] = min(1 + dp[i - coin], dp[i])
    return dp[amount] if dp[amount] != float("inf") else -1


class TestCoins(object):

    def check(self, solution):
        coins = [1, 5, 10, 25]
        # assert_equal(solution(45, coins), 3)
        # assert_equal(solution(23, coins), 5)
        # assert_equal(solution(74, coins), 8)
        assert_equal(solution(10, [1, 2, 3, 5]), 2)
        assert_equal(solution(11, [1, 2, 5]), 3)
        print('Passed all tests.')
# Run Test


test = TestCoins()
test.check(coin_change)
