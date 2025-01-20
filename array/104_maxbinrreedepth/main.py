from typing import List
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr, i, n):
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2 * i + 1, n)
        root.right = build_tree(arr, 2 * i + 2, n)
    return root

# https://leetcode.com/problems/basic-calculator/
class Solution:

    @timeit
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calc_depth(node, depth):
            if not node:
                return depth
            depth += 1
            return max(calc_depth(node.left, depth), calc_depth(node.right, depth))  
        return calc_depth(root, 0) 
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2], 2)
    ]
    for case in cases:
        input = build_tree(case[0], 0, len(case[0]))
        expected = case[1]
        judge(solution.maxDepth(input), expected)

    
   