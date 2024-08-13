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


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:

    @timeit
    def maxProfit(self, prices: List[int]) -> int:
        min_idx = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
                continue
            if prices[i] > prices[min_idx]:
                max_profit = max(max_profit, prices[i]-prices[min_idx])
        return max_profit

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([7,1,3,2,2,2], 2),
        ([6,1,3,2,4,7], 6)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxProfit(input), expected)

    
   