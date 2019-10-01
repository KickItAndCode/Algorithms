from nose.tools import assert_equal


def rev_word2(s):
    return " ".join(reversed(s.split()))


def rev_word(s):
    length = len(s)
    words = []
    i = 0
    space = [' ']

    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])

        i += 1
    return " ".join(custom_reverse(words))


def custom_reverse_(words):
    result = []

    i = len(words) - 1

    while i >= 0:
        result.append(words[i])
        i -= 1
    return result


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '),
                     'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word)


# print(rev_word('Hi John,   are you ready to go?'))
# print(rev_word('    space before   awesome'))
