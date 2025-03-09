from typing import List
from datetime import datetime
from typing import Optional
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr, i = 0):
    root = None
    n = len(arr)
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2 * i + 1)
        root.right = build_tree(arr, 2 * i + 2)
    return root

# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [-1,-1,-1]
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]
        return dfs(root)[-1]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,1,1,None,1,None,None,1,1,None,1], 2)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.longestZigZag(input)
        judge(result, expected)
    
   
