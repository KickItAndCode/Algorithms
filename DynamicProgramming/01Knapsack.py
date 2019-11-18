# You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
# In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
# The first line consists of N the number of items.
# The second line consists of W, the maximum capacity of the knapsack.
# In the next line are N space separated positive integers denoting the values of the N items,
# and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.

# Output:
# For each testcase, in a new line, print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000
# 1 ≤ W ≤ 1000
# 1 ≤ wt[i] ≤ 1000
# 1 ≤ v[i] ≤ 1000

# Example:
# Input:
# 2
# 3
# 4
# 1 2 3
# 4 5 1
# 2
# 3
# 1 2 3
# 4 5 6
# Output:
# 3
# 1


# 0 1 2 3 4 5 6
# 0
# 1
# 2
# 3
def knapSack(capacity, wt, val, val_length):
    dp = [[0 for x in range(capacity + 1)] for x in range(val_length + 1)]

    for i in range(val_length+1):
        for w in range(capacity + 1):
            curr = i-1
            currVal = val[curr]
            currWeight = wt[curr]
            if i == 0 or capacity == 0:
                dp[i][w] = 0

            # if the current weight is greater than the current max weight
            # we can't use the current item so grab the one above it
            elif currWeight > w:
                dp[i][w] = dp[i-1][w]
            else:

                # logic to determine if we want to use the current value or not use it
                # use the current weight to determine what value would be in addition
                # to the current value
                withItem = currVal + dp[i-1][w - currWeight]
                withoutItem = dp[i-1][w]

                dp[i][w] = max(withItem, withoutItem)
    return dp[-1][-1]


val = [5, 3, 4]
wt = [3, 2, 1]
capacity = 5
val_length = len(val)
# print(knapSack(capacity, wt, val, val_length))
print(knapSack(5, [5, 3, 4, 2], [60, 50, 70, 30], 4))  # 80
