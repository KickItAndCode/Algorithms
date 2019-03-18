from nose.tools import assert_equal

def reverse2(s):

    end = len(s) -1
    res = []
    return reverse_helper(s, end, res)

def reverse_helper(s, end, res):
    if end < 0:
        return ''.join(res)
    else:
        res.append(s[end])
        return reverse_helper(s, end -1, res)

def reverse(s):
    if len(s) <=  1:
        return s

    return reverse(s[1:]) + s[0]



class TestReverse(object):

    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')

        print 'PASSED ALL TEST CASES!'

# Run Tests
test = TestReverse()
test.test_rev(reverse)

reverse('hello world')
