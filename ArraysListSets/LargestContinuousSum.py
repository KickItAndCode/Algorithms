# Given an array of integers (positive and negative)
# find the largest continuous sum.


from nose.tools import assert_equal


def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    # max=sum=arr[0] bug: TypeError: 'int' object is not callable. (Do not use the keyword!)
    max_num = sum = arr[0]

    for n in arr[1:]:
        sum = max(sum+n, n)
        max_num = max(sum, max_num)
    return max_num


# def large_cont_sum(arr):

#     if (len(arr) == 1):
#         return arr[1]

#     i, j = 0, 1
#     curr, res = arr[0], 0
#     length = len(arr)
#     while j <= length - 1 and i < length - 1:

#         curr = curr + arr[j]
#         res = max(res, curr)
#         j += 1

#         if j == length:
#             i += 1
#             j = i + 1
#             curr = arr[i]

#         res = max(res, curr)

#     return res


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([-1, 2, 8, -5, 3]), 10)
        assert_equal(sol([1, 2, -1, 3]), 5)
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(large_cont_sum)


# large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
