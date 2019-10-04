# 151. Reverse Words in a String

# Given an input string, reverse the string word by word.


# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words
# to a single space in the reversed string.

from nose.tools import assert_equal


def reverseWords(s):
    start = 0
    end = start

    words = []
    for i in range(len(s)):
        c = s[i]
        # if you have found a space then take start to end as a word
        if c == ' ':
            # if you have moved forward
            if end > start:
                words.append(s[start:end])
             # reset start and end to be right after the previous word
            start = end = i + 1
        else:
            end = i + 1

    # when you finish iterating throught the loop adjust end to get
    # the last word since there is no space to determine it
    end = len(s)
    if end > start:
        words.append(s[start:end])

    words.reverse()
    return ' '.join(words)


class TestReverse(object):

    def test_rev(self, solution):
        assert_equal(solution("a good   example"),
                     "example good a")
        assert_equal(solution("  hello world!  "),
                     "world! hello")
        assert_equal(solution("the sky is blue"),
                     "blue is sky the")

        print('PASSED ALL TEST CASES!')


# Run Tests
test = TestReverse()
test.test_rev(reverseWords)
