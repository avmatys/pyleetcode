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


# https://leetcode.com/problems/path-sum-iii/description/
# Brute-force approch
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def calc_sum(node):
            if not node:
                return
            dfs(node, 0)
            calc_sum(node.left)
            calc_sum(node.right)

        def dfs(node, current_sum):
            if not node:
                return
            current_sum += node.val
            if current_sum == targetSum:
                self.count += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        # Run calculation
        calc_sum(root)
        return self.count
    
# Optimal approach with prefixes calculation
class SolutionRev:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_map = dict()
        prefix_map[0] = 1
        return self.calc_sum(root, 0, targetSum, prefix_map)
    
    def calc_sum(self, node, root_sum, target_sum, prefix_map):
        if not node:
            return 0
        root_sum += node.val
        # Count of the paths to the current node 
        paths_count = prefix_map.get(root_sum - target_sum, 0)
        # Update number of the paths with the current root_sum
        prefix_map[root_sum] = prefix_map.get(root_sum, 0) + 1
        # Recurcively calculate number of paths -> go to the last node
        result = paths_count + self.calc_sum(node.left, root_sum, target_sum, prefix_map) + self.calc_sum(node.right, root_sum, target_sum, prefix_map)
        # And backtrack visited 
        prefix_map[root_sum] = prefix_map.get(root_sum) - 1
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([10,5,-3,3,2,None,11,3,-2,None,1], 8), 3)
    ]
    for case in cases:
        input = build_tree(case[0][0])
        expected = case[1]
        result = solution.pathSum(input, case[0][1])
        judge(result, expected)
    
   