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
        self.children = [None] * 26 
        self.is_end = False

# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class WordDictionary:      

    def __init__(self):
        self.root = TrieNode()
        self.max_len = 0

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            ch_code = ord(c) - ord('a')
            if not curr.children[ch_code]:
                curr.children[ch_code] = TrieNode()
            curr = curr.children[ch_code]
        curr.is_end = True
        self.max_len = max(len(word), self.max_len)

    def search(self, word: str) -> bool:
        if len(word) > self.max_len:
            return False
        return self.search_helper(self.root, word, 0)

    def search_helper(self, node, word, idx):
        if node is None:
            return False
        if idx == len(word):
            return node.is_end
        if word[idx] == '.':
            for child in node.children:
                if child is not None and self.search_helper(child, word, idx + 1):
                    return True
            return False
        else:
            ch_code = ord(word[idx]) - ord('a')
            if node.children[ch_code] is None: 
                return False
            return self.search_helper(node.children[ch_code], word, idx + 1)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    trie = WordDictionary()
    trie.addWord('abscf')
    trie.addWord('avc')
    trie.addWord('abc')
    assert trie.search('a') == False
    assert trie.search('abc') == True
    assert trie.search('a.s') == False
    assert trie.search('.v.') == True
