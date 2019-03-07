# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
from nose.tools import assert_equal


def uni_char3 (s):
    return len(set(s) == len(s))

def uni_char2(s):
    dict = {}
    for c in s:
        if c not in dict:
            dict[c] = True
        elif c in dict:
            return False
    return True

def uni_char(s):
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestUnique()
t.test(uni_char)
