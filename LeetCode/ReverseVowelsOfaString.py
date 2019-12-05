# 345. Reverse Vowels of a String
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


def reverseVowels(s):
    vowels = set(["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"])

    l, r = 0, len(s) - 1
    S = list(s)
    while l < r:
        # if both are vowels swap
        if S[l] in vowels and s[r] in vowels:
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        elif S[l] not in vowels:
            l += 1
        elif S[r] not in vowels:
            r -= 1
    return "".join(S)


print(reverseVowels("hello"))  # holle
print(reverseVowels("leetcode"))  # leotcede
