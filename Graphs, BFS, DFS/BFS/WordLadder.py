# 127. Word Ladder
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# Intuition

# Start from beginWord and search the endWord using BFS.

# Algorithm

# Do the pre-processing on the given wordList and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.

# Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node. We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.

# To prevent cycles, use a visited dictionary.

# While the queue has elements, get the front element of the queue. Let's call this word as current_word.

# Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the all_combo_dict.

# The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

# Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the level for the current_word.

# Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.

# Termination condition for standard BFS is finding the end word.
from collections import defaultdict, deque
from string import ascii_lowercase

# easiest to understand


def ladderLength3(beginWord, endWord, wordList):
    # start with queue with the first word
    queue = [(beginWord, 1)]
    visited = set()
    wordSet = set(wordList)

    while queue:

        # grab first word and current level
        word, dist = queue.pop(0)

        # check if your current word is the end work
        if word == endWord:
            return dist

        # loop through length of word
        for i in range(len(word)):

            # loop through all lowercase chars
            for j in ascii_lowercase:

                # swap a character with the current char
                tmp = word[:i] + j + word[i+1:]

                # check if the word has been seen before and if its in the word list
                if tmp not in visited and tmp in wordSet:
                    queue.append((tmp, dist+1))
                    visited.add(tmp)
    return 0


def ladderLength(beginWord, endWord, wordList):

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    # Since all words are of same length.
    L = len(beginWord)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time.
    all_combo_dict = defaultdict(list)

    for word in wordList:
        for i in range(L):
            # Key is the generic word
            # Value is a list of words which have the same intermediate generic word.
            key = word[:i] + "*" + word[i+1:]
            all_combo_dict[key].append(word)

    queue = deque([(beginWord, 1)])

    # Visited to make sure we don't repeat processing same word.
    visited = {beginWord: True}
    while queue:
        curr_word, level = queue.popleft()
        for i in range(L):
            # Intermediate words for current word
            intermediate_word = curr_word[:i] + "*" + curr_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:

                # If at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer.
                if word == endWord:
                    return level + 1

                # Otherwise, add it to the BFS Queue. Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))

            all_combo_dict[intermediate_word] = []
    return 0


def ladderLength2(beginWord, endWord, wordList):
    wordSet = set(wordList)

    if endWord not in wordSet:
        return 0

    queue = deque()
    queue.append(beginWord)

    res = 0

    while queue:
        for i in range(len(queue) - 1, -1, -1):
            word = queue.popleft()
            if word == endWord:
                return res + 1

            # make a copy of word to manipulate
            # go through the word to check possibilities
            for i in range(len(word)):
                newword = list(word)
                for char in ascii_lowercase:
                    newword[i] = char
                    newString = "".join(newword)
                    # if the word is in the word list and isn't the same as the original word
                    if newString in wordSet and newString != wordSet:
                        queue.append(newString)
                        wordSet.remove(newString)
        res += 1
    return 0


# print(ladderLength("hit", "cog", [
#       "hot", "dot", "dog", "lot", "log", "cog"]))  # 5
# print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0


print(ladderLength3("hit", "cog", [
      "hot", "dot", "dog", "lot", "log", "cog"]))  # 5
print(ladderLength3("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
