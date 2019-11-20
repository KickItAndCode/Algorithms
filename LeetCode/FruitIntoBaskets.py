# 904. Fruit Into Baskets
# In a row of trees, the i-th tree produces fruit with type tree[i].

# You start at any tree of your choice, then repeatedly perform the following steps:

# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

# What is the total amount of fruit you can collect with this procedure?


# Example 1:

# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# Example 2:

# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# Example 3:

# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:

# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.


# Note:

# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length

# this question is masked and is really longest substring with at most two character
# two pointers and continue while we can pick fruit
# then when we get
from collections import defaultdict, Counter


def totalFruit1(tree):
    res, i = 0, 0
    count = Counter()
    for j, val in enumerate(tree):
        count[val] += 1
        while len(count) > 2:
            count[tree[i]] -= 1
            if count[tree[i]] == 0:
                del count[tree[i]]
            i += 1
        res = max(res, j-i + 1)
    return res


# The problem is equivalent to finding the longest contiguous subarray with at most two distinct numbers. We initialize two pointers i and j to be 0. We iterate i over range(len(tree)), and keep a dictionary dic of numbers in tree[j:i+1]. Once len(dic) > 2, we move j to the right until len(dic) == 2. The longest contiguous subarray ending with tree[i] and with at most two distinct numbers is then i-j+1. The maximum of i-j+1 over all i gives the desired value of the problem.

# The time complexity is O(n), and the space complexity is O(1).
def totalFruit2(tree):

    j = 0
    dic = defaultdict(int)
    maxlen = -float('inf')
    for i in range(len(tree)):
        if tree[i] in dic:
            dic[tree[i]] += 1
        while len(dic) > 2:
            dic[tree[j]] -= 1
            if dic[tree[j]] == 0:
                del dic[tree[j]]
            j += 1
        maxlen = max(maxlen, i-j+1)
    return maxlen if maxlen != -float('inf') else 0


def totalFruit3(tree):
    result = 0
    l = r = -1
    mem = defaultdict(int)

    while r < len(tree):
        while len(mem) <= 2:  # valid
            result = max(result, sum(mem.values()))

            r += 1
            if r == len(tree):
                return result

            mem[tree[r]] += 1

        while len(mem) > 2:  # solution invalid
            l += 1

            mem[tree[l]] -= 1
            if mem[tree[l]] == 0:
                del mem[tree[l]]

    return result


print(totalFruit1([1, 2, 1]))  # 3 We can collect [1,2,1].
# 3 We can collect [1,2,2]. #If we started at the first tree, we would only collect [0, 1].
print(totalFruit1([0, 1, 2, 2]))
print(totalFruit1([1, 2, 3, 2, 2]))  # 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# 5 Explanation: We can collect [1,2,1,1,2].
print(totalFruit1([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
