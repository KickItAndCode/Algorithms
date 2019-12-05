# 191. Number of 1 Bits
# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).


# Example 1:

# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:

# Input: 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


# Note:

# Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.


# The solution is straight-forward. We check each of the 3232 bits of the number. If the bit is 11, we add one to the number of 11-bits.

# We can check the i^{th}i
# th
#   bit of a number using a bit mask. We start with a mask m=1m=1, because the binary representation of 11 is,

# 0000 0000 0000 0000 0000 0000 0000 000100000000000000000000000000000001 Clearly, a logical AND between any number and the mask 11 gives us the least significant bit of this number. To check the next bit, we shift the mask to the left by one.

# 0000 0000 0000 0000 0000 0000 0000 001000000000000000000000000000000010

# And so on.

def hammingWeight(n):

    count = 0
    mask = 1
    for i in range(32):
        # check the result of and it with the mask
        if ((n & mask) != 0):
            count += 1
        # shift the placement of the 1 all the way to the end
        mask <<= 1
    return count


print(hammingWeight(4))
