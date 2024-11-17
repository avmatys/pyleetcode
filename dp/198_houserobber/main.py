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


# https://leetcode.com/problems/house-robber/description/
class Solution:

    @timeit
    def rob(self, nums: List[int]) -> int:  
        n = len(nums)
        if n < 3:
            return max(nums)
        result = [0] * n
        result[0] = nums[0];
        result[1] = max(nums[0], nums[1])
        for i in range(2, n):
            result[i] = max(nums[i] + result[i - 2], result[i - 1])
        print(result)
        return result[n-1]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [([1,2,3,1], 4),
             ([2,7,9,3,1], 12),
             ([2,1,1,2], 4)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.rob(input), expected)

    
   