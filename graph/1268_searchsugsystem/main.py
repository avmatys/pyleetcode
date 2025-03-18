from typing import List
from datetime import datetime
from typing import Optional

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


class TrieNode:

    def __init__(self):
        self.chars = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.chars[idx] is None:
                node.chars[idx] = TrieNode()
            node = node.chars[idx]
        node.end = True

    def dfs_prefix(self, result, node, word):
        if len(result) == 3:
            return
        if node.end:
            result.append(word)
        for i, node in enumerate(node.chars):
            if node is not None:
                self.dfs_prefix(result, node, word + chr(i + 97))


    def suggest_words(self, prefix):
        result = []
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            #  We should form a prefix. If char is not in the prefix - return
            if curr.chars[idx] is None:
                return result
            curr = curr.chars[idx]
        self.dfs_prefix(result, curr, prefix)
        return result

# https://leetcode.com/problems/search-suggestions-system/
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for p in products:
            trie.insert(p)
        result = []
        for i in range(len(searchWord)):
            result.append(trie.suggest_words(searchWord[:i + 1]))
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
