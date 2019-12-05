# def sum_func(n):
#     if len(str(n)) == 1:
#         return n

#     else:
#         return n % 10 + sum_func(n//10)


def sum_func(n):
    if (len(str(n)) == 0):
        return n
    else:
        curr = n % 10
        newN = n // 10
        return curr + sum_func(newN)


def sum_func2(n):
    res = 0
    if n < 0:
        n *= -1
    while n > 0:
        res += n % 10
        n //= 10

    return res


# print(sum_func2(4321))
print(sum_func2(-4321))
