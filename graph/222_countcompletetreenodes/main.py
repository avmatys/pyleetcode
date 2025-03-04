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


# https://leetcode.com/problems/count-complete-tree-nodes/
class Solution:

    @timeit
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def height(root):
            return -1 if root is None else 1 + height(root.left)
        
        h = height(root)
        total_count = 0
        while root:
            if height(root.right) == h - 1:
                total_count += 1 << h
                root = root.right
            else:
                total_count += 1 << (h - 1)
                root = root.left
            h -= 1
        return total_count


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3,4,5,6], 6),
        ([1,2,3], 3),
        ([1], 1),
        ([], 0)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.countNodes(input)
        judge(result, expected)

    
   