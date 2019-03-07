# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to
# become 'A4B4C5D2E4'. For this problem, you can falsely "compress"
# strings of single or double letters. For instance, it is okay for
# 'AAB' to return 'A2B1' even though this technically takes more space.
#
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

import collections
from nose.tools import assert_equal



def compress (s):
    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    #Intialize Values
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            # the previous char and the current count then reset
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r


# this solution doesn't preserver order because dicts aren't guarateed
def compress2(s):
    dict = collections.defaultdict(int)

    for c in s:
        dict[c] += 1

    result = []
    for key, value in dict.items():
        result.append(key)
        result.append(str(value))
    return "".join(result)

print (compress('AAAAABBBBCCCC'))


class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestCompress()
t.test(compress)
