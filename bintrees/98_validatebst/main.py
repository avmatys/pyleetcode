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


# https://leetcode.com/problems/validate-binary-search-tree
class Solution:

    @timeit
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        prev = None
        valid = True
        def inorder(node):
            nonlocal prev
            nonlocal valid
            if node is None:
                return
            inorder(node.left)
            if prev is not None:
                if node.val <= prev:
                    valid = False
                    return 
            prev = node.val
            inorder(node.right)
        inorder(root)
        return valid

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2,1,3], True),
        ([5,1,4,None,None,3,6],False)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.isValidBST(input)
        judge(result, expected)
    
   