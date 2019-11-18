from nose.tools import assert_equal


def permuteGeeksForGeeks(s):

    def permuteHelper(res, l, r):
        if l == r:
            print(''.join(res))

        else:
            for i in range(l, r + 1):
                res[l], res[i] = res[i], res[l]
                permuteHelper(res, l+1, r)
                res[l], res[i] = res[i], res[l]

    permuteHelper(list(s), 0, len(s) - 1)


# permuteGeeksForGeeks("ABC")


def permute(s):
    out = []

    if len(s) <= 1:
        out = [s]
    else:
        # for every letter in string
        for i, let in enumerate(s):
            # for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i + 1:]):

                # print(f'curr letter is {let}')
                # print(f'perm is {perm}')
                # add it to the output
                out += [let+perm]
                # print(f'Output is: {out}')
    return out


def permute2(s):
    res = []

    if len(s) == 1:
        return [s]

    # get all permuations of length n -1
    perms = permute2(s[1:])

    # current char
    char = s[0]

    # go through each options without the curr char
    for perm in perms:
        # get result for each index
        # essentially before mid and after
        for i in range(len(perm) + 1):
            res.append(perm[:i] + char + perm[i:])
    return res


# print (permute('abc'))


class TestPerm(object):

    def test(self, solution):

        assert_equal(sorted(solution('abc')), sorted(
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(
            ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print('All test cases passed.')


# Run Tests
t = TestPerm()
t.test(permute)
