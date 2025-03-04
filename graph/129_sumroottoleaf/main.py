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


# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
class Solution:

    @timeit
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def get_number(node: TreeNode, current_sum: int):
            # Leaf node, value was already summed
            if not node:
                return 0
            # Update current sum
            current_sum = 10 * current_sum + node.val
            # Check if we can proceed
            if not node.left and not node.right:
                return current_sum
            # Recursively continue
            return get_number(node.left, current_sum) + get_number(node.right, current_sum)
        return get_number(root, 0)

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1], 1),
        ([1,2,3], 25),
        ([4,9,0,5,1], 1026),
        ([0], 0)
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        result = solution.sumNumbers(input)
        judge(result, expected)

    
   