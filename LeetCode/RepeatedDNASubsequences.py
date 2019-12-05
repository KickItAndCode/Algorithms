# 187. Repeated DNA Sequences
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Example:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

from collections import defaultdict


def findRepeatedDnaSequences(s):
    res = []
    seenMap = defaultdict(int)
    i = 0
    while i + 10 <= len(s):
        subsequence = s[i: i+10]
        i += 1
        seenMap[subsequence] += 1
    for k, v in seenMap.items():
        if v >= 2:
            res.append(k)

    return res

# faster


def findRepeatedDnaSequences2(s):
    res = []
    seenMap = defaultdict(int)
    i = 0
    while i + 10 <= len(s):
        subsequence = s[i: i+10]
        i += 1
        seenMap[subsequence] += 1

        if seenMap[subsequence] == 2:
            res.append(subsequence)

    return res


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
