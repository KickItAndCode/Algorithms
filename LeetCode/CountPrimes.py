# 204. Count Primes
# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


def countPrimes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, n):
        if is_prime[i] == True:
            for j in range(2, (n-1) // i + 1):
                is_prime[i*j] = False
    return sum(is_prime)


def countPrimes(n):
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5)+1):
        if is_prime[i]:
            is_prime[i*i: n: i] = [False] * len(is_prime[i*i: n: i])

    return sum(is_prime)


print(countPrimes(10))
