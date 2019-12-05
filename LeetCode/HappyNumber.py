# 202. Happy Number
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# grab last digits and get its square and chop it off the int
# and add that to the previous until the number is zero

# continue this process until you find a 1 or end up in a cycle
# track seen sums with a set


def isHappy(n):
    seen = set()
    while n != 1:
        current = n
        sum = 0
        while current != 0:
            sum += (current % 10) * (current % 10)
            current //= 10

        if sum in seen:
            return False

        seen.add(sum)
        n = sum

    return True


print(isHappy(19))
