from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def dfs(node):
            # No node
            if not node:
                return None
            # Try to find bigger value
            if node.val < low:
                return dfs(node.right)
            # Try to fin smaller
            if node.val > high:
                return dfs(node.left)
            # Keep current node
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        return dfs(root)
