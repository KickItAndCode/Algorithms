# 921. Minimum Add to Make Parentheses Valid

# Given a string S of '(' and ')' parentheses, we add the
#  minimum number of parentheses ( '(' or ')', and in any
# positions ) so that the resulting parentheses string is valid.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A
#  and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number
# of parentheses we must add to make the resulting string valid.


# Example 1:

# Input: "())"
# Output: 1
# Example 2:

# Input: "((("
# Output: 3
# Example 3:

# Input: "()"
# Output: 0
# Example 4:

# Input: "()))(("
# Output: 4
from nose.tools import assert_equal


def minAddToMakeValid(S):

    stack = []
    count = 0
    for s in S:
        if s == ')':
            # if the top of the stack is opening its a match so remove it
            if len(stack) > 0 and stack[len(stack) - 1] == '(':
                del stack[len(stack)-1]
            # otherwise not a match
            else:
                count += 1
        else:
            stack.append(s)
    for s in stack:
        count += 1
    return count


class MinAddToMakeValidTest(object):

    def test(self, solution):

        assert_equal(solution("())"), 1)
        assert_equal(solution("((("), 3)
        assert_equal(solution("()"), 0)
        assert_equal(solution("()))(("), 4)

        print('All test cases passed.')


# Run Tests
t = MinAddToMakeValidTest()
t.test(minAddToMakeValid)
