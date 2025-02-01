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


# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
class Solution:

    @timeit
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []
        result = None
        count = 0
        def bfs(node):
            nonlocal count
            nonlocal result
            if node is None:
                return
            # Get to the end of the left subtree, this is the first element in the sequence
            bfs(node.left)
            # Now we can update counter becase we are on the lowest level
            count += 1
            # We can check if the condition is met and set the value and return
            if count == k:
                result = node.val
                return
            bfs(node.right)
        bfs(root)
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,0,48,None,None,12,49], 1), 0),
        (([5,3,6,2,4,None,None,1],3), 3),
        (([1,0,2], 2), 1)
    ]
    for case in cases:
        input = build_tree(case[0][0])
        expected = case[1]
        result = solution.kthSmallest(input, case[0][1])
        judge(result, expected)
    
   