from nose.tools import assert_equal

def permute(s):
    out = []

    if len(s) <= 1:
         out = [s]
    else:
        #for every letter in string
        for i, let in enumerate(s):
            # for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i +1:]):

                #print(f'curr letter is {let}')
                #print(f'perm is {perm}')
                #add it to the output
                out += [let+perm]
    return out



# print (permute('abc'))


class TestPerm(object):

    def test(self,solution):

        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )

        print ('All test cases passed.')



# Run Tests
t = TestPerm()
t.test(permute)
