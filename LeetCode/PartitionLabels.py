# 763. Partition Labels
# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9, 7, 8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:

# S will have length in range[1, 500].
# S will consist of lowercase letters('a' to 'z') only.


# def partitionLabels(S):
#     res = []
#     lastIndexes = [0] * 26

#     # initializes this array to contain the last indexes
#     # for each character in S
#     for i in range(len(S)):
#         lastIndexes[ord((S[i])) - 96] = i

#     i = 0
#     while i < len(S):
#         # get last index for the curr char
#         end = lastIndexes[ord((S[i])) - 96]
#         j = i
#         # loop from j to the last index of the current char
#         # update end
#         while j != end:
#             end = max(end, lastIndexes[ord((S[j])) - 96])
#             j += 1
#         # record the lenght of the partition
#         res.append(j-i + 1)
#         # set I to be one after to look for the next partition
#         i = j + 1
#     return res

# Store the last seen index in the first pass. In the second pass, lookup the last seen for each character as we encounter them and keep track of the maximum last seen value so far. Whenever we reach an index that equals the maximum last seen so far, we start a new partition.

def partitionLabels(S):
    res, last_seen, max_last_seen, count = [], {}, 0, 0
    # store last time we seen this in map
    for i, char in enumerate(S):
        last_seen[char] = i

    # go through all chars for a second time
    # update the max seen  and keep count until you see get to the max seen character
    for i, char in enumerate(S):
        max_last_seen = max(max_last_seen, last_seen[char])
        count += 1

        # if these are equal this is the furthest for that partition
        if i == max_last_seen:
            res.append(count)
            count = 0
    return res


print(partitionLabels("ababcbacadefegdehijhklij"))  # [9,7,8]
print(partitionLabels("qvmwtmzzse"))  #
