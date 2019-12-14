# Trie(we pronounce "try") or prefix tree is a tree data structure, which is used for retrieval of a key in a dataset of strings. There are various applications of this very efficient data structure such as:

#     # autocomplete
# spell checker
# ip routinig longest prefix matching
# t9 predictive text
# solving word games

# # o()
# There are several other data structures, like balanced trees and hash tables, which give us the possibility to search for a word in a dataset of strings. Then why do we need trie? Although hash table has O(1)O(1) time complexity for looking for a key, it is not efficient in the following operations:

# Finding all keys with a common prefix.
# Enumerating a dataset of strings in lexicographical order.
# Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to O(n)O(n), where nn is the number of keys inserted. Trie could use less space compared to Hash Table when storing many keys with the same prefix. In this case using trie has only O(m)O(m) time complexity, where mm is the key length. Searching for a key in a balanced tree costs O(m \log n)O(mlogn) time complexity.


class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word = False
            self.children = {}

    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        # @param {string} word
        # @return {void}
        # Inserts a word into the trie.
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.word=True
    
        # @param {string} word
        # @return {boolean}
        # Returns if the word is in the trie.
        def search(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    return False
                node=node.children[i]
            return node.word
    
        # @param {string} prefix
        # @return {boolean}
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        def startsWith(self, prefix):
            node=self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node=node.children[i]
            return True
            
    
    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")

# less clear but fancy

# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.is_word = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         current = self.root
#         for letter in word:
#             current = current.children[letter]
#         current.is_word = True

#     def search(self, word):
#         current = self.root
#         for letter in word:
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return current.is_word

#     def startsWith(self, prefix):
#         current = self.root
#         for letter in prefix:
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return True

