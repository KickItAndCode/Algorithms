#  # 557 Reverse Words in a String III

#  Given a string, you need to reverse the order of characters in each
# word within a sentence while still preserving whitespace and initial
#  word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there
#  will not be any extra space in the string.


# "take two"
# "ekat owt"

def reverseWords(self, s: str) -> str:
    list = s.split()
    newWords = [word[::-1] for word in list]
    return " ".join(newWords)


def reverseWords(self, s: str) -> str:
    new_s = ""
    start = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            new_s += self.reverse(s[start:i])+" "
            start = i+1
        elif i+1 == len(s):
            new_s += self.reverse(s[start:i+1])

    return(new_s)


def reverse(self, word):
    start = 0
    end = len(word)-1
    a = list(word)
    while start < end:
        temp = a[start]
        a[start] = a[end]
        a[end] = temp
        start += 1
        end -= 1
    return "".join(a)
