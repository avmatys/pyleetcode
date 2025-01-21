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

# https://leetcode.com/problems/invert-binary-tree/
class Solution:

    @timeit
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert compare_tree(result, expected)

def compare_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (p is None and q is None): 
        return True
    if p and q and p.val == q.val:
        return compare_tree(p.left, q.left) and compare_tree(p.right, q.right)
    return False

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([2,1,3], [2,3,1])
    ]
    for case in cases:
        p = build_tree(case[0])
        expected = build_tree(case[1])
        judge(solution.invertTree(p), expected)

    
   