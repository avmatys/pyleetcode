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

# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            ch_code = ord(c) - ord('a')
            if not curr.children[ch_code]:
               curr.children[ch_code] = TrieNode()
            curr = curr.children[ch_code]
        curr.is_end = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            ch_code = ord(c) - ord('a')
            if not curr.children[ch_code]:
                return False
            curr = curr.children[ch_code]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            ch_code = ord(c) - ord('a')
            if not curr.children[ch_code]:
                return False
            curr = curr.children[ch_code]
        return True

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    trie = Trie()
    trie.insert('abscf')
    trie.insert('avc')
    trie.insert('abc')
    assert trie.startsWith('a') == True
    assert trie.startsWith('b') == False
    assert trie.search('abs') == False
    assert trie.search('abc') == True
