# 38. Count and Say
# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.
# the nth term is the read-off of the (n - 1)th term

# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 4
# Output: "1211"

# Idea here is keep track of the first letter in the sequence and count consecutive occurances. Once you encounter a new letter you add the previous count and letter to the chain. Repeat n-1 times (since we seeded the initial '1' case). We always update temp after the inner loop since we will never have already added the last sequence.


def countAndSay(n):
    s = '1'
    for i in range(n-1):
        let, temp, count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count) + let
                let = l
                count = 1
        temp += str(count) + let
        s = temp
    return s


print(countAndSay(8))
