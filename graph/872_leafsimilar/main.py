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


# https://leetcode.com/problems/leaf-similar-trees/description/
class Solution:

    @timeit
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leafs(root, leafs):
            if not root:
                return
            if not root.left and not root.right:
                leafs.append(root.val)
                return
            get_leafs(root.left, leafs)
            get_leafs(root.right, leafs)
        leafs1, leafs2 = [], []
        get_leafs(root1, leafs1)
        get_leafs(root2, leafs2)
        return leafs1 == leafs2

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([3,5,1,6,2,9,8,None,None,7,4],[3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]), True)
    ]
    for case in cases:
        input1 = build_tree(case[0][0])
        input2 = build_tree(case[0][1])
        expected = case[1]
        result = solution.leafSimilar(input1, input2)
        judge(result, expected)
    
   