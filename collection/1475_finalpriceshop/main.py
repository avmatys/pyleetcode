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


# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
class Solution:

    @timeit
    def finalPrices(self, prices: List[int]) -> List[int]:
      
        n = len(prices)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            price = prices[i]
            while stack and prices[stack[-1]] > price:
               stack.pop()
            result[i] = price - prices[stack[-1]] if stack else price
            stack.append(i)
        return result


def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
             ([1,2,3,4,5], [1,2,3,4,5]),
             ([8,4,6,2,3], [4,2,4,2,3])
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.finalPrices(input), expected)

    
   