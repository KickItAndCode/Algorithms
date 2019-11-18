# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


def reverse(x):

    negative = False
    if x < 0:
        negative = True
        x *= -1

    rev = 0
    while x > 0:
        rev = (rev * 10) + (x % 10)
        x //= 10

    if rev > 0x7FFFFFFF:
        return 0

    return rev if not negative else (-1 * rev)


def reverse2(x):

    if x > 0:  # handle positive numbers
        a = int(str(x)[::-1])
    if x <= 0:  # handle negative numbers
        a = -1 * int(str(x*-1)[::-1])
    # handle 32 bit overflow
    mina = -2**31
    maxa = 2**31 - 1
    if a not in range(mina, maxa):
        return 0
    else:
        return a


print(reverse2(123))  # 321
print(reverse2(-123))  # -321
