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

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def calc_score(self, root, scores):
        if root is None:
            return 0
        score = root.val + self.calc_score(root.left, scores) + self.calc_score(root.right, scores)
        scores.append(score)
        return score

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        scores = []
        total = self.calc_score(root, scores)
        # To maximaze the result we should minimaze the diff
        diff = inf
        result = 0
        for score in scores[:-1]:
            curr_diff = abs(total - 2 * score)
            if curr_diff < diff:
                diff = curr_diff
                result = (total - score) * score
        return result % 1000000007

