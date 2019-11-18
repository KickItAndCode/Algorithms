# 844. Backspace String Compare
# # means a backspace character.
# Given two strings S and T, return if they are equal when both are typed into empty text editors.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".


def backspaceCompare(S, T):
    return helper([], S) == helper([], T)


def helper(stack, S):
    stack = []
    for c in S:
        if c != "#":
            stack.append(c)
        elif stack:
            stack.pop()
    return stack


# true Explanation: Both S and T become "ac".
print(backspaceCompare("ab#c", "ad#c"))

# true Explanation: Both S and T become "".
print(backspaceCompare("ab##", "c#d#"))

# false Explanation: S becomes "c" while T becomes "b".
print(backspaceCompare("a#c", "b"))
