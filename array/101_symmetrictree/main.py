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

# https://leetcode.com/problems/symmetric-tree/
class Solution:

    def check(self, left:TreeNode, right:TreeNode):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)

    @timeit
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,2,3,4,4,3], True),
        ([1,2,2,3,5,4,3], False)
    ]
    for case in cases:
        p = build_tree(case[0])
        expected = case[1]
        judge(solution.isSymmetric(p), expected)

    
   