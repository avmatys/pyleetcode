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

def tree_to_ll(node):
    result = []
    while node:
        result.append(node.val),
        if node.right:
            result.append(None)
        node = node.right
    return result

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
class Solution:

   def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            # If we have any left node - proceed it
            if node.left:
                curr = node.left
                # Go to the deepest right node
                while curr.right:
                    curr = curr.right
                # Change links
                curr.right = node.right # Attach the latest node from the left subnode (curr) to the right node of the prev node (like insert between nodes)
                node.right = node.left # And after this link left to the right
                node.left = None
            # Go to the next right node
            node = node.right

def judge(result, expected):
    result_list = tree_to_ll(result)
    print(f'Result {result_list} Expected {expected}')
    for i in range(len(expected)):
        assert result_list[i] == expected[i]


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([1,2,3], [1,None,2,None,3]),
        ([1,2,5,3,4,None,6], [1,None,2,None,3,None,4,None,5,None,6]),
        ([], []),
        ([0], [0])
    ]
    for case in cases:
        input = build_tree(case[0])
        expected = case[1]
        solution.flatten(input)
        judge(input, expected)

    
   