# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

# f l o w e r
# 0 1 2 3 4 5


def longestCommonPrefix(strs):
    # get the min length of a string in the list
    minL = min(map(len, strs)) if strs else 0
    # loop over the characters from the smallest
    for i in range(minL):
        # loop over strings in list starting with the second
        for j in range(1, len(strs)):
            # compare the first string with the others
            # compare the the same index in chars for each of the strings
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]

    return strs[0][:minL] if minL else ""


print(longestCommonPrefix(["flower", "flow", "flight"]))  # fl
print(longestCommonPrefix(["dog", "racecar", "car"]))  # ""
