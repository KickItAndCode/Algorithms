# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.


def letterCombinations(digits):
    res = []
    if not digits:
        return res

    mappings = ["0", "1", "abc", "def", "ghi",
                "jkl", "mno", "pqrs", "tuv", "wxyz"]

    helper(res, digits, "", 0, mappings)
    return res


def helper(res, digits, curr, index, mappings):

    # if the length matches the length of digits
    #   then add curr to res and return
    if len(curr) == len(digits):
        res.append(curr)
        return

    # gets letters for that digits string
    letters = mappings[int(digits[index])]

    # loop through each letter
    for i in range(len(letters)):
        # call helper function on curr + current letter in loop
        # increase index to move to next letter in the digits
        helper(res, digits, curr + letters[i], index+1, mappings)


# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
print(letterCombinations("23"))
