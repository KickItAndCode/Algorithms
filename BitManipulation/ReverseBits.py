# 190. Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.


# Example 1:

# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
# Example 2:

# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.


# Note:

# Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.


#  We first intitialize result to 0. We then iterate from
# 0 to 31 (an integer has 32 bits). In each iteration:
# We first shift result to the left by 1 bit.
# Then, if the last digit of input n is 1, we add 1 to result. To
# find the last digit of n, we just do: (n & 1)
# Example, if n=5 (101), n&1 = 101 & 001 = 001 = 1;
# however, if n = 2 (10), n&1 = 10 & 01 = 00 = 0).

# Finally, we update n by shifting it to the right by 1 (n >>= 1). This is because the last digit is already taken care of, so we need to drop it by shifting n to the right by 1.

# At the end of the iteration, we return result.
def reverseBits(self, n):
    reversed = 0
    for i in range(32):
        reversed = reversed << 1
        reversed |= (n >> i) & 0x1
    return reversed

 def reverseBits(self, n):
        res = 0
        for i in range(32):
            res += n & 1
            n = n >> 1
            if i != 31:
                res = res << 1
        return res
