
# 125. Valid Palindrome
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as
#  valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

# This problem can have whitespace and other characters
# This problem can be solved by checking if the character is a valid char
# then adding it to a list and changing the case to lower case
# then check if the oroginal char array is equal to the char array in reverse

from nose.tools import assert_equal


def isPalindrome(s):
    if not s:
        return True

    char = []

    for i in s:
        if i.isalnum():
            char.append(i.lower())

    return char == char[::-1]


def isPalindrome2(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if i < j and not s[i].isalnum():
            i += 1
        elif i < j and not s[j].isalnum():
            j -= 1

        if i < j and s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


class IsPalindromeTest(object):

    def test(self, solution):

        assert_equal(solution("A man, a plan, a canal: Panama"), True)
        assert_equal(solution("race a car"), False)
        print('All test cases passed.')


# Run Tests
t = IsPalindromeTest()
# t.test(isPalindrome)
t.test(isPalindrome2)
