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


# https://leetcode.com/problems/counting-bits/description/
class Solution:

    @timeit
    def countBits(self, n: int) -> List[int]:
        # Init array
        dp = [0] * (n + 1)
        # Each element is 2^n + offset
        for i in range(1,n+1):
            i_power = math.floor(math.log2(i))
            i_offset = int(i - math.pow(2, i_power))
            dp[i] = 1 + dp[i_offset]
        return dp
           
class SolutionRev:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1 , 1, 2, 1, 2]),
        (8, [0,1,1,2,1,2,2,3,1]),
        (0, [0])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.countBits(input), expected)

    
   
