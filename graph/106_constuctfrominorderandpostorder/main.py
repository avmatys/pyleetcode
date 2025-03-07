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

def compare_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None): 
            return True
        if p and q and p.val == q.val:
            return compare_tree(p.left, q.left) and compare_tree(p.right, q.right)
        return False

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Check if lists are not empty
        if not inorder or not postorder:
            return None
        if len(inorder) < 2:
            return TreeNode(inorder[0])
        # Ok, we have enough elements to build a subtrees
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx : -1])
        return root

    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert compare_tree(result, expected)


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([9,3,15,20,7], [9,15,7,20,3]), [3,9,20,None,None,15,7]),
        (([-1],[-1]), [-1])
    ]
    for case in cases:
        result = solution.buildTree(case[0][0], case[0][1])
        expected = build_tree(case[1])
        judge(result, expected)

    
   