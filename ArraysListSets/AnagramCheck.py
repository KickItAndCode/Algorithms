from nose.tools import assert_equal

#"public relations" is an anagram of "crap built on lies."
#"clint eastwood" is an anagram of "old west action"

def anagram(s1,s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    counter = {}

    for letter in s1:
        if letter in counter:
            counter[letter] +=1
        else:
            counter[letter] = 1
    for letter in s2:
        if  letter in counter:
            counter[letter] -= 1
        else:
            return False

    for k in counter:
        if counter[k] != 0:
            return False

    return True

class AnagramTest(object):

    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL TEST CASES PASSED')

# Run Tests
t = AnagramTest()
t.test(anagram)
