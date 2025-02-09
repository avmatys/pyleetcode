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


# https://leetcode.com/problems/coin-change/description/
class Solution:

    @timeit
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                coins_count = [dp[i - c] for c in coins if c < i]
                if len(coins_count) == 0: continue
                dp[i] = 1 + min(coins_count)
        return dp[amount] if dp[amount] != float('inf') else -1

def judge(result: str, expected: str):
    print(f'Result:   {result}')
    print(f'Expected: {expected}')
    assert result == expected    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([1,2,5], 11), 3),
        (([1,5,7], 21), 3),
        (([1,5,7], 2), 2),
        (([1,5,7], 16), 4),
        (([2], 3), -1),
        (([1], 0), 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.coinChange(*input), expected)

    
   