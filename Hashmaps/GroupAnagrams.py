# 49. Group Anagrams
# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict

# Two strings are an anagram if and only if their storted strongs
# are equal
# create a hashmap
# loop through strings and sorted the value
# add a tuple of the sorted value of the string to the map
# append to the list value the original string
# return the values list of the map

# Time O (NK log K) N is length of str k is max lengh of str
# space O(NK)


def groupAnagrams(strs):
    map = defaultdict(list)
    for s in strs:
        map[tuple(sorted(s))].append(s)
    return map.values()


def isAnagram(s1, s2):

    map = {}
    for c in s1:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    for c in s2:
        if c not in map:
            return False

    return True


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
