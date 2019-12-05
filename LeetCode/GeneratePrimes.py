def generatePrimes(n):
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n ** 0.5)+1):
        if is_prime[i]:
            is_prime[i*i: n: i] = [False] * len(is_prime[i*i: n: i])

    res = [i for i, x in enumerate(is_prime) if x]
    return res

# better


def generatePrimes2(n):

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for p in range(2, n + 1):
        if is_prime[p] == True:
            primes.append(p)
            for j in range(p * 2, n + 1, p):
                is_prime[j] = False
    return primes


print(generatePrimes2(18))
print(generatePrimes2(5))
