# 482. License Key Formatting
# You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

# Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

# Given a non-empty string S and a number K, format the string according to the rules described above.

# Example 1:
# Input: S = "5F3Z-2e-9-w", K = 4

# Output: "5F3Z-2E9W"

# Explanation: The string S has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:
# Input: S = "2-5g-3-J", K = 2

# Output: "2-5G-3J"

# Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
# Note:
# The length of string S will not exceed 12,000, and K is a positive integer.
# String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
# String S is non-empty.


def licenseKeyFormatting(S, K):

    res = []

    # count to make sure we don't add more
    # then K chars before we add a -
    groupCount = K

    # get ride of dashes and upper case all
    S = S.replace("-", "").upper()
    for i in range(len(S)-1, -1, -1):

        res.insert(0, S[i])
        groupCount -= 1

        if groupCount == 0 and i != 0:
            res.insert(0, "-")
            groupCount = K

    return "".join(res)


def licenseKeyFormatting2(S, K):

    S = S.replace("-", "").upper()  # remove "-" and covert string to uppercase
    remainder = len(S) % K      # calculate length of first group
    # For example:
    # remainder==1; k=3: 1-123-123-123
    # remainder==0; k=3: _-123-123-123 (blank)

    first_grp = [S[0:remainder]]  # first group
    other_grps = [S[i:i+K]
                  for i in range(remainder, len(S), K)]  # other groups

    if remainder:
        return "-".join(first_grp+other_grps)
    # first group is empty at this point
    return "-".join(other_grps)


print(licenseKeyFormatting2("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(licenseKeyFormatting2("2-5g-3-J", 2))  # "2-5G-3J"
print(licenseKeyFormatting2("--a-a-a-a--", 2))  # "AA-AA"
