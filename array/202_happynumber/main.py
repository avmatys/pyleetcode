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

# https://leetcode.com/problems/happy-number/?
class Solution:

    @timeit
    def isHappy(self, n: int) -> bool:
        def next_number(number):
            sum_squares = 0
            while number:
                digit = number % 10
                sum_squares += digit ** 2
                number //= 10
            return sum_squares
        nums = set()
        while n not in nums:
            nums.add(n)
            n = next_number(n)
            if n == 1:
                return True
        return False
        
    
def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (19, True),
        (2, False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isHappy(input), expected)


    
   