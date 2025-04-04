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

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
class Solution:

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                return depth, None
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            # Left is deepre -> return left's lca
            if left[0] > right[0]:
                return left
            # The same as for left
            elif right[0] > left[0]:
                return right
            # Both subtrees have the same depth - current node is lca
            else:
                return left[0], node
        return dfs(root, 0)[1]
