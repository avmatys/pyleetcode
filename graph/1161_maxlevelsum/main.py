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


# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
class Solution:

    @timeit
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = [float('-inf'), -1]
        level = 1
        while queue:
            level_queue = deque()
            level_sum = 0
            while queue:
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left:
                    level_queue.append(curr.left)
                if curr.right:
                    level_queue.append(curr.right)
            if level_sum > max_sum[0]:
                max_sum[0] = level_sum
                max_sum[1]= level
            level += 1
            queue = level_queue
        return max_sum[1]

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,7,0,7,-8,None,None], 2)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.maxLevelSum(input)
        judge(result, expected)
    
   
