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


# https://leetcode.com/problems/binary-tree-right-side-view/description/
class Solution:

    @timeit
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root, level, result):
            if not root:
                return
            if len(result) == level:
                result.append(root.val)
            bfs(root.right, level + 1, result)
            bfs(root.left, level + 1, result)
        result = []
        bfs(root, 0, result)
        return result
     
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    for i in range(len(result)):       
        assert result[i] == expected[i]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,None,5,None,4], [1,3,4]),
        ([1,2,3,4,None,None,None,5], [1,3,4,5])    
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.rightSideView(input)
        judge(result, expected)
    
   