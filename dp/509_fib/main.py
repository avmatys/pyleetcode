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
    def fib(self, n: int) -> int:
       if n < 2:
           return n
       prev = 0
       curr = 1
       for i in range(1, n):
           tmp = curr
           curr += prev
           prev = tmp
       return curr

    

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (1, 1),
        (0, 0)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.fib(input), expected)

    
   