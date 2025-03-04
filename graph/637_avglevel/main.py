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


# https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution:

    @timeit
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs(root, level, result):
            if not root:
                return
            if len(result) < level + 1:
                result.append([])
            result[level].append(root.val)
            bfs(root.left, level + 1, result)
            bfs(root.right, level + 1, result)
        result = []
        bfs(root, 0, result)
        return [sum(subarr)/len(subarr) for subarr in result]
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for i in range(len(result)):       
        assert result[i] == expected[i]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3,9,20,None,None,15,7], [3.00000,14.50000,11.00000])
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.averageOfLevels(input)
        judge(result, expected)
    
   