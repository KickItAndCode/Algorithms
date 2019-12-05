# You are given two non-empty strings: a big string and a small string. Write a function that returns the smallest substring in the big string that contains all of the characters found in the small string. Note that 1) the substring can contain other characters not found in the small string, 2) the characters in the substring don't have to be in the same order as they appear in the small string, and 3) if the small string has duplicate characters, the substring has to contain those duplicate characters (it can also contain more, but not fewer).

# Sample input: "abcd$ef$axb$c$", "$$abf"
# Sample output: "f$axb$"

from collections import Counter, defaultdict


def smallestSubstringContaining(bigString, smallString):

    targetCharCounts = Counter(smallString)
    substringBounds = getStringFromBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)


def getSubstringBounds(s, targetCharCounts):
    substringBounds = [0, float("inf")]
    substringCharCounts = defaultdict(int)
    numUniqueChars = len(targetCharCounts.keys())
    l, r, numUniqueCharsDone = 0, 0, 0

    # move the right index to the right in the string until you've counted all of the target characters enough times
    while r < len(s):
        rightChar = s[r]
        if rightChar not in targetCharCounts:
            r += 1
            continue
        # we found a char in our small small substring
        substringCharCounts[rightChar] += 1

        # if we found it then increase our done count
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1
        # move the left index to the right in the string until you no longer have ebough of the target characters in between leftidx and right idx. Update the substring bounds accordingly
        while numUniqueCharsDone == numUniqueChars and l <= r:
            substringBounds = getCloserBounds(
                l, r, substringBounds[0], substringBounds[1])
            leftChar = s[l]

            if leftChar not in targetCharCounts:
                l += 1
                continue

            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1

            substringCharCounts[leftChar] -= 1
            l += 1
        r += 1
    return substringBounds


def getCloserBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2-idx1 < idx4 - idx3 else [idx3, idx4]


def getStringFromBounds(s, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""

    return s[start:end + 1]


print(smallestSubstringContaining("abcd$ef$axb$c$", "$$abf"))  # "f$axb$"
