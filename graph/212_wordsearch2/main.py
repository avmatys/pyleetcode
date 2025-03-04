from typing import List, Set
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
        self.word = None

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            ch_code = ord(c) - ord('a')
            if not curr.children[ch_code]:
                curr.children[ch_code] = TrieNode()
            curr = curr.children[ch_code]
        curr.is_end = True
        curr.word = word
    
# https://leetcode.com/problems/word-search-ii/description/
class Solution:

    def check_word(self, board: List[List[str]], i: int, j: int, result: List[str], node: TrieNode):
        n, m = len(board), len(board[0])
        if i < 0 or j < 0 or i >=n or j >= m or board[i][j] == '#':
            return
        ch_code = ord(board[i][j]) - ord('a')
        if not node.children[ch_code]:
            return
        node = node.children[ch_code]
        if node.is_end:
            node.is_end = False
            result.append(node.word)

        tmp = board[i][j]
        board[i][j] = '#'
        for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+x, j+y
            self.check_word(board, ni, nj, result, node)
        board[i][j] = tmp
    
    @timeit
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        n, m = len(board), len(board[0])
        result = []
        for i in range(n):
            for j in range(m):
                self.check_word(board, i, j, result, trie.root)
        return result   

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert len(result) == len(expected)
    for w in expected:
        assert w in result

if __name__ == '__main__':
    cases = [
        (([["a","b"],["c","d"]],["abcb"]), []),
        (([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]), ["eat","oath"]),
        (([["a","a"],["a","a"],["a","a"]], ["aa"]), ["aa"]), 
        (([["a","a"]], ["aaa"]), [])
    ]
    for case in cases:
        solution = Solution()
        result = solution.findWords(*case[0])
        judge(result, case[1])
