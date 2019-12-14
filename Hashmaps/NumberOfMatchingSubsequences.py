from collections import defaultdict


def numMatchingSubseq(S, words):
    # keys of this map are individual chars and the value is a list of words
    map = defaultdict(list)
    count = 0

    # build map with initial words
    for word in words:
        map[word[0]].append(word)

    # loop through large string
    for char in S:
        # grab all the current words that start with the char
        wordsExpectingChar = map[char]

        # we've stored the words so you can empty the list here
        map[char] = []

        # go through the words that start with char
        for word in wordsExpectingChar:
            # its a full word
            if len(word) == 1:
                count += 1
            else:
                # slice the word minues the first char and put it in the map
                map[word[1]].append(word[1:])

    return count


print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))  # 3
