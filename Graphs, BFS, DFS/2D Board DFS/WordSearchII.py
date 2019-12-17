# 212. Word Search II
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


# Example:

# Input:
# board = [
#     ['o', 'a', 'a', 'n'],
#     ['e', 't', 'a', 'e'],
#     ['i', 'h', 'k', 'r'],
#     ['i', 'f', 'l', 'v']
# ]
# words = ["oath", "pea", "eat", "rain"]

# Output: ["eat", "oath"]
# optimal approach does DFS but uses a try


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root

        for w in words:
            trie.insert(w)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)

        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)

        if not node:
            return

        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp


# too slow approach


def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def exist(board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                # find first letter
                if board[i][j] == word[0] and dfs(board, i, j, 0,  word):
                    return True

        return False

    def dfs(board, i, j, count, word):
        # found word
        if count == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
            return False

        temp = board[i][j]
        board[i][j] = " "

        found = dfs(board, i+1, j, count + 1, word) or dfs(board, i-1, j, count + 1,
                                                           word) or dfs(board, i, j-1, count + 1, word) or dfs(board, i, j+1, count + 1, word)

        board[i][j] = temp
        return found

    res = []
    for word in words:
        if exist(board, word):
            res.append(word)
    return res
