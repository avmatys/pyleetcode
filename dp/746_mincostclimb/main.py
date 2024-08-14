from typing import List
from datetime import datetime


# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:

    @timeit
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range (2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        dp[n] = min(dp[n-1],dp[n-2])
        return dp[n]
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([10,15,20], 15),
        ([1,100,1,1,1,100,1,1,100,1], 6)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.minCostClimbingStairs(input), expected)

    
   