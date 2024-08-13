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


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:

    @timeit
    def maxProfit(self, prices: List[int]) -> int:
        min_idx = 0
        max_idx = min_idx
        max_profit = 0
        for i in range(1, len(prices)):
            # If new element is still bigger - don't sell stocks, continue looking for local max
            if prices[i] > prices[max_idx]:
                max_idx = i
            # If current element is less than min or max or it's end of the array - sell can buy new stocks
            if prices[i] < prices[min_idx] or prices[i] < prices[max_idx] or i == len(prices) - 1:
                max_profit += prices[max_idx] - prices[min_idx]
                min_idx = i
                max_idx = i
        return max_profit

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,1,3,2,2], 2),
        ([7,1,3,10,5,20], 24),
        ([7,1,3,10,11,2,10], 18),
        ([2,4,1], 2)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.maxProfit(input), expected)

    
   