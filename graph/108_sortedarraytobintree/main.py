from typing import List
from typing import Optional
from datetime import datetime
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

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
class Solution:

    @timeit
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def findnode(start: int, end: int):
            
            # Base case
            if start >= end:
                return None
            
            middle_idx = (end + start) // 2

            # Find roots of left and right subtrees
            left = findnode(start, middle_idx)
            right = findnode(middle_idx + 1, end)

            node = TreeNode(nums[middle_idx], left, right)
            
            return node
        
        root = findnode(0, len(nums))
        return root
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([-10,-3,0,5,9]), [0,-3,9,-10, None,5])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.sortedArrayToBST(input), expected)

    
   