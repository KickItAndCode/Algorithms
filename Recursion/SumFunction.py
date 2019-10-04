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


print(sum_func(4321))
