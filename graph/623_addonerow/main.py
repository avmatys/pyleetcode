from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node, h, t):
            if h == depth:
                new = TreeNode(val)
                if t == 1: new.right = node
                if t == -1: new.left = node
                return new
            if node is None:
                return None
            node.left = dfs(node.left, h + 1, -1)
            node.right = dfs(node.right, h + 1, 1)
            return node

        return dfs(root, 1, -1)
