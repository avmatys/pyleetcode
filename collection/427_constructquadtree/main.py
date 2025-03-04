from typing import List, Optional
from datetime import datetime
import math
from collections import deque


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert len(result) == len(expected)
    for i in range(len(result)):
        assert result[i] == expected[i]

def serialize_iter(node):
    if not node:
        return []
    result, level = [], 0
    queue = deque([node])
    while queue:
        next_level = level
        next_queue = deque()
        level_data = []
        while queue:
            curr = queue.popleft()
            if curr is None:
                level_data.append(None)
                next_queue.extend([None] * 4)
                continue
            level_data.append([int(curr.isLeaf), int(curr.val)])
            next_queue.extend([curr.topLeft, curr.topRight, curr.bottomLeft, curr.bottomRight])
            if not curr.isLeaf:
                next_level = level + 1
        if next_level != level:
            queue = next_queue
            level = next_level
        else:
            while level_data[-1] is None:
                level_data.pop()
        result.extend(level_data)
    return result 

def trim_none(result):
    while result[-1] == None:
        result.pop()

# https://leetcode.com/problems/construct-quad-tree/description/
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:

    def construct_tree(self, grid, row, col, size):
        # Check if all elements in the specified segment has same values
        equal = True
        for i in range(row, row + size):
            for j in range(col, col + size):
                if grid[row][col] != grid[i][j]:
                    equal = False
                    break
            if not equal: break
        # If all elements the same - we can compress them
        if equal:
            return Node(grid[row][col] != 0, True)
        # Else repeat the same procedure  
        else:
            mid = size // 2
            node = Node(True, False)
            node.topLeft = self.construct_tree(grid, row, col, mid)
            node.topRight = self.construct_tree(grid, row, col + mid, mid)
            node.bottomLeft = self.construct_tree(grid, row + mid, col, mid)
            node.bottomRight = self.construct_tree(grid, row + mid, col + mid, mid)
            return node

    @timeit
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.construct_tree(grid, 0, 0, n)

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[0]], [[1,0]]),
        ([[1]], [[1,1]]),
        ([[0,1],[1,0]], [[0,1],[1,0],[1,1],[1,1],[1,0]]),
        ([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]], [[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]])
    ]
    for case in cases:
        lists = []
        root = solution.construct(case[0])
        result = serialize_iter(root)
        judge(result, case[1])
    



    
   