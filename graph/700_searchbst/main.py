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

# https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:

    @timeit
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, val):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val < val:
                return search(node.right, val)
            else:
                return search(node.left, val)
        return search(root, val)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([4,2,7,1,3], 2), 2)
    ]
    for case in cases:
        input = build_tree(case[0][0])
        expected = case[1]
        result = solution.searchBST(input, case[0][1])
        judge(result.val if result else None, expected)
    
   
