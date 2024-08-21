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


# https://leetcode.com/problems/divisor-game/
class Solution:

    @timeit
    def divisorGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        for i in range(2, n+1): # Start form of the dp array
            for x in range (1, i): # Try to chec all digits 0 < x < i
                if i % x == 0: # Restriction from the task
                    dp[i] = dp[i] | ~dp[i-x] # We should set True if previously this element was set to true or if previous step (i-x) was False
        return bool(dp[n])
    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3, False),
        (2, True),
        (1, False),
        (4, True),
        (100, True)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.divisorGame(input), expected)

    
   