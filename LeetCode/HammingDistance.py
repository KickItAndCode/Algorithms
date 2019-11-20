# 461. Hamming Distance
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.


def hammingDistance(x, y):
    res = 0
    while x > 0 or y > 0:
        # x % 2 will gives us last digit in binary
        # so xor that with the last from x

        res += (x % 2) ^ (y % 2)
        x >>= 1
        y >>= 1
    return res
    # then chop off last digit of both and continue the loop
