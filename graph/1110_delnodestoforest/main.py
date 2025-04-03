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

# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, to_delete, visited, forest):
        if not root or root.val in visited:
            return
        visited.add(root.val)
        if root.left:
            left = root.left
            if left.val in to_delete:
                if left.left and left.left.val not in to_delete:
                    forest.append(left.left)
                    self.dfs(left.left, to_delete, visited, forest)
                if left.right and left.right.val not in to_delete:
                    forest.append(left.right)
                    self.dfs(left.left, to_delete, visited, forest)
                root.left = None
            else:
                self.dfs(left, to_delete, visited, forest)
        if root.right:
            right = root.right
            if right.val in to_delete:
                if right.left and right.left.val not in to_delete:
                    forest.append(right.left)
                    self.dfs(right.left, to_delete, visited, forest)
                if right.right and right.right.val not in to_delete:
                    forest.append(right.right)
                    self.dfs(right.right, to_delete, visited, forest)
                root.right = None
            else:
                self.dfs(right, to_delete, visited, forest)

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = [root]
        self.dfs(root, to_delete, set(), forest)
        return forest

