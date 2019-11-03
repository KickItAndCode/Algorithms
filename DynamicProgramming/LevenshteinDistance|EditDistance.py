# Write a program that takes two strings and computes the minimum
#  number of edits needed to transform the first string into
# the second string.


def levenshteinDistance(str1, str2):
    # builds array of arrays
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    # inits the first row with 0, 1,2 3,4
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j-1]:
                edits[i][j] = edits[i - 1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1],
                                      edits[i-1][j], edits[i][j-1])
    return edits[-1][-1]


print(levenshteinDistance("abc", "yabd"))  # 2
