# 6. ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Approach 2: Visit by Row
# Intuition

# Visit the characters in the same order as reading the Zig-Zag pattern line by line.

# Algorithm

# Visit all characters in row 0 first, then row 1, then row 2, and so on...

# For all whole numbers kk,

# Characters in row 00 are located at indexes k \; (2 \cdot \text{numRows} - 2)k(2⋅numRows−2)
# Characters in row \text{numRows}-1numRows−1 are located at indexes k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1k(2⋅numRows−2)+numRows−1
# Characters in inner row ii are located at indexes k \; (2 \cdot \text{numRows}-2)+ik(2⋅numRows−2)+i and (k+1)(2 \cdot \text{numRows}-2)- i(k+1)(2⋅numRows−2)−i.

# Complexity Analysis

# Time Complexity: O(n)O(n), where n == \text{len}(s)n==len(s). Each index is visited once.
# Space Complexity: O(n)O(n). For the cpp implementation, O(1)O(1) if return string is not considered extra space.


def convert(s, numRows):
    if numRows == 1:
        return s

    n = len(s)
    cycle = 2 * numRows - 2

    strlist = []
    for i in range(numRows):
        # loop from i to length using the cycle  to skip rows
        for j in range(i, n, cycle):
            strlist.append(s[j])

            if i != numRows - 1 and i != 0 and j + cycle - 2 * i < n:
                strlist.append(s[j + cycle - 2 * i])
    newStr = ''.join(strlist)
    return newStr

# https://leetcode.com/problems/zigzag-conversion/discuss/3417/A-10-lines-one-pass-o(n)-time-o(1)-space-accepted-solution-with-detailed-explantation

 def convert(self, s, numRows):
        if numRows<=1: return s
        cycle, slen, res = numRows*2 - 2, len(s), ""
        for i in xrange(numRows):
            for j in xrange(i, slen, cycle):
                res += s[j]
                secondJ = (j - i) + cycle - i
                if (secondJ-j) % cycle != 0 and secondJ < slen:
                    res += s[secondJ]
        return res
