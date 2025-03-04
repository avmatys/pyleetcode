from typing import List
from datetime import datetime
from collections import Counter


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
        self.count = 0
        self.childs = dict()
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, values):
        curr_node = self.root
        for value in values:
            if value not in curr_node.childs:
                curr_node.childs[value] = TrieNode()
            curr_node = curr_node.childs[value]
        curr_node.count += 1
    
    def count_array(self, values):
        curr_node = self.root
        for value in values:
            if value not in curr_node.childs:
                return 0
            curr_node = curr_node.childs[value]
        return curr_node.count

# https://leetcode.com/problems/equal-row-and-column-pairs
class Solution:

    # Brute force
    @timeit
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                k = 0
                while k < n and grid[i][k] == grid[k][j]:
                    k += 1
                count += k == n
        return count
    
    # Prefix tree
    @timeit
    def equalPairs2(self, grid: List[List[int]]) -> int:
        n, count = len(grid), 0
        trie = Trie()
        for i in range(n):
            trie.insert(grid[i])
        for j in range(n):
            values = [grid[i][j] for i in range(n)]
            count += trie.count_array(values)
        return count

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.equalPairs2(input), expected)

    
   