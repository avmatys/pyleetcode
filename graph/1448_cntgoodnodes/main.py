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


# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
class Solution:

    @timeit
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            result = 0
            if node.val >= max_val:
                result += 1
                max_val = max(max_val, node.val)
            result += dfs(node.left, max_val)
            result += dfs(node.right, max_val)
            return result
        return dfs(root, float('-inf'))

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,1,4,3,None,1,5], 4)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.goodNodes(input)
        judge(result, expected)
    
   