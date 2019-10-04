from nose.tools import assert_equal


def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)


# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):

    # Base CASES
    if n == 1 or n == 0:
        return n
    # Check cache

    if cache[n] != None:
        return cache[n]

    # keep setting Caching
    cache[n] = fib_dyn(n-1) + fib_dyn(n - 2)
    # return nth number on Cache
    return cache[n]


# fib_dyn(10)


def fib_iter2(n):

    i = 1
    a = 0
    b = 1
    c = None

    while i < n:

        c = a + b
        a = b
        b = c

        i += 1
    return c

# method using tuple unpacking


def fib_iter(n):

    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b

    return a


# fib_iter(23)

#fib (n-1) +  fib(n+2)
# 0 1 1 2 3 5 8 13 21


class TestFib(object):

    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)
        print('Passed all tests.')


# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

# t.test(fib_rec)
# t.test(fib_dyn)
t.test(fib_iter)
