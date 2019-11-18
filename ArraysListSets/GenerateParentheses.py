# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


# Approach 2 (Directed Backtracking)

# The 3 Keys To Backtracking

# Our Choice:
# Whether we place a left or right paren at a certain decision point in our recursion.

# Our Constraints:
# We can't place a right paren unless we have left parens to match against.

# Our Goal:
# Place all k left and all k right parens.


# The Key

# At each point of constructing the string of length 2k we make a choice.

# We can place a "(" and recurse or we can place a ")" and recurse.

# But we can't just do that placement, we need 2 critical pieces of information.

# The amount of left parens left to place.
# The amount of right parens left to place.

# We have 2 critical rules at each placement step.

# We can place a left parentheses if we have more than 0 left to place.

# We can only place a right parentheses if there are left parentheses that we can match against.

# We know this is the case when we have less left parentheses to place than right parentheses to place.

# Once we establish these constraints on our branching we know that when we have 0 of both parens to place that we are done, we have an answer in our base case.

def generateParenthesis(n):
    def generate(res, left, right, curr):

        if left == 0 and right == 0:
            res.append(curr)

        # At each frame of the recursion we have 2 things we can do:
        # 1.) Insert a left parenthesis
        # 2.) Insert a right parenthesis
        # These represent all of the possibilities of paths we can take from this
        # respective call. The path that we can take all depends on the state coming
        # into this call.

        # Can we insert a left parenthesis? Only if we have lefts remaining to insert
        # at this point in the recursion

        if left > 0:
            generate(res, left - 1, right, curr + "(")

        # Can we insert a right parenthesis? Only if the number of left parens needed
        # is less than then number of right parens needed.

        # This means that there are open left parenthesis to close OTHERWISE WE CANNOT
        # USE A RIGHT TO CLOSE ANYTHING. We would lose balance.
        if left < right:
            generate(res, left, right - 1, curr + ")")

        # numLeftParensNeeded ->           We did not use a left paren
        # numRightParensNeeded - 1 ->      We used a right paren
        # parenStringInProgress + ")" ->   We append a right paren to the string in progress
        # result  ->                        Just pass the result list along for the next call to use

    res = []
    generate(res, n, n, '')
    return res


print(generateParenthesis(3))
