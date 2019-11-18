# 66. Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        elif digits[i] == 9:
            digits[i] = 0

    # otherwise all numbers are 9's
    res = [0] * len(digits) + 1
    res[0] = 1
    return res

# faster


def plusOne(digits):
    length = len(digits) - 1
    while digits[length] == 9:
        digits[length] = 0
        length -= 1
    if(length < 0):
        digits = [1] + digits
    else:
        digits[length] += 1
    return digits


print(plusOne([1, 2, 3]))
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

print(plusOne([4, 3, 2, 1]))
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
