from nose.tools import assert_equal
from collections import defaultdict
# "public relations" is an anagram of "crap built on lies."
# "clint eastwood" is an anagram of "old west action"


# def anagram(s1, s2):

#     s1 = s1.replace(' ', '').lower()
#     s2 = s2.replace(' ', '').lower()

#     if len(s1) != len(s2):
#         return False

#     counter = {}

#     for letter in s1:
#         if letter in counter:
#             counter[letter] += 1
#         else:
#             counter[letter] = 1
#     for letter in s2:
#         if letter in counter:
#             counter[letter] -= 1
#         else:
#             return False

#     for k in counter:
#         if counter[k] != 0:
#             return False

#     return True


def anagram(s1, s2):

    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    map = {}
    for n in s1:
        if n in map:
            map[n] += 1
        else:
            map[n] = 1

    for n in s2:
        if n in map:
            map[n] -= 1
        else:
            return False

    for k, v in map.items():
        if v != 0:
            return False

    return True


def anagram2(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    map = defaultdict(int)
    for i in range(len(s1)):
        map[s1[i]] += 1
        map[s2[i]] -= 1

    for k, v in map.items():
        if v != 0:
            return False
    return True


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        assert_equal(sol('clint eastwood', 'old west action'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t = AnagramTest()
t.test(anagram2)
