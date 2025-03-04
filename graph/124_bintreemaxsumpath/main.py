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

def build_tree(arr, i = 0):
    root = None
    n = len(arr)
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2 * i + 1)
        root.right = build_tree(arr, 2 * i + 2)
    return root


# https://leetcode.com/problems/binary-tree-maximum-path-sum/
class Solution:

    @timeit
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = float('-inf')
        def calc_sum(node):
            nonlocal max_sum
            if node is None:
                return 0
            left_sum = max(calc_sum(node.left), 0)
            right_sum = max(calc_sum(node.right), 0)
            curr_sum = left_sum + right_sum + node.val
            max_sum = max(max_sum, curr_sum)
            return node.val + max(left_sum, right_sum) # We can't go to the 2 directions together, but only one
        calc_sum(root)
        return max_sum

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3], 6),
        ([1,2,-1000], 3),
        ([-1,2,-3], 2),
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.maxPathSum(input)
        judge(result, expected)

    
   