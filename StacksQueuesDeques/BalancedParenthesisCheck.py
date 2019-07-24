from nose.tools import assert_equal


def balance_check2(s):

    # Check is even number of brackets
    if len(s)%2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([ ('(',')'), ('[',']'), ('{','}') ])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for paren in s:

        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)

        else:

            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False

            # Check the last open parenthesis
            last_open = stack.pop()

            # Check if it has a closing match
            if (last_open,paren) not in matches:
                return False

    return len(stack) == 0

def balance_check(s):
    open= ['[','(', '{']
    close = [']', '}', ')']
    stack = []
    for c in s:
        if c in open:
            stack.append(c)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    return len(stack) == 0


balance_check('[]') #True
balance_check('[](){([[[]]])}') #True
balance_check('()(){]}') #False




class TestBalanceCheck(object):

    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print  ('ALL TEST CASES PASSED')

# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
