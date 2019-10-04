# 739. Daily Temperatures

# Given a list of daily temperatures T, return a list such that,
# for each day in the input, tells you how many days you would
# have to wait until a warmer temperature. If there is no future
# day for which this is possible, put 0 instead.

# For example, given the list of temperatures
# T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
# [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range[1, 30000].
# Each temperature will be an integer in the range[30, 100].

from nose.tools import assert_equal

# O(n) time because in while you only check the top element of the stack


def dailyTemperatures(T):
    # out put array keeps track of days or difference of index from one day to another
    out = [0] * len(T)
    stack = []
    for i in range(0, len(T)):
        temp = T[i]

        # loop while top element of the stack exist and is less than temp
        while len(stack) > 0 and T[stack[-1]] < temp:
            # Get index of top stack
            oldIndex = stack[-1]
            # if the temp is greater than element at top of stack
            if temp > T[oldIndex]:
                out[oldIndex] = i - oldIndex
                stack.pop()
            else:
                break
        stack.append(i)
    return out


class DailyTemperaturesTest(object):

    def test(self, solution):

        assert_equal(solution([73, 74, 75, 71, 69, 72, 76, 73]), [
                     1, 1, 4, 2, 1, 1, 0, 0]
                     )
        print('All test cases passed.')


# Run Tests
t = DailyTemperaturesTest()
t.test(dailyTemperatures)
