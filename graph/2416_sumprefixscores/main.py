from typing import List

class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.count = 0

    def insert(self, key):
        curr = self
        for ch in key:
            idx = ord(ch) - 97
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr.children[idx].count += 1
            curr = curr.children[idx]

    def score(self, key):
        curr = self
        res = 0
        for ch in key:
            idx = ord(ch) - 97
            res += curr.children[idx].count
            curr = curr.children[idx]
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for w in words:
            root.insert(w)
        res = []
        for w in words:
            res.append(root.score(w))
        return res
