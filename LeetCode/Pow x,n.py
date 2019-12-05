# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# x ^ n = (1/x) ^ (-n)
# x ^ (2n) = (x ^ n) * (x ^ n)

# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


# Few Simple Steps

# Check is n equals 0, since (any_number)^0 = 1. Hence return 1
# Check is n is a negative number, since (any_number)^(-3) = 1/(any_number)^3
# Check is n is an even number, since (any_number)^(2j) = (anynumber) * (anynumber) * (anynumber)^(2j/2)
# Otherwise (any_number)^(n) = (any_number)^(n-1) * (any_number)

def myPow(self, x: float, n: int) -> float:
    # return x**n

    if n == 0:
        return 1
    if n < 0:
        return 1/self.myPow(x, -n)
    if n % 2 == 0:
        return self.myPow(x*x, n/2)
    else:
        return self.myPow(x, n-1)*x


def myPow(self, x, n):
        return x ** n


def myPow(self, x, n):
    if not n:
        return 1
    if n < 0:
        return 1 / self.myPow(x, -n)
    if n % 2:
        return x * self.myPow(x, n-1)
    return self.myPow(x*x, n/2)


 def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

def myPow(x, n):
    # x**n == (1/x)**(-n)
    # by using the property above we can transform the negetive power problem to positive power problem
    # so that we solve the positive power situation, we also solved the negtive power situation.
    if n < 0:
        x = 1/x
        n = -n
    # We solve the positive power here:
    power = 1
    current_product = x
    while n > 0:
        # if n is odd numberm, we need to time x one more time
        if n % 2:
            power = power * current_product
        current_product = current_product * current_product
        n = n//2
    return power


print(myPow(2, 4))
print(myPow(2, -2))
