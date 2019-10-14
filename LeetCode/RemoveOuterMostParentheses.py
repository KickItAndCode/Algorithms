# 1021. Remove Outermost Parentheses
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.


# Example 1:

# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".


# Note:

# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string

from nose.tools import assert_equal


def removeOuterParentheses(S):
	parts = []
    left_n = 0
    right_n = 0

    # [j+1:i] will be slice getting parts without beginning and end
    j = 0  

    for i in range(len(S)):
        if S[i] == "(":
            left_n += 1  # add 1 when left parenthesis
        else:
            right_n += 1  # add 1 when right

        if left_n == right_n:
            parts.append(S[j + 1:i])  # add part when left_n = right_n
            j = i + 1  # because next first item will be cut, i + 1 gives j += 2 total

class removeOuterParenthesesTest (object):

    def test(self, sol):
        assert_equal(sol("(()())(())"),  "()()()")
        assert_equal(sol("(()())(())(()(()))"), "()()()()(())")

        print("ALL TEST CASES PASSED")


# Run and test
t = removeOuterParenthesesTest()
t.test(removeOuterParentheses)
