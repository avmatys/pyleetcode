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

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root  
    left = find_node(root.left, val)
    if left:
        return left
    right = find_node(root.right, val)
    if right:
        return right


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
class Solution:

    @timeit
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,3],2,3), 1)
    ]
    for case in cases:
        input = build_tree(case[0][0])
        expected = case[1]
        p = find_node(input,case[0][1])
        q = find_node(input,case[0][2])
        result = solution.lowestCommonAncestor(input, p, q)
        judge(result, find_node(input,expected))

    
   