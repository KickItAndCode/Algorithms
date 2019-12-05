def RemoveVowels(s):
    vowels = set(["a", "e", "i", "o", "u"])
    res = ""
    for c in s:
        if c not in vowels:
            res += c
    return res


print(RemoveVowels("leetcodeisacommunityforcoders"))
print(RemoveVowels("aeiou"))
