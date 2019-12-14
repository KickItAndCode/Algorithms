def squareRoot(k):
    l, r = 0, k
    while l <= r:
        mid = l + (r-l) // 2
        midSquared = mid * mid

        if midSquared <= k:
            l = mid + 1
        else:
            r = mid - 1

    return l - 1


print(squareRoot(4))
