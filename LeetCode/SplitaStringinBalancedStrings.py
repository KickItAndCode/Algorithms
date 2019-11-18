# 1221. Split a String in Balanced Strings

# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.


# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# Example 4:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

def balancedStringSplit(s):
    j, counter = 0, 0
    for i in range(len(s)):
        if s[i] == 'R':
            j += 1
        if s[i] == 'L':
            j -= 1
        if j == 0:
            counter += 1
    return counter
 def balancedStringSplit(s):
        w_count = l_count = r_count = 0
        for ch in s:
            if ch == "L":
                l_count += 1
            else:
                r_count += 1
                
            if l_count == r_count:
                w_count += 1
        return w_count

print(balancedStringSplit("RLRRLLRLRL"))  # 4
