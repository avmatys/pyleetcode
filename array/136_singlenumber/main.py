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

# https://leetcode.com/problems/single-number/description
class Solution:

    @timeit
    def singleNumber(self, nums: List[int]) -> int:
      result = 0
      for num in nums:
          result ^= num
      return result
        

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2,2,1], 1),
        ([4,1,2,1,2], 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.singleNumber(input), expected)

    
   