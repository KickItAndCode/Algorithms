# 693. Binary Number with Alternating Bits
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.


def hasAlternatingBits(n):
    last = n % 2
    n >>= 1
    while n > 0:
        curr = n % 2
        n >>= 1
        if curr == last:
            return False
        last = curr
    return True


print(hasAlternatingBits(5))  # true The binary representation of 5 is: 101
print(hasAlternatingBits(7))  # false The binary representation of 7 is: 111.
print(hasAlternatingBits(11))  # false The binary representation of 11 is: 1011
print(hasAlternatingBits(10))  # true The binary representation of 10 is: 1010.
