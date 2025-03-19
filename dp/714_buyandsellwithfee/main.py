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

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, not_hold = -prices[0], 0 
        for price in prices[1:]:
            thold = hold
            hold = max(hold, not_hold - price)
            not_hold = max(not_hold, price + thold - fee)
        return max(hold, not_hold)      

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

