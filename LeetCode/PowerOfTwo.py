# 231. Power of Two

# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false


def isPowerOfTwo(n):
    res = 1
    while res < n:
        res *= 2
    return res == n


def isPowerOfThree(self, n: int) -> bool:
    while n % 3 == 0 and n != 0:
        n /= 3
    return n == 1
    # this solution takes advantage that the high integer in
    # The tricky one, if 3^19 is divisible by n, n must be its factor: 3^i, i =0,1,2 ... 19


 def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0

print(isPowerOfTwo(20))  # false
print(isPowerOfTwo(16))  # true
