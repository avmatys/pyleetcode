from typing import List
from datetime import datetime
import math

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper

# https://leetcode.com/problems/house-robber-iii/description/
class Solution:

    @timeit
    def dfs(self, node):
        if not node:
            return (0,0) # prev_max, max
        lpm, lm = self.dfs(node.left)
        rpm, rm = self.dfs(node.right)
        return (lm + rm, max(lpm + rpm + node.val, lm + rm))

    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]    
