# 67. Add Binary
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


def addBinary(a, b):
    res = ''
    carry = 0
    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        res += str(carry % 2)
        carry //= 2

    return res[::-1]


def addBinary2(a, b):
    result = ''
    index = 0

    carry = '0'
    while index < max(len(a), len(b)) or carry == '1':

        # gets value from the back of A or B array minus the index
        # if the index is in range othersize use 0
        num_a = a[-1 - index] if index < len(a) else '0'
        num_b = b[-1 - index] if index < len(b) else '0'

        # add values including any carry over
        val = int(num_a) + int(num_b) + int(carry)

        # result is the prev result plus curr val converted to a string
        result = str(val % 2) + result

        # carry over a 1 if the value is greater than 1
        carry = '1' if val > 1 else '0'

        # increment index
        index += 1

    return result


print(addBinary("11", "1"))  # 100
print(addBinary("1010", "1011"))  # "10101"
print(addBinary2("11", "1"))  # 100
print(addBinary2("1010", "1011"))  # "10101"
