from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:

    @timeit
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        root = Trie()
        for str in strs[1:]:
            root.insert(str)
        prefix = root.longest_prefix(strs[0])
        return prefix


class TrieNode:

    def __init__(self):
        self.children = {}
        self.children_count = 0
        self.is_end = False

    def add_char(self, character):
        if character not in self.children:
            self.children[character] = TrieNode()
            self.children_count += 1
    
    def get_children(self):
        return self.children.items()


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for character in word:
            node.add_char(character)
            node = node.children[character]
        node.is_end = True
    
    def longest_prefix(self, word):
        prefix = []
        node = self.root
        for character in word:
            if character in node.children and node.children_count == 1 and not node.is_end:
                prefix.append(character)
                node = node.children[character]
            else:
                break
        return "".join(prefix)


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["dog","dog","dog"], "dog"),
        (["dg", "d", "dgb"], "d")
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.longestCommonPrefix(input), expected)


    
   