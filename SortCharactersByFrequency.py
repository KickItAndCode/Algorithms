# 451. Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


def frequencySort(s):

    # dictionary to store count of character appearing in the string
    dic = {}

    # final result
    result = ""

    # loop through each char, and add the count to the dic
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    # sort the dic on values in reverse order
    sorted_dic = sorted(dic, key=dic.get, reverse=True)

    # loop through, and create final string
    for count in sorted_dic:
        result += count * (dic[count])

    return result


print(frequencySort("tree"))  # "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
print(frequencySort("cccaaa"))

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
print(frequencySort("Aabb"))
# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
