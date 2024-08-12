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


# https://leetcode.com/problems/climbing-stairs/description/
class Solution:

    @timeit
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n+1):
           dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (2, 2),
        (3, 3), 
        (4, 5),
        (1, 1)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.climbStairs(input), expected)

    
   