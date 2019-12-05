# 692. Top K Frequent Words

# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
from collections import Counter

from heapq import *


def topKFrequent(words, k):

    map = Counter(words)
    res = map.most_common(k)
    return [i[0] for i in res]


def topKFrequent2(words, k):

    count = Counter(words)
    candidates = count.keys()
    candidates = sorted(count, key=lambda w: (-count[w], w))
    return candidates[:k]


def topKFrequent(words, k):
    # map with freq counts
    count = collections.Counter(words)

    # heap array with -negative freq for max heap and word tuple
    heap = [(-freq, word) for word, freq in count.items()]

    # heapify this array
    heapify(heap)

    # loop k times popping off the largest freq of each word
    return [heapq.heappop(heap)[1] for _ in range(k)]


print(topKFrequent2(["i", "love", "leetcode", "i", "love", "coding"], 2))
# ["i", "love"]
print(topKFrequent2(["the", "day", "is", "sunny",
                     "the", "the", "the", "sunny", "is", "is"], 4))
#: ["the", "is", "sunny", "day"]
