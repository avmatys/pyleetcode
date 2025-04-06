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


# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i, n = 0, len(traversal)
        root = None
        while i < n:
            # Calc actual depth
            curr_depth = 0
            while i + curr_depth < n and traversal[i + curr_depth] == '-':
                curr_depth += 1
            i += curr_depth
            # Calc val of the node
            num_cnt = 0
            while i + num_cnt < n and traversal[i + num_cnt].isnumeric():
                num_cnt += 1
            node = TreeNode(int(traversal[i : i + num_cnt]))
            i += num_cnt
            # Assign to the appropriate node
            while stack and stack[-1][1] >= curr_depth:
                stack.pop()
            if stack:
                if stack[-1][0].left is None:
                    stack[-1][0].left = node
                else:
                    stack[-1][0].right = node
            stack.append((node, curr_depth))
        return stack[0][0] if stack else None


