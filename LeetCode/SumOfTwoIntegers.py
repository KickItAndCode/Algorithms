# 371. Sum of Two Integers
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = -2, b = 3
# Output: 1

# assuming no negative


def getSum2(a, b):

    # keep adding until we hae no carry left

    while b != 0:

        # get carry it will be shifted and stored in b later
        carry = a & b

        # ^ does the bit addition for us
        a = a ^ b

        # shift carry over 1 position because it will be added in the next iteration
        b = carry << 1

    return a

#


def getSum(a, b):
    # 32 bit int max and min
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    # mask to get the last 32 bits
    mask = 0xFFFFFFFF

    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)


def getSum3(a, b):
    if(b == 0):
        return a
    carry = (a & b) << 1
    sum = a ^ b
    return getSum3(sum, carry)


print(getSum3(1, 2))  # 3
print(getSum3(-2, 3))  # 1
