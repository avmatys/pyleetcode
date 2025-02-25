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


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:

    @timeit
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices) # day of the sell
        m = 2 # state - we have a stock or no
        dp = [[[-1 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

        def calculate(i, hold_stock, remaining):
            if i >= n or remaining == 0:
                return 0
            if dp[i][hold_stock][remaining] != -1:
                return dp[i][hold_stock][remaining]
            # For any state we can skip current position
            skip_profit = calculate(i + 1, hold_stock, remaining)
            # If we have a stock - we can sell
            if hold_stock:
                max_profit = max(skip_profit, prices[i] + calculate(i + 1, False, remaining - 1))
            # If we don't have - we can buy
            else:
                max_profit = max(skip_profit, -prices[i] + calculate(i + 1, True, remaining))
            #  Store in the memo table to 
            dp[i][hold_stock][remaining] = max_profit
            return max_profit

        return calculate(0, False, k) 

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (([3,3,5,0,0,3,1,4], 3), 8),
        (([7,1,5,3,6,4], 2), 7),
        (([1,2,3,4,5], 2), 4),
        (([7,1,3,2,2], 10), 2),
        (([7,1,3,10,5,20], 10), 24),
        (([7,1,3,10,11,2,10], 10), 18),
        (([2,4,1], 2), 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxProfit(*input), expected)

    
   