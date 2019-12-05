# 680. Valid Palindrome II
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


def validPalindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return isPalindrome(s, i + 1, j) or isPalindrome(s, i, j-1)
        i += 1
        j -= 1
    return True


def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# too slow


def validPalindrome3(s):
    if isPalindrome3(s):
        return True
    else:
        for i in range(len(s)):
            if isPalindrome3(s[:i] + s[i+1:]):
                return True
    return False


def isPalindrome3(s):
    if not s:
        return True

    char = []

    for i in s:
        if i.isalnum():
            char.append(i.lower())

    return char == char[::-1]


# print(validPalindrome("aba"))  # true
print(validPalindrome("abca"))  # true
print(validPalindrome("deeee"))  # true
