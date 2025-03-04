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


# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
class Solution:

    @timeit
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        min_diff = float('inf')
        prev = None 
        stack = []
        node = root
        while stack or node is not None:
            # Prestore all values in the stack from the all left nodes
            while node:
                stack.append(node)
                node = node.left
            # Now we can get these nodes and continue with right subtree
            node = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            node = node.right
        return min_diff


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,0,48,None,None,12,49], 1),
        ([4,2,6,1,3], 1),
        ([1,0,2], 1)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.getMinimumDifference(input)
        judge(result, expected)
    
   