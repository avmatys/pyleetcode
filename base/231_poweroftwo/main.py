from typing import List
from datetime import datetime
from collections import deque

# Track execution time of the function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        value = func(*args, **kwargs)
        end = datetime.now()
        print(f"Time: {end-start}")
        return value
    return wrapper


# https://leetcode.com/problems/power-of-two/description/
class Solution:

    @timeit
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0

def judge(result, expected):
    print(f'Result {result} Expected {expected}')
    assert result == expected
    

if __name__ == '__main__':
    solution = Solution()
    cases = [
        (3, False),
        (4, True),
        (-16, False)
    ]
    for case in cases:
        input = case[0]
        expected = case[1]
        judge(solution.isPowerOfTwo(input), expected)

    
   