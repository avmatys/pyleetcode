from typing import List
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


# https://leetcode.com/problems/number-of-1-bits/description/
class Solution:

    @timeit
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones^num)&~twos
            twos = (twos^num)&~ones
        return ones 

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([2,2,3,2], 3)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.singleNumber(input), expected)

    
   