from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        freq = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return ""
            l = dfs(node.left)
            r = dfs(node.right)
            c = f"{str(node.val)}|{l}|{r}"
            freq[c] += 1
            if freq[c] == 2:
                res.append(node)
            return c

        dfs(root)
        return res

